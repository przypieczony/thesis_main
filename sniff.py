import socket, sys
from struct import *
import re
from math import fabs
import select
import random
import threading

class transmission():
    def __init__(self, ip_list):
        self.package_number=0
        self.first_in_transmission=0
        self.ips=[]
        self.ip_list = ip_list
        self.package=[]
        self.graph=''

    def analyse(self, packet):
        self.package.append(packet)
        graph=''
        via_ip = self.package[self.package_number]['Via']
        source_ip=self.package[self.package_number]['source_ip']
        source_port=self.package[self.package_number]['source_port']
        destination_ip=self.package[self.package_number]['destination_ip']
        destination_port=self.package[self.package_number]['destination_port']
        sip_method = self.findSipMethod(packet)
        if sip_method:
            return self.printGraph(source_ip, destination_ip, sip_method)

    def findSipMethod(self, packet):
        """ """
        methods = (
        'ACK', 'BYE', 'CANCEL', 'INFO', 'INVITE', 'MESSAGE', 'NOTIFY',
        'OPTIONS', 'PRACK', 'PUBLISH', 'REFER', 'REGISTER', 'SUBSCRIBE',
        'UPDATE', re.compile('[1-6][0-9][0-9] ')
        )
        for method in methods:
            method_line = self.package[self.package_number]['data'].split('\n')[0]
            sip_method = re.search(method, method_line)
            if sip_method:
                sip_method = sip_method.group()
                break
        else:
            sip_method = re.search(r'^CSeq: [0-9]* (.*)', \
            self.package[self.package_number]['data'], re.MULTILINE) #terrible hack, sorry about that
            sip_method = sip_method.group(1)
        return sip_method

    def printGraph(self, source_ip, destination_ip, sip_method):
        """Return formatted SIP graph flow and message"""
        for ip in self.ip_list:
            if ip not in self.ips:
                self.ips.append(ip)
        request=str(str(self.package_number) + ' ' + sip_method.strip())

        if source_ip == self.ips[0]:
            delimeter_first_pos = 0
        elif source_ip == self.ips[1]:
            delimeter_first_pos = 33
        elif source_ip == self.ips[2]:
            delimeter_first_pos = 65
        elif source_ip == self.ips[3]:
            delimeter_first_pos = 94

        if destination_ip == self.ips[0]:
            delimeter_second_pos = 0
        elif destination_ip == self.ips[1]:
            delimeter_second_pos = 33
        elif destination_ip == self.ips[2]:
            delimeter_second_pos = 65
        elif destination_ip == self.ips[3]:
            delimeter_second_pos = 94

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
        self.package_number+=1
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
    except socket.error, msg:
        raise Exception, 'Socket could not be created. Error code: ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    packet = _getData(sniff_socket) #get a packet from socket
    packet = packet[0]
    ip_header_packed = packet[0:20] #first 20 characters = ip header
    try:
        ip_header = unpack('!BBHHHBBH4s4s', ip_header_packed) #unpack ip header
    except:
        raise Exception, 'Unpacking error'
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
        raise Exception, 'Unpacking error'
        return None
    
    source_port = tcp_header[0]
    destination_port = tcp_header[1]
    sequence = tcp_header[2]
    acknowledgement = tcp_header[3]
    thl = tcp_header[4] #temporary variable for getting tcp_header_lenght
    tcp_header_lenght = thl >> 4

    header_size = ip_header_length + tcp_header_lenght #get data from whole packet
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
            return sip_transmission.analyse(packet)
        else:
            error = 'Protocol is not recognized, probably Via header is missing in template'
        raise Exception, error

def _getData(socket):
    packet = None
    socket.bind(('0.0.0.0', 0))
    while not packet:
        socket.setblocking(0)
        try:
            packet = socket.recvfrom(66746)
        except Exception:
            pass
    return packet

def killTransmission():
    """ """
    global sip_transmission
    del sip_transmission

if __name__ == "__main__":
    while(1):
        sniff_results=sniff(sys.argv[1])
        if sniff_results:
            print sniff_results['graph']