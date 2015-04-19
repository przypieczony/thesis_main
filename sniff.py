import socket, sys
from struct import *
import re
from math import fabs
import select
import random
import threading

class transmission():
    def __init__(self, ip_list):
        self.package_number=-1
        self.first_in_transmission=0
        self.ips=[]
        self.ip_list = ip_list
        self.package=[]
        self.graph=''
        print "ips w inicie: ", self.ips

    def __del__(self):
        print "died"

    def analyse(self, packet):
        self.package_number+=1
        self.package.append(packet)
        graph=''
        cseq=re.search(r'^CSeq: ([0-9]*) (.*)', self.package[self.package_number]['data'], re.MULTILINE)
        via_ip = self.package[self.package_number]['Via']
        source_ip=self.package[self.package_number]['source_ip']
        source_port=self.package[self.package_number]['source_port']
        destination_ip=self.package[self.package_number]['destination_ip']
        destination_port=self.package[self.package_number]['destination_port']
        print "sending ip: {} \ndestination ip: {}\nVia: {}".format(source_ip, destination_ip, via_ip)
        if cseq:
            return self.printGraph(source_ip, destination_ip, cseq)

    def printGraph(self, source_ip, destination_ip, cseq):
        """Return formatted SIP message flow and message"""
        distance = 25
        for ip in self.ip_list:
            if ip not in self.ips:
                self.ips.append(ip)
                graph = "{}{}{}{}\n".format(self.ip_list[0].ljust(distance), self.ip_list[1].ljust(distance), self.ip_list[2].ljust(15), self.ip_list[3].rjust(24))
        request=str(cseq.group(1).strip() + ' ' + cseq.group(2).strip())

        if source_ip == self.ips[0]:
            delimeter_first_pos = 0
        elif source_ip == self.ips[1]:
            delimeter_first_pos = 29
        elif source_ip == self.ips[2]:
            delimeter_first_pos = 58
        elif source_ip == self.ips[3]:
            delimeter_first_pos = 87

        if destination_ip == self.ips[0]:
            delimeter_second_pos = 0
        elif destination_ip == self.ips[1]:
            delimeter_second_pos = 29
        elif destination_ip == self.ips[2]:
            delimeter_second_pos = 58
        elif destination_ip == self.ips[3]:
            delimeter_second_pos = 87

        print "ips w getParameters: ", self.ips
        source_ip_id=self.ips.index(source_ip)
        destination_ip_id=self.ips.index(destination_ip)
        if source_ip_id < destination_ip_id:
            delimeter_first = '|'
            delimeter_second = '>|'
            left_indention = delimeter_first_pos
        elif source_ip_id == destination_ip_id: #when destination and source ip are the same print confusing message
            delimeter_first = '?'
            delimeter_second = '?|'
            left_indention = delimeter_first_pos
        else:
            delimeter_first = '|<'
            delimeter_second = '|'
            left_indention = delimeter_second_pos

        message_length=abs(delimeter_second_pos - delimeter_first_pos)-2 #to set message range
        graph = "{}{}{}{}\n".format(" "*(left_indention), delimeter_first, request.center(message_length, "-"), delimeter_second)
        message=str(self.package_number).center(8,'-')+'\n'+str(self.package[self.package_number]['data'])
        return {'graph':graph, 'message': message}
            
def sniff(transmission_protocol, ip_list):
    global sip_transmission
    try:
        sip_transmission
    except NameError:
        sip_transmission=transmission(ip_list)
    transmission_protocols={'UDP': socket.IPPROTO_UDP, 'TCP': socket.IPPROTO_TCP} #dictionary for transport protocol selection
    if transmission_protocol not in transmission_protocols.keys():
        sys.exit()
    try: #open a socket
        global sniff_socket
        sniff_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, transmission_protocols[transmission_protocol])

        #sniff_socket.settimeout(3)
    except socket.error, msg:
        print 'Socket could not be created. Error code: ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    print "before receive"
    packet = getData(sniff_socket) #get a packet from socket
    print "after receive"
    packet = packet[0]
    ip_header_packed = packet[0:20] #first 20 characters = ip header
    try:
        ip_header = unpack('!BBHHHBBH4s4s', ip_header_packed) #unpack ip header
    except:
        print 'unpacking error'
        return None

    version_ihl = ip_header[0] #get ip version and header length
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    ip_header_length = ihl * 4 

    ttl = ip_header[5] #time to leave
    protocol = ip_header[6] #transmission protocol, defined already, but why not [tcp=6; udp=17; icmp=1]
    source_address = socket.inet_ntoa(ip_header[8])
    destination_address = socket.inet_ntoa(ip_header[9])

    tcp_header_packed = packet[ip_header_length:ip_header_length+20] #get tcp header from whole packet
    try:
        tcp_header = unpack('!HHLLBBHHH', tcp_header_packed) #unpack it
    except:
        print 'unpacking error'
        return None
    
    source_port = tcp_header[0]
    destination_port = tcp_header[1]
    sequence = tcp_header[2]
    acknowledgement = tcp_header[3]
    thl = tcp_header[4] #temporary variable for getting tcp_header_lenght
    tcp_header_lenght = thl >> 4

    header_size = ip_header_length + tcp_header_lenght * 4 #get data from whole packet
    data_size = len(packet) - header_size
    data = packet[header_size:]

    protocol=re.search(r'^Via: (.*?)/', data, re.MULTILINE)
    try:
        via_ip = re.search('Via: (.*) (.*):([0-9]+)', data, re.MULTILINE).group(2)
    except AttributeError:
        via_ip = ""
    if protocol:
        packet={
            'source_ip': str(source_address),
            'source_port': str(source_port),
            'destination_ip': str(destination_address),
            'destination_port': str(destination_port),
            'Via': via_ip,
            'version': str(version),
            'ihl': str(ihl),
            'ttl': str(ttl),
            'protocol': str(protocol),
            'sequence': str(sequence),
            'acknowledgement': str(acknowledgement),
            'tcp_header_lenght': str(tcp_header_lenght),
            'data': str(data)
        }
        
        if protocol.group(1).strip() == 'SIP':
            #print sip_transmission.package[sip_transmission.package_number]['data']
            #sip_transmission.analyse(packet)
            return sip_transmission.analyse(packet)
        else:
            print 'protocol not reckognized' + str(protocol.group())

def getData(socket):
    global packet
    packet = None
    while not packet:
        socket.setblocking(0)
        try:
            packet = socket.recvfrom(66746)
        except Exception:
            pass
    return packet

def closeConnection():
    """ """
    packet = 1

if __name__ == "__main__":
    while(1):
        sniff_results=sniff(sys.argv[1])
        if sniff_results:
            print sniff_results['graph']