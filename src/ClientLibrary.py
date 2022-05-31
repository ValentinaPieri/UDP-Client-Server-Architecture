import os
import sys

sizeBuffer = 4096

def Send(message, server_address, sock):
    print('sending message..')
    sock.sendto(message.encode(), server_address)

def Get(sock):
    print('waiting to receive..')
    data, server = sock.recvfrom(sizeBuffer)
    print('received message "%s"' % data.decode('utf8'))

