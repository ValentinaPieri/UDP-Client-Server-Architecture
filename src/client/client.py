import socket as sk
import client_lib

server_address = ('localhost', 10000)

try:
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    print("Client socket creation..")
except sock.error:
    print("Failed to create socket.")
    exit(1)

while True:
    text=input("\nWhat do you want to do? \n- get 'file_name' \n-put 'file_name' \n-list \n: ")
    
    print("")

    if text.startswith("get"):
        client_lib.get_client(text, sock, server_address)
    elif text.startswith("put"):
        client_lib.put_client(text, sock, server_address)
    elif text == "list":
        client_lib.list_client(sock,server_address)
    elif text == "exit":
        sock.sendto(text.encode(), server_address)
        sock.close()
        exit()
    else:
        print('Wrong input\nPlease try again\n')