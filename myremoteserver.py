import socket,commands

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=socket.gethostbyname(socket.gethostname())
port = 12345
print ip
x.bind((ip,port))
def receive():
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
receive()
x.close()
