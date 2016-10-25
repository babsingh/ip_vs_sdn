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
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h26 = net.addHost('h26', cls=Host, ip='10.0.0.26', defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h28 = net.addHost('h28', cls=Host, ip='10.0.0.28', defaultRoute=None)
    h19 = net.addHost('h19', cls=Host, ip='10.0.0.19', defaultRoute=None)
    h24 = net.addHost('h24', cls=Host, ip='10.0.0.24', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h29 = net.addHost('h29', cls=Host, ip='10.0.0.29', defaultRoute=None)
    h20 = net.addHost('h20', cls=Host, ip='10.0.0.20', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h30 = net.addHost('h30', cls=Host, ip='10.0.0.30', defaultRoute=None)
    h21 = net.addHost('h21', cls=Host, ip='10.0.0.21', defaultRoute=None)
    h18 = net.addHost('h18', cls=Host, ip='10.0.0.18', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h31 = net.addHost('h31', cls=Host, ip='10.0.0.31', defaultRoute=None)
    h22 = net.addHost('h22', cls=Host, ip='10.0.0.22', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h32 = net.addHost('h32', cls=Host, ip='10.0.0.32', defaultRoute=None)
    h23 = net.addHost('h23', cls=Host, ip='10.0.0.23', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h27 = net.addHost('h27', cls=Host, ip='10.0.0.27', defaultRoute=None)
    h25 = net.addHost('h25', cls=Host, ip='10.0.0.25', defaultRoute=None)

    info( '*** Add links\n')
    s1h1 = {'bw':100,'delay':'2'}
    net.addLink(s1, h1, cls=TCLink , **s1h1)
    s1h2 = {'bw':100,'delay':'2'}
    net.addLink(s1, h2, cls=TCLink , **s1h2)
    s1h3 = {'bw':100,'delay':'2'}
    net.addLink(s1, h3, cls=TCLink , **s1h3)
    s1h4 = {'bw':100,'delay':'2'}
    net.addLink(s1, h4, cls=TCLink , **s1h4)
    s1h5 = {'bw':100,'delay':'2'}
    net.addLink(s1, h5, cls=TCLink , **s1h5)
    s1h6 = {'bw':100,'delay':'2'}
    net.addLink(s1, h6, cls=TCLink , **s1h6)
    s1h7 = {'bw':100,'delay':'2'}
    net.addLink(s1, h7, cls=TCLink , **s1h7)
    s1h8 = {'bw':100,'delay':'2'}
    net.addLink(s1, h8, cls=TCLink , **s1h8)
    s1h9 = {'bw':100,'delay':'2'}
    net.addLink(s1, h9, cls=TCLink , **s1h9)
    s1h10 = {'bw':100,'delay':'2'}
    net.addLink(s1, h10, cls=TCLink , **s1h10)
    s1h11 = {'bw':100,'delay':'2'}
    net.addLink(s1, h11, cls=TCLink , **s1h11)
    s1h12 = {'bw':100,'delay':'2'}
    net.addLink(s1, h12, cls=TCLink , **s1h12)
    s1h13 = {'bw':100,'delay':'2'}
    net.addLink(s1, h13, cls=TCLink , **s1h13)
    s1h14 = {'bw':100,'delay':'2'}
    net.addLink(s1, h14, cls=TCLink , **s1h14)
    s1h15 = {'bw':100,'delay':'2'}
    net.addLink(s1, h15, cls=TCLink , **s1h15)
    s1h16 = {'bw':100,'delay':'2'}
    net.addLink(s1, h16, cls=TCLink , **s1h16)
    s1h17 = {'bw':100,'delay':'2'}
    net.addLink(s1, h17, cls=TCLink , **s1h17)
    s1h18 = {'bw':100,'delay':'2'}
    net.addLink(s1, h18, cls=TCLink , **s1h18)
    s1h19 = {'bw':100,'delay':'2'}
    net.addLink(s1, h19, cls=TCLink , **s1h19)
    s1h20 = {'bw':100,'delay':'2'}
    net.addLink(s1, h20, cls=TCLink , **s1h20)
    s1h21 = {'bw':100,'delay':'2'}
    net.addLink(s1, h21, cls=TCLink , **s1h21)
    s1h22 = {'bw':100,'delay':'2'}
    net.addLink(s1, h22, cls=TCLink , **s1h22)
    s1h23 = {'bw':100,'delay':'2'}
    net.addLink(s1, h23, cls=TCLink , **s1h23)
    s1h24 = {'bw':100,'delay':'2'}
    net.addLink(s1, h24, cls=TCLink , **s1h24)
    s1h25 = {'bw':100,'delay':'2'}
    net.addLink(s1, h25, cls=TCLink , **s1h25)
    s1h26 = {'bw':100,'delay':'2'}
    net.addLink(s1, h26, cls=TCLink , **s1h26)
    s1h27 = {'bw':100,'delay':'2'}
    net.addLink(s1, h27, cls=TCLink , **s1h27)
    s1h28 = {'bw':100,'delay':'2'}
    net.addLink(s1, h28, cls=TCLink , **s1h28)
    s1h29 = {'bw':100,'delay':'2'}
    net.addLink(s1, h29, cls=TCLink , **s1h29)
    s1h30 = {'bw':100,'delay':'2'}
    net.addLink(s1, h30, cls=TCLink , **s1h30)
    s1h31 = {'bw':100,'delay':'2'}
    net.addLink(s1, h31, cls=TCLink , **s1h31)
    s1h32 = {'bw':100,'delay':'2'}
    net.addLink(s1, h32, cls=TCLink , **s1h32)


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

