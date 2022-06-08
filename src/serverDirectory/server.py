import socket as sk
import ServerLibrary
import time
import sys

try:
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    server_address = ('localhost',10000)
    print('\n\r starting up on %s port %s' % server_address)
    sock.bind(server_address)
except sock.error:
    print("Failed to create socket.")
    sys.exit(1)

while True:

    print('\n\r waiting to receive message..')
    data, client_address = sock.recvfrom(4096)
    command = data.decode()
    print('received %s bytes from %s' % (len(data), client_address))
    print(command)

    if command.startswith("get"):
        ServerLibrary.get_server(sock, command)
    elif command.startswith("put"):
        ServerLibrary.put_server(command, sock, server_address)
    elif command.startswith == "list":
        ServerLibrary.list_server(sock,server_address)
    elif command.startswith == "exit":
        sock.close()
        sys.exit()
    else:
        print("Invalid command")
    
    if data:
        data1='Programmazione di Reti'
        time.sleep(2)
        sent = sock.sendto(data1.encode(), client_address)
        print('sent %s bytes back to %s' % (sent,client_address))
 
