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
    if len(data.decode('utf8')) < 30:


def ListClient(sock):
    data = sock.recvfrom(sizeBuffer)
    print(data(sock).decode())