import socket

#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
#    sock.connect(("127.0.0.1", 5002))

 #   sock.send(b"hi from client")
  #  print(sock.recvfrom(8192))
    
# attempt to make a program to send information over UDP
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
message = b"hello world"

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #SOCK_DGRAM signifies UDP
sock.sendto(message,(UDP_IP, UDP_PORT))
