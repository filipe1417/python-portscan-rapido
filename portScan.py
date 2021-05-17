#!/usr/bin/python3

import sys, socket 

host = socket.gethostbyname(sys.argv[1])
portas = sys.argv[2]

def portScan(host,porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((host,int(porta))) == 0:
        print("Porta " + porta + " aberta")

for p in portas.split(","):
    portScan(host,p)
