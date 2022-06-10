import os

sizeBuffer = 4096

def get_client(command,sock,server_address):
    sock.sendto(command.encode(), server_address)
    data = sock.recvfrom(sizeBuffer)[0]
    if data.decode() == "ok":
        filename = command.split(' ')[1]
        f = open(filename,'wb')
        while True:
            data = sock.recvfrom(sizeBuffer)[0]
            if data == b"EOF":
                break
            f.write(data)
        print("Successfully received file from Server")
        f.close()
    else:
        print("File not Found")

def put_client(command, sock, server_address):
    filename = command.split(' ')[1]
    if os.path.exists(filename):
        sock.sendto(command.encode(), server_address)
        f = open(filename,'rb')
        while True:
            data = f.read(sizeBuffer)
            if not data:
                sock.sendto(b"EOF", server_address)
                break
            sock.sendto(data, server_address)
        f.close()
        print("Successfully sent file from Client")
    else:
        print("File not Found")

def list_client(sock,server_address):
    sock.sendto("list".encode(), server_address)
    num_files = int(sock.recvfrom(sizeBuffer)[0].decode())
    for i in range(num_files):
        data = sock.recvfrom(sizeBuffer)[0]
        print(data.decode())
    print("\nSuccessfully received list from Server")