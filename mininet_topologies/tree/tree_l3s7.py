#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      port=6633)

    info( '*** Add switches\n')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)

    info( '*** Add links\n')
    s3s1 = {'bw':100,'delay':'2ms'}
    net.addLink(s3, s1, cls=TCLink , **s3s1)
    h1s4 = {'bw':100,'delay':'2ms'}
    net.addLink(h1, s4, cls=TCLink , **h1s4)
    s7s3 = {'bw':100,'delay':'2ms'}
    net.addLink(s7, s3, cls=TCLink , **s7s3)
    s6s3 = {'bw':100,'delay':'2ms'}
    net.addLink(s6, s3, cls=TCLink , **s6s3)
    s4s2 = {'bw':100,'delay':'2ms'}
    net.addLink(s4, s2, cls=TCLink , **s4s2)
    s5s2 = {'bw':100,'delay':'2ms'}
    net.addLink(s5, s2, cls=TCLink , **s5s2)
    s2s1 = {'bw':100,'delay':'2ms'}
    net.addLink(s2, s1, cls=TCLink , **s2s1)
    s4h2 = {'bw':100,'delay':'2ms'}
    net.addLink(s4, h2, cls=TCLink , **s4h2)
    s5h3 = {'bw':100,'delay':'2ms'}
    net.addLink(s5, h3, cls=TCLink , **s5h3)
    s5h4 = {'bw':100,'delay':'2ms'}
    net.addLink(s5, h4, cls=TCLink , **s5h4)
    s6h5 = {'bw':100,'delay':'2ms'}
    net.addLink(s6, h5, cls=TCLink , **s6h5)
    s6h6 = {'bw':100,'delay':'2ms'}
    net.addLink(s6, h6, cls=TCLink , **s6h6)
    s7h7 = {'bw':100,'delay':'2ms'}
    net.addLink(s7, h7, cls=TCLink , **s7h7)
    s7h8 = {'bw':100,'delay':'2ms'}
    net.addLink(s7, h8, cls=TCLink , **s7h8)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s5').start([c0])
    net.get('s4').start([c0])
    net.get('s1').start([c0])
    net.get('s3').start([c0])
    net.get('s7').start([c0])
    net.get('s6').start([c0])
    net.get('s2').start([c0])

    info( '*** Configuring switches\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

