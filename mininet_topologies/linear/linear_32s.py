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
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s23 = net.addSwitch('s23', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s18 = net.addSwitch('s18', cls=OVSKernelSwitch)
    s16 = net.addSwitch('s16', cls=OVSKernelSwitch)
    s20 = net.addSwitch('s20', cls=OVSKernelSwitch)
    s31 = net.addSwitch('s31', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s28 = net.addSwitch('s28', cls=OVSKernelSwitch)
    s19 = net.addSwitch('s19', cls=OVSKernelSwitch)
    s30 = net.addSwitch('s30', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s21 = net.addSwitch('s21', cls=OVSKernelSwitch)
    s32 = net.addSwitch('s32', cls=OVSKernelSwitch)
    s26 = net.addSwitch('s26', cls=OVSKernelSwitch)
    s22 = net.addSwitch('s22', cls=OVSKernelSwitch)
    s29 = net.addSwitch('s29', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s27 = net.addSwitch('s27', cls=OVSKernelSwitch)
    s24 = net.addSwitch('s24', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s17 = net.addSwitch('s17', cls=OVSKernelSwitch)
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch)
    s25 = net.addSwitch('s25', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h30 = net.addHost('h30', cls=Host, ip='10.0.0.30', defaultRoute=None)
    h20 = net.addHost('h20', cls=Host, ip='10.0.0.20', defaultRoute=None)
    h26 = net.addHost('h26', cls=Host, ip='10.0.0.26', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h27 = net.addHost('h27', cls=Host, ip='10.0.0.27', defaultRoute=None)
    h25 = net.addHost('h25', cls=Host, ip='10.0.0.25', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h22 = net.addHost('h22', cls=Host, ip='10.0.0.22', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h19 = net.addHost('h19', cls=Host, ip='10.0.0.19', defaultRoute=None)
    h24 = net.addHost('h24', cls=Host, ip='10.0.0.24', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h28 = net.addHost('h28', cls=Host, ip='10.0.0.28', defaultRoute=None)
    h21 = net.addHost('h21', cls=Host, ip='10.0.0.21', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h31 = net.addHost('h31', cls=Host, ip='10.0.0.31', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h32 = net.addHost('h32', cls=Host, ip='10.0.0.32', defaultRoute=None)
    h18 = net.addHost('h18', cls=Host, ip='10.0.0.18', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h29 = net.addHost('h29', cls=Host, ip='10.0.0.29', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h23 = net.addHost('h23', cls=Host, ip='10.0.0.23', defaultRoute=None)

    info( '*** Add links\n')
    h1s1 = {'bw':100,'delay':'2ms'}
    net.addLink(h1, s1, cls=TCLink , **h1s1)
    h2s2 = {'bw':100,'delay':'2ms'}
    net.addLink(h2, s2, cls=TCLink , **h2s2)
    s2s1 = {'bw':100,'delay':'2ms'}
    net.addLink(s2, s1, cls=TCLink , **s2s1)
    s2s3 = {'bw':100,'delay':'2ms'}
    net.addLink(s2, s3, cls=TCLink , **s2s3)
    s3h3 = {'bw':100,'delay':'2ms'}
    net.addLink(s3, h3, cls=TCLink , **s3h3)
    s3s4 = {'bw':100,'delay':'2ms'}
    net.addLink(s3, s4, cls=TCLink , **s3s4)
    s4h4 = {'bw':100,'delay':'2ms'}
    net.addLink(s4, h4, cls=TCLink , **s4h4)
    s4s5 = {'bw':100,'delay':'2ms'}
    net.addLink(s4, s5, cls=TCLink , **s4s5)
    s5h5 = {'bw':100,'delay':'2ms'}
    net.addLink(s5, h5, cls=TCLink , **s5h5)
    s5s6 = {'bw':100,'delay':'2ms'}
    net.addLink(s5, s6, cls=TCLink , **s5s6)
    s6h6 = {'bw':100,'delay':'2ms'}
    net.addLink(s6, h6, cls=TCLink , **s6h6)
    s6s7 = {'bw':100,'delay':'2ms'}
    net.addLink(s6, s7, cls=TCLink , **s6s7)
    s7h7 = {'bw':100,'delay':'2ms'}
    net.addLink(s7, h7, cls=TCLink , **s7h7)
    s7s8 = {'bw':100,'delay':'2ms'}
    net.addLink(s7, s8, cls=TCLink , **s7s8)
    s8h8 = {'bw':100,'delay':'2ms'}
    net.addLink(s8, h8, cls=TCLink , **s8h8)
    h32s32 = {'bw':100,'delay':'2ms'}
    net.addLink(h32, s32, cls=TCLink , **h32s32)
    s32s31 = {'bw':100,'delay':'2ms'}
    net.addLink(s32, s31, cls=TCLink , **s32s31)
    s31h31 = {'bw':100,'delay':'2ms'}
    net.addLink(s31, h31, cls=TCLink , **s31h31)
    s31s30 = {'bw':100,'delay':'2ms'}
    net.addLink(s31, s30, cls=TCLink , **s31s30)
    s30h30 = {'bw':100,'delay':'2ms'}
    net.addLink(s30, h30, cls=TCLink , **s30h30)
    h29s29 = {'bw':100,'delay':'2ms'}
    net.addLink(h29, s29, cls=TCLink , **h29s29)
    s29s30 = {'bw':100,'delay':'2ms'}
    net.addLink(s29, s30, cls=TCLink , **s29s30)
    s29s28 = {'bw':100,'delay':'2ms'}
    net.addLink(s29, s28, cls=TCLink , **s29s28)
    s28h28 = {'bw':100,'delay':'2ms'}
    net.addLink(s28, h28, cls=TCLink , **s28h28)
    s27h27 = {'bw':100,'delay':'2ms'}
    net.addLink(s27, h27, cls=TCLink , **s27h27)
    s26h26 = {'bw':100,'delay':'2ms'}
    net.addLink(s26, h26, cls=TCLink , **s26h26)
    s25h25 = {'bw':100,'delay':'2ms'}
    net.addLink(s25, h25, cls=TCLink , **s25h25)
    s25s26 = {'bw':100,'delay':'2ms'}
    net.addLink(s25, s26, cls=TCLink , **s25s26)
    s26s27 = {'bw':100,'delay':'2ms'}
    net.addLink(s26, s27, cls=TCLink , **s26s27)
    s27s28 = {'bw':100,'delay':'2ms'}
    net.addLink(s27, s28, cls=TCLink , **s27s28)
    s25s24 = {'bw':100,'delay':'2ms'}
    net.addLink(s25, s24, cls=TCLink , **s25s24)
    s24h24 = {'bw':100,'delay':'2ms'}
    net.addLink(s24, h24, cls=TCLink , **s24h24)
    s23s24 = {'bw':100,'delay':'2ms'}
    net.addLink(s23, s24, cls=TCLink , **s23s24)
    s23h23 = {'bw':100,'delay':'2ms'}
    net.addLink(s23, h23, cls=TCLink , **s23h23)
    s22h22 = {'bw':100,'delay':'2ms'}
    net.addLink(s22, h22, cls=TCLink , **s22h22)
    s22s23 = {'bw':100,'delay':'2ms'}
    net.addLink(s22, s23, cls=TCLink , **s22s23)
    s22s21 = {'bw':100,'delay':'2ms'}
    net.addLink(s22, s21, cls=TCLink , **s22s21)
    s21h21 = {'bw':100,'delay':'2ms'}
    net.addLink(s21, h21, cls=TCLink , **s21h21)
    h20s20 = {'bw':100,'delay':'2ms'}
    net.addLink(h20, s20, cls=TCLink , **h20s20)
    s20s21 = {'bw':100,'delay':'2ms'}
    net.addLink(s20, s21, cls=TCLink , **s20s21)
    s20s19 = {'bw':100,'delay':'2ms'}
    net.addLink(s20, s19, cls=TCLink , **s20s19)
    s19h19 = {'bw':100,'delay':'2ms'}
    net.addLink(s19, h19, cls=TCLink , **s19h19)
    s19s18 = {'bw':100,'delay':'2ms'}
    net.addLink(s19, s18, cls=TCLink , **s19s18)
    s18h18 = {'bw':100,'delay':'2ms'}
    net.addLink(s18, h18, cls=TCLink , **s18h18)
    h13s13 = {'bw':100,'delay':'2ms'}
    net.addLink(h13, s13, cls=TCLink , **h13s13)
    h14s14 = {'bw':100,'delay':'2ms'}
    net.addLink(h14, s14, cls=TCLink , **h14s14)
    h15s15 = {'bw':100,'delay':'2ms'}
    net.addLink(h15, s15, cls=TCLink , **h15s15)
    h16s16 = {'bw':100,'delay':'2ms'}
    net.addLink(h16, s16, cls=TCLink , **h16s16)
    h17s17 = {'bw':100,'delay':'2ms'}
    net.addLink(h17, s17, cls=TCLink , **h17s17)
    s17s18 = {'bw':100,'delay':'2ms'}
    net.addLink(s17, s18, cls=TCLink , **s17s18)
    s16s17 = {'bw':100,'delay':'2ms'}
    net.addLink(s16, s17, cls=TCLink , **s16s17)
    s15s16 = {'bw':100,'delay':'2ms'}
    net.addLink(s15, s16, cls=TCLink , **s15s16)
    s14s15 = {'bw':100,'delay':'2ms'}
    net.addLink(s14, s15, cls=TCLink , **s14s15)
    s13s14 = {'bw':100,'delay':'2ms'}
    net.addLink(s13, s14, cls=TCLink , **s13s14)
    h9s9 = {'bw':100,'delay':'2ms'}
    net.addLink(h9, s9, cls=TCLink , **h9s9)
    s8s9 = {'bw':100,'delay':'2ms'}
    net.addLink(s8, s9, cls=TCLink , **s8s9)
    s10s9 = {'bw':100,'delay':'2ms'}
    net.addLink(s10, s9, cls=TCLink , **s10s9)
    s10h10 = {'bw':100,'delay':'2ms'}
    net.addLink(s10, h10, cls=TCLink , **s10h10)
    s11h11 = {'bw':100,'delay':'2ms'}
    net.addLink(s11, h11, cls=TCLink , **s11h11)
    s12h12 = {'bw':100,'delay':'2ms'}
    net.addLink(s12, h12, cls=TCLink , **s12h12)
    s12s13 = {'bw':100,'delay':'2ms'}
    net.addLink(s12, s13, cls=TCLink , **s12s13)
    s11s12 = {'bw':100,'delay':'2ms'}
    net.addLink(s11, s12, cls=TCLink , **s11s12)
    s10h11 = {'bw':100,'delay':'2ms'}
    net.addLink(s10, s11, cls=TCLink , **s10h11)
    

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s8').start([c0])
    net.get('s6').start([c0])
    net.get('s23').start([c0])
    net.get('s11').start([c0])
    net.get('s12').start([c0])
    net.get('s18').start([c0])
    net.get('s16').start([c0])
    net.get('s20').start([c0])
    net.get('s31').start([c0])
    net.get('s3').start([c0])
    net.get('s28').start([c0])
    net.get('s19').start([c0])
    net.get('s30').start([c0])
    net.get('s9').start([c0])
    net.get('s1').start([c0])
    net.get('s21').start([c0])
    net.get('s32').start([c0])
    net.get('s26').start([c0])
    net.get('s22').start([c0])
    net.get('s29').start([c0])
    net.get('s4').start([c0])
    net.get('s27').start([c0])
    net.get('s24').start([c0])
    net.get('s13').start([c0])
    net.get('s17').start([c0])
    net.get('s15').start([c0])
    net.get('s25').start([c0])
    net.get('s2').start([c0])
    net.get('s7').start([c0])
    net.get('s14').start([c0])
    net.get('s10').start([c0])
    net.get('s5').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

