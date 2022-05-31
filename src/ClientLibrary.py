import os
import sys

sizeBuffer = 4096

def Send(message, server_address, sock):
    print('sending message..')
    sock.sendto(message.encode(), server_address)



