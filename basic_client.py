#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:37:24 2020

@author: austinfedoretz
"""


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM is TCP
s.connect(("0.0.0.0", 5005)) # internal machine

full_msg = "" # empty string for recieved message

while True: # makes it so that if data is large it gets coninually loaded "is a buffer"
    msg = s.recv(8) #the size of the chuncks of data being sent are 1024    
    if len(msg) <= 0: # if thier is no more data being sent break the loop
        break
    full_msg += msg.decode("utf-8")
    
print(full_msg)