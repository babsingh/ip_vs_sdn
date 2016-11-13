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
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)

    info( '*** Add links\n')
    h1s8 = {'bw':100,'delay':'2'}
    net.addLink(h1, s8, link=TCLink , **h1s8)
    s8s4 = {'bw':100,'delay':'2'}
    net.addLink(s8, s4, link=TCLink , **s8s4)
    s9s4 = {'bw':100,'delay':'2'}
    net.addLink(s9, s4, link=TCLink , **s9s4)
    s10s5 = {'bw':100,'delay':'2'}
    net.addLink(s10, s5, link=TCLink , **s10s5)
    s11s5 = {'bw':100,'delay':'2'}
    net.addLink(s11, s5, link=TCLink , **s11s5)
    s12s6 = {'bw':100,'delay':'2'}
    net.addLink(s12, s6, link=TCLink , **s12s6)
    s13s6 = {'bw':100,'delay':'2'}
    net.addLink(s13, s6, link=TCLink , **s13s6)
    s14s7 = {'bw':100,'delay':'2'}
    net.addLink(s14, s7, link=TCLink , **s14s7)
    s15s7 = {'bw':100,'delay':'2'}
    net.addLink(s15, s7, link=TCLink , **s15s7)
    s4s2 = {'bw':100,'delay':'2'}
    net.addLink(s4, s2, link=TCLink , **s4s2)
    s5s2 = {'bw':100,'delay':'2'}
    net.addLink(s5, s2, link=TCLink , **s5s2)
    s6s3 = {'bw':100,'delay':'2'}
    net.addLink(s6, s3, link=TCLink , **s6s3)
    s7s3 = {'bw':100,'delay':'2'}
    net.addLink(s7, s3, link=TCLink , **s7s3)
    s2s1 = {'bw':100,'delay':'2'}
    net.addLink(s2, s1, link=TCLink , **s2s1)
    s3s1 = {'bw':100,'delay':'2'}
    net.addLink(s3, s1, link=TCLink , **s3s1)
    s8h2 = {'bw':100,'delay':'2'}
    net.addLink(s8, h2, link=TCLink , **s8h2)
    s9h3 = {'bw':100,'delay':'2'}
    net.addLink(s9, h3, link=TCLink , **s9h3)
    s10h5 = {'bw':100,'delay':'2'}
    net.addLink(s10, h5, link=TCLink , **s10h5)
    s10h6 = {'bw':100,'delay':'2'}
    net.addLink(s10, h6, link=TCLink , **s10h6)
    s11h7 = {'bw':100,'delay':'2'}
    net.addLink(s11, h7, link=TCLink , **s11h7)
    s11h8 = {'bw':100,'delay':'2'}
    net.addLink(s11, h8, link=TCLink , **s11h8)
    s9h4 = {'bw':100,'delay':'2'}
    net.addLink(s9, h4, link=TCLink , **s9h4)
    s12h10 = {'bw':100,'delay':'2'}
    net.addLink(s12, h10, link=TCLink , **s12h10)
    s12h11 = {'bw':100,'delay':'2'}
    net.addLink(s12, h11, link=TCLink , **s12h11)
    s13h12 = {'bw':100,'delay':'2'}
    net.addLink(s13, h12, link=TCLink , **s13h12)
    s13h13 = {'bw':100,'delay':'2'}
    net.addLink(s13, h13, link=TCLink , **s13h13)
    s14h14 = {'bw':100,'delay':'2'}
    net.addLink(s14, h14, link=TCLink , **s14h14)
    s14h15 = {'bw':100,'delay':'2'}
    net.addLink(s14, h15, link=TCLink , **s14h15)
    s15h16 = {'bw':100,'delay':'2'}
    net.addLink(s15, h16, link=TCLink , **s15h16)
    s15h17 = {'bw':100,'delay':'2'}
    net.addLink(s15, h17, link=TCLink , **s15h17)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s4').start([c0])
    net.get('s6').start([c0])
    net.get('s2').start([c0])
    net.get('s12').start([c0])
    net.get('s11').start([c0])
    net.get('s10').start([c0])
    net.get('s9').start([c0])
    net.get('s14').start([c0])
    net.get('s3').start([c0])
    net.get('s8').start([c0])
    net.get('s5').start([c0])
    net.get('s15').start([c0])
    net.get('s7').start([c0])
    net.get('s13').start([c0])
    net.get('s1').start([c0])

    info( '*** Configuring switches\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

