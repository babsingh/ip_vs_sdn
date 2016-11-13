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
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s16 = net.addSwitch('s16', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)

    info( '*** Add links\n')
    h1s1 = {'bw':100,'delay':'2'}
    net.addLink(h1, s1, cls=TCLink , **h1s1)
    h2s2 = {'bw':100,'delay':'2'}
    net.addLink(h2, s2, cls=TCLink , **h2s2)
    s2s1 = {'bw':100,'delay':'2'}
    net.addLink(s2, s1, cls=TCLink , **s2s1)
    s2s3 = {'bw':100,'delay':'2'}
    net.addLink(s2, s3, cls=TCLink , **s2s3)
    s3h3 = {'bw':100,'delay':'2'}
    net.addLink(s3, h3, cls=TCLink , **s3h3)
    s3s4 = {'bw':100,'delay':'2'}
    net.addLink(s3, s4, cls=TCLink , **s3s4)
    s4h4 = {'bw':100,'delay':'2'}
    net.addLink(s4, h4, cls=TCLink , **s4h4)
    s4s5 = {'bw':100,'delay':'2'}
    net.addLink(s4, s5, cls=TCLink , **s4s5)
    s5h5 = {'bw':100,'delay':'2'}
    net.addLink(s5, h5, cls=TCLink , **s5h5)
    s5s6 = {'bw':100,'delay':'2'}
    net.addLink(s5, s6, cls=TCLink , **s5s6)
    s6h6 = {'bw':100,'delay':'2'}
    net.addLink(s6, h6, cls=TCLink , **s6h6)
    s6s7 = {'bw':100,'delay':'2'}
    net.addLink(s6, s7, cls=TCLink , **s6s7)
    s7h7 = {'bw':100,'delay':'2'}
    net.addLink(s7, h7, cls=TCLink , **s7h7)
    s7s8 = {'bw':100,'delay':'2'}
    net.addLink(s7, s8, cls=TCLink , **s7s8)
    s8h8 = {'bw':100,'delay':'2'}
    net.addLink(s8, h8, cls=TCLink , **s8h8)
    s8s9 = {'bw':100,'delay':'2'}
    net.addLink(s8, s9, cls=TCLink , **s8s9)
    s9s10 = {'bw':100,'delay':'2'}
    net.addLink(s9, s10, cls=TCLink , **s9s10)
    s10s11 = {'bw':100,'delay':'2'}
    net.addLink(s10, s11, cls=TCLink , **s10s11)
    s11s12 = {'bw':100,'delay':'2'}
    net.addLink(s11, s12, cls=TCLink , **s11s12)
    s12s13 = {'bw':100,'delay':'2'}
    net.addLink(s12, s13, cls=TCLink , **s12s13)
    s13s14 = {'bw':100,'delay':'2'}
    net.addLink(s13, s14, cls=TCLink , **s13s14)
    s14s15 = {'bw':100,'delay':'2'}
    net.addLink(s14, s15, cls=TCLink , **s14s15)
    s15s16 = {'bw':100,'delay':'2'}
    net.addLink(s15, s16, cls=TCLink , **s15s16)
    h9s9 = {'bw':100,'delay':'2'}
    net.addLink(h9, s9, cls=TCLink , **h9s9)
    h10s10 = {'bw':100,'delay':'2'}
    net.addLink(h10, s10, cls=TCLink , **h10s10)
    h11s11 = {'bw':100,'delay':'2'}
    net.addLink(h11, s11, cls=TCLink , **h11s11)
    h12s12 = {'bw':100,'delay':'2'}
    net.addLink(h12, s12, cls=TCLink , **h12s12)
    h13s13 = {'bw':100,'delay':'2'}
    net.addLink(h13, s13, cls=TCLink , **h13s13)
    h14s14 = {'bw':100,'delay':'2'}
    net.addLink(h14, s14, cls=TCLink , **h14s14)
    h15s15 = {'bw':100,'delay':'2'}
    net.addLink(h15, s15, cls=TCLink , **h15s15)
    h16s16 = {'bw':100,'delay':'2'}
    net.addLink(h16, s16, cls=TCLink , **h16s16)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s11').start([c0])
    net.get('s1').start([c0])
    net.get('s6').start([c0])
    net.get('s9').start([c0])
    net.get('s13').start([c0])
    net.get('s5').start([c0])
    net.get('s2').start([c0])
    net.get('s16').start([c0])
    net.get('s10').start([c0])
    net.get('s7').start([c0])
    net.get('s15').start([c0])
    net.get('s8').start([c0])
    net.get('s12').start([c0])
    net.get('s14').start([c0])
    net.get('s4').start([c0])
    net.get('s3').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

