#! /usr/bin/python 
import socket,sys

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=sys.argv[1]
port = 12345
x.sendto("wanna connect",(ip,port))

def sender():
	response=x.recvfrom(10)
	if response[0]== "ok" :
		while 1:
			command=raw_input("enter your command: ")
			x.sendto(command,(ip,port))
			print "======================="
			commout=x.recvfrom(100)
			print command
			print "after execution:  "
			print commout
	else:
		print "connection refused by server"
sender()
x.close()
	
