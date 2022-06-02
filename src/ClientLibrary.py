import os
import sys

sizeBuffer = 4096

def client_send(message, server_address, sock):
    print('sending message..')
    sock.sendto(message.encode(), server_address)

def client_get(message,sock):
    print('waiting to receive..')
    try:
        data = sock.recvfrom(sizeBuffer)[0]
        if "Error" in data(sock).decode():
            print("File doesn't exist")
            return
        f = open(message, "w")

    except ConnectionResetError:
        print("Error. Port numbers not matching. Exiting. Next time enter same port numbers.")
        sys.exit()
    except:
        print("Timeout or some other error")
        sys.exit()
        
    print('received message "%s"' % data.decode('utf8'))
    f.write(data.decode())

def list_client(sock,server_address):
    sock.sendto("list".encode(), server_address)

    num_files = int(sock.recvfrom(sizeBuffer)[0].decode())
    for i in range(num_files):
        data = sock.recvfrom(sizeBuffer)[0]
        print(data.decode())