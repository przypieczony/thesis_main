#Socket client example in python
 
import socket   #for sockets
import sys  #for exit



host = '127.0.0.1';
port = 18951;

#create an INET, STREAMing socket
try:
    sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sending_socket.setblocking(0)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
try:
    sending_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sending_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
except AttributeError, e:
    print "cos sie wydarzylo"
print 'Socket Created'
 
#Connect to remote server
sending_socket.bind((host, port))
print 'Socket Connected to ' + host
 
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"


try :
    #Set the whole string
    i = 0
    sending_socket.sendto(message, ('127.165.116.16', 64514))
except socket.error, e:
    #Send failed
    print 'Send failed, ',e
    sys.exit()

 

