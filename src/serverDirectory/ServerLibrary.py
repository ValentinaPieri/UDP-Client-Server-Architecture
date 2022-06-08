import os
import sys

sizeBuffer = 4096

def get_server(filename,sock):
    filename, addr = sock.recvfrom(sizeBuffer)
    filename = filename.decode()
    f = open(filename,'w')

    data, addr = sock.recvfrom(sizeBuffer)
    f.write(data.decode())

    print("Received a file from "+str(addr)+": "+filename)
    f.close()

    reply = 'File has been received!'
    sock.sendto(reply.encode(), addr)

def put_server(filename,sock,server_address):
    if os.path.exists(filename):
        sock.sendto(filename.encode(), server_address)
    
    f = open(filename,'r')
    data = f.read()
    f.close()
    sock.sendto(data.encode(), server_address)
    print("Successfully sent file to Server")

def list_server(sock,client_address):
    path = os.getcwd()
    F = os.listdir(path)
    filelist = []
    for file in F:
        filelist.append(file)
    filelistStr = str(filelist)
    filelistEn = filelistStr.encode('utf-8')
    sock.sendto(filelistEn, client_address)
    print("Successfully sent list from Server")