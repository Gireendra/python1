import socket,commands

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=socket.gethostbyname(socket.gethostname())
port = 12345
print ip
x.bind((ip,port))
request= x.recvfrom(20)
print request[0]
choice=raw_input("enter your choice: type yes to connect and type no to refuse the connection:  ")

def logic():
	 x.sendto("start",(request[1]))
         while 1:
		msg=x.recvfrom(100)
                print msg[0]
                status,comm=commands.getstatusoutput(msg[0])
                if status == 0:
                	print "output of command: ",comm
                        x.sendto(comm,(msg[1]))
                else:   
			print "didn't work"  
                        x.sendto("sorry,we weren't able to do that",(msg[1]))
def sendreceive():
	x.sendto("wrong username and password combination",(request[1]))
        x.sendto("enter username(server)",(request[1]))
        username=x.recvfrom(100)
        x.sendto("enter the password(server)",(request[1]))
        password=x.recvfrom(100)
	#print username[0]
        #print password[0]
	print type(username[0])
	return {username,password}
def receive():
	if choice=="yes":
		x.sendto("ok",(request[1]))
		h=x.recvfrom(20)
		print "h is:",h[0]
		
		usernames, passwords=sendreceive()
		print usernames[0],passwords[0]
		
		if usernames[0] == "root" and passwords[0] == "redhat" :
			logic()
				
		else:
			x.sendto("try again",(request[1]))
				
				
			if usernames=="root" and passwords=="redhat" :
				logic()
				
			else:
				sendreceive()
					
				
	
	else:
		x.sendto("not interested",(request[1]))
receive()
x.close()
