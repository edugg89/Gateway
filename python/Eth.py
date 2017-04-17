'''
Created on 13 abr. 2017

@author: Edu
'''

from winpcapy import WinPcapDevices
from winpcapy import WinPcapUtils
import time
import signal
import sys
import IPLayer



def miprueba():
     IPLayer.IP_handler()

def mypacket_printer_callback(win_pcap, param, header, pkt_data):
        a = ':'.join(hex(ord(x))[2:] for x in pkt_data)
        try:
            IPLayer.IP_handler()
            
        except KeyboardInterrupt:
            print("me parooooo")
            win_pcap.stop()


    
class EthDebugger(object):
    '''
    A class that allows sending and receiving raw ethernet packets
    '''
    
    
    def __init__(self,srcMAC,dstMAC):
        '''
        Constructor
        '''
        self.SrcMAC = srcMAC
        self.DstMAC = dstMAC
        print("List of devices:")
        devices = WinPcapDevices.list_devices()
        for device in devices:
            print(device,devices[device])
       
       
        
    def SendPacket(self,data):
        '''
        Sends a an ethernet packet to dstMAC and SRCmac definedd in contructor
        '''    
        packet = '{dstMAC}{srcMAC}{payload}'.format(dstMAC = self.DstMAC, srcMAC = self.SrcMAC, payload =data )
        #arp_request_hex_template = "%(dst_mac)s%(src_mac)s08060001080006040001" \
        #                   "%(sender_mac)s%(sender_ip)s%(target_mac)s%(target_ip)s" + "00" * 18
        #packet = arp_request_hex_template % {
        #"dst_mac": "aa"*6,
        #"src_mac": "bb"*6,
        #"sender_mac": "bb"*6,
        #"target_mac": "cc"*6,
        # 192.168.0.1
        #"sender_ip": "c0a80001",
        # 192.168.0.2
        #"target_ip": "c0a80002"
        #}
        #print packet
        #WinPcapUtils.send_packet("*Ethernet*", packet.decode("hex"))
        # Add padding if necessary
        #if (len(packet)<120):
        #    packet = packet + "00" * (60-len(packet)/2)
        
        #WinPcapUtils.send_packet("*Ethernet*", packet.decode("hex"))
        self.SendRawPacket(packet)
        
    def SendRawPacket(self,data):
        '''
        Sends a raw packet
        '''    
        # Add padding if necessary
        if (len(data)<120):
            data = data + "00" * (60-len(data)/2)
        
        WinPcapUtils.send_packet("*Ethernet*", data.decode("hex"))
    
    def RecvRawPacket(self):
        # WinPcapUtils.capture_on_and_print("*Ethernet*")
        WinPcapUtils.capture_on("*Ethernet*",mypacket_printer_callback)

    def SendARPreq(self,SrcIP,DstIP):
        packet = "ffffffffffff{srcMAC}08060001080006040001{srcMAC}{srcIP}000000000000{dstIP}".format(srcIP=SrcIP, dstIP= DstIP, srcMAC= self.SrcMAC )       
        self.SendRawPacket(packet)
        
        
myDebugger = EthDebugger("aaaaaaaaaaaa","bbbbbbbbbbbb") 
myDebugger.SendPacket("0800aa")
myDebugger.SendARPreq("c0a80001","c0a80002")
miprueba()
# myDebugger.RecvRawPacket()
print("end")