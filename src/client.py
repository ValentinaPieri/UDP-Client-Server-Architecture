import socket as sk
import time

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
print("Client socket creation..")
server_address = ('localhsot', 10000)
#aggiungere se c'è errore
message=input("\nWhat do you want to do? \n- get 'file_name' \n-put 'file_name' \n-list \n-exit \n:")

try:
    print('sending message..')
    time.sleep(2)
    sent = sock.sendto(message.encode(), server_address)

    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    time.sleep(2)
    print('received message "%s"' % data.decode('utf8'))
except Exception as info:
    print(info)
finally:
    print('closing socket')
    sock.close()