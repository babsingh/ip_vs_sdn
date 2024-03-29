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

    info( '*** Add hosts\n')
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)

    info( '*** Add links\n')
    h1s1 = {'bw':100,'delay':'2ms'}
    net.addLink(h1, s1, cls=TCLink , **h1s1)
    h2s1 = {'bw':100,'delay':'2ms'}
    net.addLink(h2, s1, cls=TCLink , **h2s1)
    h3s1 = {'bw':100,'delay':'2ms'}
    net.addLink(h3, s1, cls=TCLink , **h3s1)
    h4s1 = {'bw':100,'delay':'2ms'}
    net.addLink(h4, s1, cls=TCLink , **h4s1)
    h5s1 = {'bw':100,'delay':'2ms'}
    net.addLink(h5, s1, cls=TCLink , **h5s1)
    h6s1 = {'bw':100,'delay':'2ms'}
    net.addLink(h6, s1, cls=TCLink , **h6s1)
    h7s1 = {'bw':100,'delay':'2ms'}
    net.addLink(h7, s1, cls=TCLink , **h7s1)
    h8s1 = {'bw':100,'delay':'2ms'}
    net.addLink(h8, s1, cls=TCLink , **h8s1)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

