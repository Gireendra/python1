#! /usr/bin/python 
import socket,sys

def sender():
	x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	ip=sys.argv[1]
	port = 12345
	while 1:
		command=raw_input("enter your command: ")
		x.sendto(command,(ip,port))
		print "======================="
		commout=x.recvfrom(100)
		print command
		print "after execution:  "
		print commout
sender()
s.close()
	
