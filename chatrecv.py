#!/usr/bin/python2

import  socket

#  defining UDP socket
data=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  getting ip 
hn=socket.gethostname()
ip=socket.gethostbyname(hn)
port=8888
#  binding ip & port
data.bind((ip,port))

while True:
	x=data.recvfrom(100)
	print  "data from Sender  "+x[0]
	print  "_______________________"
	print  "_______________________"
	msg=raw_input("type your reply :   ")
	data.sendto(msg,x[1])
	print  "########################"
	print  "########################"
	print  "########################"






