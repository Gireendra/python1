#!/usr/bin/python2

import  socket

#  defining UDP socket
data=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  getting ip 
ip="192.168.10.103"
port=8888
#  binding ip & port

while True:
	msg=raw_input("type your message :  ")
	data.sendto(msg,(ip,port))
	print  "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	print  "@@@                        @@"
	print  "@@@                        @@"
	print  "@@@                        @@"
	print  "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	print  data.recvfrom(100)[0]
	print  "____________________________"
	print  "____________________________"
	print  "____________________________"




