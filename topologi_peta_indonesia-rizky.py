#!/usr/bin/env python

" Custom Topology to use ONOS Controller"

from mininet.topo import Topo
from mininet.log import setLogLevel, info

class MyTopo( Topo ):

    def addSwitch(self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13'}
        kwargs.update( opts )
        return super(MyTopo, self).addSwitch( name, **kwargs )

    def __init__( self ):
        "Create MyTopo topology..."
        
        # Inisialisasi Topology
        Topo.__init__( self )

        # Tambahkan node, switch, dan host

        info( '*** Add switches\n')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')
        s13 = self.addSwitch('s13')
        s14 = self.addSwitch('s14')
        s15 = self.addSwitch('s15')

        info( '*** Add hosts\n')
        h1 = self.addHost('h1', ip='111.99.2.1')
        h2 = self.addHost('h2', ip='111.99.3.2')
        h3 = self.addHost('h3', ip='111.99.4.3')
        h4 = self.addHost('h4', ip='111.99.6.4')
        h5 = self.addHost('h5', ip='111.99.7.5')
        h6 = self.addHost('h6', ip='111.99.8.6')
        h7 = self.addHost('h7', ip='111.99.9.7')
        h8 = self.addHost('h8', ip='111.99.10.8')
        h9 = self.addHost('h9', ip='111.99.11.9')
        h10 = self.addHost('h10', ip='111.99.12.10')
        h11 = self.addHost('h11', ip='111.99.13.11')
        h12 = self.addHost('h12', ip='111.99.14.12')

        info( '*** Add links\n')
        self.addLink(s2, h1)
        self.addLink(s3, h2)
        self.addLink(s4, h3)
        self.addLink(s6, h4)
        self.addLink(s7, h5)
        self.addLink(s8, h6)
        self.addLink(s9, h7)
        self.addLink(s10, h8)
        self.addLink(s11, h9)
        self.addLink(s12, h10)
        self.addLink(s13, h11)
        self.addLink(s14, h12)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s3, s4)
        self.addLink(s3, s5)
        self.addLink(s4, s5)
        self.addLink(s2, s6)
        self.addLink(s4, s6)
        self.addLink(s5, s6)
        self.addLink(s4, s7)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s7, s9)
        self.addLink(s8, s9)
        self.addLink(s8, s10)
        self.addLink(s8, s11)
        self.addLink(s9, s10)
        self.addLink(s9, s11)
        self.addLink(s9, s12)
        self.addLink(s7, s13)
        self.addLink(s11, s13)
        self.addLink(s11, s14)
        self.addLink(s12, s14)
        self.addLink(s13, s14)
        self.addLink(s14, s15)

topos = { 'mytopo': ( lambda: MyTopo() ) }
    
if __name__ == '__main__':
    from onosnet import run
    run( MyTopo() )
