import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #SOCK_DGRAM signifies UDP

###############################################################
#		This sends notifies the server what client is operating, this is client 2
###############################################################

clientI = bytes("c2", "utf-8")
s.sendto(clientI,(UDP_IP, UDP_PORT))

clientO = bytes("c1", "utf-8")
s.sendto(clientO,(UDP_IP, UDP_PORT))

###############################################################
#		This sends the server information
###############################################################
myinfor = "515"
data = bytes(myinfor, "utf-8")

s.sendto(data,(UDP_IP, UDP_PORT))

while True:
	msg = s.recvfrom(2048)
	print(f"the information recieved is{ msg}")




