import threading
import socket

#Now receive data
class Sniff(threading.Thread):
    """Sniffing tools for capturing messages"""
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print "Sniffig...\n"
        message = None
        while True:
	        sniff_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
	        sniff_socket.bind(('0.0.0.0', 0))
	    	#sniff_socket.settimeout(5)
	    	message = sniff_socket.recvfrom(66666)
	    	print message

thread = Sniff()
thread.start()