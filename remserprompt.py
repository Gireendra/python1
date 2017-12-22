import socket,commands

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=socket.gethostbyname(socket.gethostname())
port = 12345
print ip
x.bind((ip,port))
request= x.recvfrom(20)
print request
choice=raw_input("enter your choice: type yes to connect and type no to refuse the connection:  ")
def receive():
	if choice=="yes":
		x.sendto("ok",(request[1]))
		while 1:
			msg=x.recvfrom(100)
			print msg[0]
			status,comm=commands.getstatusoutput(msg[0])
			if status == 0:
				print "output of command: ",comm
				x.sendto(comm,(msg[1]))
			else:
				print msg[0] 
  				x.sendto("sorry,we weren't able to do that",(msg[1]))
	else:
		x.sendto("not interested",(request[1]))
receive()
x.close()
