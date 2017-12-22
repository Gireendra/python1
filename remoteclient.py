#! /usr/bin/python 
import socket,sys

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=sys.argv[1]
port = 12345
x.sendto("wanna connect",(ip,port))
def sendreceive():
	login_req=x.recvfrom(100)
        print login_req[0]
	usr=x.recvfrom(100)
	print usr[0]
        username=raw_input()
        x.sendto(username,(ip,port))
        passwordprompt=x.recvfrom(100)
        print passwordprompt[0]
        password=raw_input()
        x.sendto(password,(ip,port))

def logic():
	while 1:
        	command=raw_input("enter your command: ")
                x.sendto(command,(ip,port))
                print "======================="
                commout=x.recvfrom(100)
                print command
                print "after execution:  "
                print commout[0]
                

def sender():
	response=x.recvfrom(10)
	if response[0]== "ok" :
		x.sendto("let's start",(ip,port))
		sendreceive()
		confirmation=x.recvfrom(40)
                print confirmation[0]
		if confirmation[0]== "start" :
			logic()
		else:
			sendreceive()		

		
				
			
	else:
		print "connection refused by server"
sender()
x.close()
	
