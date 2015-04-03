import socket
import sys
import optparse
import select
import time
import random

def open_sock(ip, port, options):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		sock.setblocking(0)
	except Exception, e:
		sys.stderr.write("ERROR: cannot create socket. %s\n" % e)
		sys.exit(-1)
	try:
		sock.seckopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.seckopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
	except AttributeError:
		pass
	
	if options.source_port:
		sock.bind((ip, port))
	sock.settimeout(options.wait)
	return sock

if __name__ == "__main__":
	opt = optparse.OptionParser(usage="")
	opt.add_option('-i', dest='wait', type='float', default=1,
                    		help='Specify packet send interval time in seconds')

	opt.add_option('-S', dest='source_ip', type='string', default="0.0.0.0",
                           help='Specify ip address to bind for sending and receiving UDP datagrams')

	opt.add_option('-P', dest='source_port', type='int', default=5060,
                           help='Specify the port number to use as a source port in UDP datagrams')

	opt.add_option('-d', dest='dest_ip', type='string', default=None,
                           help='*mandatory* Specify the destination ip address')

	opt.add_option('-p', dest='dest_port', type='int', default=5060,
                           help='*mandatory* Specify the destination port number')

	options, args = opt.parse_args(sys.argv[1:])

	random_loopback = "127.{}.{}.{}".format(random.randint(1,255), random.randint(1,255), random.randint(1,255))
	sending_sock = open_sock(random_loopback, options.source_port, options)
	print "sending socket got ip: {} and port: {}".format(options.source_ip, options.source_port)
	receiving_sock = open_sock("127.0.0.1", options.dest_port, options)
	print "receiving socket got ip: {} and port: {}".format(options.dest_ip, options.dest_port)
	


	try:
		print "sending..."
		time.sleep(2)
		sending_sock.sendto("wyslano z sending socket: {} do {}:{}".format(options.source_ip, options.dest_ip, options.dest_port), (options.dest_ip, options.dest_port))
	except Exception, e:
		sys.stderr.write("ERROR: cannot open socket. %s\n" % e)

	read = [receiving_sock]
	inputready,outputready,exceptready = select.select(read,[],[],10)

	buf = receiving_sock.recvfrom(0xffff)
	print "Received to {}:{}, message: |{}|".format(options.dest_ip, options.dest_port, buf)
