#!/usr/bin/python

import sys, getopt
from mininet.topo import Topo
from mininet.topolib import TreeTopo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel

class LinearTopo(Topo):
   "Linear topology of k switches, with one host per switch."

   def __init__(self, k=2, **opts):
       """Init.
           k: number of switches (and hosts)
           hconf: host configuration options
           lconf: link configuration options"""

       super(LinearTopo, self).__init__(**opts)

       self.k = k

       lastSwitch = None
       for i in irange(1, k):
           host = self.addHost('h%s' % i, cpu=.5/k)
           switch = self.addSwitch('s%s' % i)
           # 10 Mbps, 5ms delay, 1% loss, 1000 packet queue
           self.addLink( host, switch, bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
           if lastSwitch:
               self.addLink(switch, lastSwitch, bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
           lastSwitch = switch

class SingleSwitchTopo(Topo):
   "Single switch connected to n hosts."
   def __init__(self, k=2, **opts):
       # Initialize topology and default options
       Topo.__init__(self, **opts)
       switch = self.addSwitch('s1')
       # Python's range(N) generates 0..N-1
       for h in range(k):
           host = self.addHost('h%s' % (h + 1))
           self.addLink(host, switch)

def perfTest(argv):

   type = ''
   numHosts = 2
   depth = 2
   fanout = 2

   try:
      opts, args = getopt.getopt(argv,"ht:n:d:f:",["type=","hosts=","depth=","fanout="])
   except getopt.GetoptError:
      print 'topo_mininet.py -t <topo> -n <hosts>'
      print 'topo_mininet.py -t <topo> -d <depth> -f <fanout>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
        print 'topo_mininet.py -t <topo> -h <hosts>'
        print 'topo_mininet.py -t <topo> -d <depth> -f <fanout>' 
	sys.exit()
      elif opt in ("-t", "--type"):
         type = arg
      elif opt in ("-n", "--hosts"):
         numHosts = arg
      elif opt in ("-d", "--depth"):
         depth = arg
      elif opt in ("-f", "--fanout"):
         fanout = arg

   print 'type - ', type
   
   if type == 'tree':
      print 'depth - ', depth
      print 'fanout - ', fanout   
   else:
      print 'hosts - ', numHosts

   "Create network and run simple performance test"

   if type == 'linear':
      print 'generating linear topology'
      topo = LinearTopo( k= int(numHosts) )
   elif type == 'single':
      print 'generating single switch topology'
      topo = SingleSwitchTopo( k= int(numHosts) )
   elif type == 'tree':
      print 'generating tree topology'
      topo = TreeTopo( depth= int(depth), fanout= int(fanout) )
   else:
      print 'invalid topology'
      print 'valid topology: single, linear or tree'
      sys.exit(2)


   net = Mininet(topo=topo,
                 host=CPULimitedHost, link=TCLink)
   net.start()
   print "Dumping host connections"
   dumpNodeConnections(net.hosts)
   print "Testing network connectivity"
   net.pingAll()
   print "Testing bandwidth between h1 and h4"
   h1, h4 = net.get('h1', 'h4')
   net.iperf((h1, h4))
   net.stop()

if __name__ == '__main__':
   setLogLevel('info')
   perfTest(sys.argv[1:])
