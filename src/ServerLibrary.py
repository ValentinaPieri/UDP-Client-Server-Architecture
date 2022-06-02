import os
import sys

sizeBuffer = 4096

def ServerGet(filename,sock):
    filename, addr = sock.recvfrom(sizeBuffer)
    filename = filename.decode()
    f = open(filename,'w')

    data, addr = sock.recvfrom(sizeBuffer)
    f.write(data.decode())

    print("Received a file from "+str(addr)+": "+filename)
    f.close()

    reply = 'File has been received!'
    sock.sendto(reply.encode(), addr)
