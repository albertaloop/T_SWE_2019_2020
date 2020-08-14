###############################################################
#       This program allows a user to send direct information to specific programs
# 		Allowing for properites in specific programs to be changed
#		This is Client 0
#		Aclient1 is c1 and Aclient2 is c2
###############################################################

import socket
import time
import numpy as np

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #SOCK_DGRAM signifies UDP

###############################################################
#        This sends the server information
###############################################################

print("Hello i am the user interface for the server\n")

clientI = bytes("c0", "utf-8")				# input client
s.sendto(clientI,(UDP_IP, UDP_PORT))

while True:

	print("please enter what client you would like to write to:\n")
	clientO = input("-------------")
	clientO = bytes(clientO, "utf-8")				# output client
	s.sendto(clientO,(UDP_IP, UDP_PORT))

	print("now enter in the information you would like to send to that client\n")
	data = input("______________")								# data being sent out
	data = bytes(myinfor, "utf-8")
	s.sendto(data,(UDP_IP, UDP_PORT))
