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

def ListServer(sock,client_address):
    path = os.getcwd()
    F = os.listdir(path)
    filelist = []
    for file in F:
        filelist.append(file)
    filelistStr = str(filelist)
    filelistEn = filelistStr.encode('utf-8')
    sock.sendto(filelistEn, client_address)
    print("List sent from Server")