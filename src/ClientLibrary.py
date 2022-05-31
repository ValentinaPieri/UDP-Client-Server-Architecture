from distutils import filelist
import os
import sys

sizeBuffer = 4096

def SendClient(message, server_address, sock):
    print('sending message..')
    sock.sendto(message.encode(), server_address)

def ClientGet(message,sock):
    print('waiting to receive..')
    try:
        data, server = sock.recvfrom(sizeBuffer)
        if "Error" in data(sock).decode():
            print("File doesn't exist")
            return
        f = open((message.slipt())[1], "w")

    except ConnectionResetError:
        print("Error. Port numbers not matching. Exiting. Next time enter same port numbers.")
        sys.exit()
    except:
        print("Timeout or some other error")
        sys.exit()
        
    print('received message "%s"' % data.decode('utf8'))

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

def ListClient(sock):
    data = sock.recvfrom(sizeBuffer)
    print(data(sock).decode())

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