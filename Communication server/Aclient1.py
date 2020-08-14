import socket
import time
import numpy as np

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #SOCK_DGRAM signifies UDP

###############################################################
#        This sends the server information, This is client 1
###############################################################

clientI = bytes("c1", "utf-8")				# input client
s.sendto(clientI,(UDP_IP, UDP_PORT))

clientO = bytes("c2", "utf-8")				# output client
s.sendto(clientO,(UDP_IP, UDP_PORT))

myinfor = "456"								# data being sent out
data = bytes(myinfor, "utf-8")
s.sendto(data,(UDP_IP, UDP_PORT))

###############################################################
#       This collects the informations
###############################################################

while True:

    msg, addr = s.recvfrom(2048)
    msg = msg.decode("utf-8")
    print(f"the information recieved is{ msg}")

    check = "data"
    if msg == check: # this tells the server the next message will be actual data

        info, addr = s.recvfrom(2048)
        info = int(info.decode("utf-8"))

        print(f"i recieved the information i needed")
        print(info)
