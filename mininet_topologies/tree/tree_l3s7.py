#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)

    info( '*** Add links\n')
    s3s1 = {'bw':100,'delay':'2'}
    net.addLink(s3, s1, cls=TCLink , **s3s1)
    h1s4 = {'bw':100,'delay':'2'}
    net.addLink(h1, s4, cls=TCLink , **h1s4)
    h2s5 = {'bw':100,'delay':'2'}
    net.addLink(h2, s5, cls=TCLink , **h2s5)
    h3s6 = {'bw':100,'delay':'2'}
    net.addLink(h3, s6, cls=TCLink , **h3s6)
    h4s7 = {'bw':100,'delay':'2'}
    net.addLink(h4, s7, cls=TCLink , **h4s7)
    s7s3 = {'bw':100,'delay':'2'}
    net.addLink(s7, s3, cls=TCLink , **s7s3)
    s6s3 = {'bw':100,'delay':'2'}
    net.addLink(s6, s3, cls=TCLink , **s6s3)
    s4s2 = {'bw':100,'delay':'2'}
    net.addLink(s4, s2, cls=TCLink , **s4s2)
    s5s2 = {'bw':100,'delay':'2'}
    net.addLink(s5, s2, cls=TCLink , **s5s2)
    s2s1 = {'bw':100,'delay':'2'}
    net.addLink(s2, s1, cls=TCLink , **s2s1)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s7').start([c0])
    net.get('s2').start([c0])
    net.get('s5').start([c0])
    net.get('s4').start([c0])
    net.get('s3').start([c0])
    net.get('s6').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

