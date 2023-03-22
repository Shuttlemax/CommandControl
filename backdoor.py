import socket
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

HOST = '' 
BASE_PORT = 1234 
PUB_KEY = ''
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def bind_socket(port = BASE_PORT, host = HOST):
    while port < 9999:
        try:
            s.bind((host, port))
            return port
        except socket.error as msg:
            print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            port+=1
    return -1

def connect():
    s.listen()
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    return conn


def authenticate(conn):
    signature = conn.recv(4096)
    message = conn.recv(4096)
    success = True
    with open("pubkey.pem", "rb") as key_file:
        pub = serialization.load_pem_pub_key(
            key_file.read(),
            password=None,
        )

        try:
            # verify signed message
            pub.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
        except Exception as e:
            # verification failed
            success = False
    return success




while True:
    ok = bind_socket()
    if ok:
        print('Socket bind complete')
    conn = connect()
    ok = authenticate(conn)
    if !ok:
        # close connection
        print('Authentication failed.')
    else:
        conn.send(b'success')

