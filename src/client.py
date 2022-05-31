import socket as sk
import time
import ClientLibrary

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
print("Client socket creation..")
server_address = ('localhost', 10000)
#aggiungere se c'è errore
# try:
#     socket.gethostbyname(sys.argv[1])
# except socket.error:
#     print("Invalid host name. Exiting. Next time enter in proper format.")
#     sys.exit()

message=input("\nWhat do you want to do? \n- get 'file_name' \n-put 'file_name' \n-list \n:")

# MessClient = message.encode('utf-8')
#     try:
#         s.sendto(MessClient, (host, server_address))
#     except ConnectionResetError:
#         print(
#             "Error. Port numbers are not matching. Exiting. Next time please enter same port numbers.")
#         sys.exit()

try:
    ClientLibrary.Send()
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    time.sleep(2)
    print('received message "%s"' % data.decode('utf8'))
except Exception as info:
    print(info)
finally:
    print('closing socket')
    sock.close()