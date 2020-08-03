#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:36:24 2020

@author: austinfedoretz
"""

#server tutorial

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM is TCP
s.bind(("0.0.0.0", 5005)) # internal machine
s.listen(5) #has a queue of 5 connections

while True:
    clientsocket, address = s.accept()
    print(f"connenction from {address} has been established")
    clientsocket.send(bytes("Welcome to the server","utf-8"))
    clientsocket.close()