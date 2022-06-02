import socket as sk
import sys
import ClientLibrary

try:
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    print("Client socket creation..")
    server_address = ('localhost', 10000)
except sock.error:
    print("Failed to create socket.")
    sys.exit()

# MessClient = message.encode('utf-8')
#     try:
#         s.sendto(MessClient, (host, server_address))
#     except ConnectionResetError:
#         print(
#             "Error. Port numbers are not matching. Exiting. Next time please enter same port numbers.")
#         sys.exit()
while True:
    text=input("\nWhat do you want to do? \n- get 'file_name' \n-put 'file_name' \n-list \n: ")

    try:
        if text.split([0]) == "get":
            ClientLibrary.ClientGet(sock, text.split([1]))
        elif text.split([0]) == "put":
            ClientLibrary.ClientPut(text.split([1]), sock, server_address)
        elif text.split([0]) == "list":
            ClientLibrary.ListClient(sock)
        elif text.split([0]) == "exit":
            sock.close()
            sys.exit()
    finally:
        print('closing socket')
        sock.close()

# try:
#     ClientLibrary.Send()
#     print('waiting to receive')
#     data, server = sock.recvfrom(4096)
#     time.sleep(2)
#     print('received message "%s"' % data.decode('utf8'))
# except Exception as info:
#     print(info)
# finally:
#     print('closing socket')
#     sock.close()