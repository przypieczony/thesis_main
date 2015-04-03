import socket, sys
from struct import *
import re
from math import fabs
import select
import random

class transmission():
    def __init__(self, ip_dict):
        self.package_number=-1
        self.first_in_transmission=0
        self.ips=[]
        self.ip_list=''
        self.ip_dict=ip_dict
        self.package=[]
        self.graph=''



    def randomLoopback(self):
        """Return ip address 127.{}.{}.{} """
        return "127.{}.{}.{}".format(random.randint(1,255), \
                random.randint(1,255), random.randint(1,255))

    def analyse(self, packet):
        self.package_number+=1
        self.package.append(packet)
        graph=''
        cseq=re.search(r'^CSeq: ([0-9]*) (.*)', self.package[self.package_number]['data'], re.MULTILINE)
        source_ip=self.package[self.package_number]['source_ip']
        source_port=self.package[self.package_number]['source_port']
        destination_ip=self.package[self.package_number]['destination_ip']
        destination_port=self.package[self.package_number]['destination_port']

        if cseq:
            #for key, value in self.ip_dict.items():
            #    self.ip_dict[key]=self.randomLoopback()

            full_length=len(self.ip_dict["sourceAddress"])+len(self.ip_dict["proxyOneAddress"])+len(self.ip_dict["proxyTwoAddress"])+len(self.ip_dict["destAddress"])
            max_length = 120
            spacer = (max_length - full_length)/2
            #graph = "{}{}{}{}\n".format(self.ip_dict["sourceAddress"]+spacer*" ", self.ip_dict["proxyOneAddress"]+spacer*" ", self.ip_dict["proxyTwoAddress"]+spacer*" ", self.ip_dict["destAddress"])
            graph = "{}{}{}{}\n".format(self.ip_dict["sourceAddress"].ljust(26), self.ip_dict["proxyOneAddress"].ljust(26), self.ip_dict["proxyTwoAddress"].ljust(15), self.ip_dict["destAddress"].rjust(27))
            #test_ip_addr = "255.255.255.255"
            #graph = "{}{}{}{}\n".format(test_ip_addr, test_ip_addr.center(32), test_ip_addr.center(32), test_ip_addr)
            request=str(cseq.group(1).strip() + ' ' + cseq.group(2).strip())
            source_ip_id=self.ip_dict.values().index(source_ip)
            destination_ip_id=self.ip_dict.values().index(destination_ip)
            if source_ip_id < destination_ip_id:
                delimeter_first = '|'
                delimeter_second = '>|'
            elif source_ip_id == destination_ip_id: #when destination and source ip are the same print confusing message
                delimeter_first = '?'
                delimeter_second = '?'
            else:
                delimeter_first = '|<'
                delimeter_second = '|'
            distance=int(fabs(int(destination_ip_id-source_ip_id)))
            if source_ip == self.ip_dict["sourceAddress"]:
                graph+=delimeter_first + request.center(16*distance,'-') + delimeter_second + '\n'
            elif source_ip == self.ip_dict["destAddress"]:
                graph+=6*""+ delimeter_first + request.center(16*distance,'-') + delimeter_second + '\n'
            else:
                graph+=delimeter_first + request.center(16*distance,'-') + delimeter_second + '\n'
            message=str(self.package_number).center(8,'-')+'\n'+str(self.package[self.package_number]['data'])
            return {'graph':graph, 'message': message}
            
def sniff(transmission_protocol, ip_dict):
    global sip_transmission
    try:
        sip_transmission
    except NameError:
        sip_transmission=transmission(ip_dict)
    transmission_protocols={'UDP': socket.IPPROTO_UDP, 'TCP': socket.IPPROTO_TCP} #dictionary for transport protocol selection
    if transmission_protocol not in transmission_protocols.keys():
        sys.exit()
    try: #open a socket
        sniff_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, transmission_protocols[transmission_protocol])
    except socket.error, msg:
        print 'Socket could not be created. Error code: ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    packet = sniff_socket.recvfrom(66746) #get a packet from socket
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
    if protocol:
        packet={
            'source_ip': str(source_address),
            'source_port': str(source_port),
            'destination_ip': str(destination_address),
            'destination_port': str(destination_port),
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

if __name__ == "__main__":
    while(1):
        sniff_results=sniff(sys.argv[1])
        if sniff_results:
            print sniff_results['graph']