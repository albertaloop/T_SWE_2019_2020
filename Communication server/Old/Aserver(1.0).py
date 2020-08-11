import socket
import numpy as np

clientinfo = np.array([])

ip = "127.0.0.1"
port = 5005;

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind((ip,port))
#s.listen(5) doesnot work for dgram

clients = []
addrC = []

while True:

    clientI, addr = s.recvfrom(1024) 
    print("received message: %s" % clientI)

    clients.append(clientI.decode("utf-8"))
    addrC.append(addr)

    clientO, addr = s.recvfrom(1024) 
    print("received message: %s" % clientO)

    data, addr = s.recvfrom(1024) 
    print("received message: %s" % data)
    
    print(addr)
    datad = data.decode("utf-8")             
    print(datad)

    print("the person the info is being sent to is")
    print(clients)
    print("the address is")
    print(addrC)
    print(addrC[0][0])

    s.sendto(bytes("asdas", "utf-8"),addr)

    for x in range (len(clients)):
        if clients[x] == clientO.decode('utf-8'):
            print(x)
            print(addrC[0])
            s.sendto(data, addrC[x])

###############################################################
#       This dictates who is using the server
###############################################################
        # what i need is to create a array that stores user information
        # then while loop what needs to be sent to whom 
        # then continuosly send information between user 1 and user 2
