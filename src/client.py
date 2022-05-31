from fileinput import filename
import socket as sk
import time
import sys
import ClientLibrary

try:
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    print("Client socket creation..")
    server_address = ('localhost', 10000)
except sock.error:
    print("Failed to create socket.")
    sys.exit(1)

# MessClient = message.encode('utf-8')
#     try:
#         s.sendto(MessClient, (host, server_address))
#     except ConnectionResetError:
#         print(
#             "Error. Port numbers are not matching. Exiting. Next time please enter same port numbers.")
#         sys.exit()
while True:
    fileName=input("File name: ")
    text=input("\nWhat do you want to do with %s? \n- get 'file_name' \n-put 'file_name' \n-list \n: " % fileName)

    try:
        if text == "get":
            ClientLibrary.ClientGet(sock, fileName)
        elif text == "put":
            ClientLibrary.ClientPut(fileName, sock, server_address)
        elif text == "list":
            ClientLibrary.ListClient(sock)
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