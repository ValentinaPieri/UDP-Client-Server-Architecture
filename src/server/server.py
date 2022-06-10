import socket as sk
import server_lib
import threading


def command_thread(command, sock, client_address):
    if command.startswith("get"):
        server_lib.get_server(command, sock, client_address)
    elif command.startswith("put"):
        server_lib.put_server(command, sock)
    elif command == "list":
        server_lib.list_server(sock, client_address)
    else:
        print("Invalid command")


try:
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    server_address = ('localhost', 10000)
    print('\n\r starting up on %s port %s' % server_address)
    sock.bind(server_address)
except sock.error:
    print("Failed to create socket.")
    exit(1)

while True:
    print('\n\r waiting to receive message..')
    data, client_address = sock.recvfrom(4096)
    command = data.decode()
    print('received %s bytes from %s' % (len(data), client_address))
    print(command)
    if command == "exit":
        sock.close()
        exit()

    thread = threading.Thread(target=command_thread,
                              args=(command, sock, client_address))
    thread.start()
    thread.join()
