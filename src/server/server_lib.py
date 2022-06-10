import os

sizeBuffer = 4096

def get_server(command, sock, client_address):
    filename = command.split(' ')[1]
    if os.path.exists(filename):
        sock.sendto("ok".encode(), client_address)
        f = open(filename, 'rb')
        while True:
            data = f.read(sizeBuffer)
            if not data:
                sock.sendto(b"EOF", client_address)
                break
            sock.sendto(data, client_address)
        f.close()
        print("Successfully sent file from Server")
    else:
        sock.sendto("error".encode(), client_address)


def put_server(command, sock):
    filename = command.split(' ')[1]
    f = open(filename, 'wb')
    while True:
        data = sock.recvfrom(sizeBuffer)[0]
        if data == b"EOF":
            break
        f.write(data)
    f.close()
    print("Successfully received file from Client")


def list_server(sock, client_address):
    filelist = os.listdir(".")
    filelist.remove("server.py")
    filelist.remove("server_lib.py")
    filelist.remove("__pycache__")
    file_num = len(filelist)
    sock.sendto(str(file_num).encode(), client_address)
    for file in filelist:
        sock.sendto(file.encode(), client_address)
    print("\nSuccessfully sent list from Server")
