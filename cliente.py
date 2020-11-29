import socket
#import pickle

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MSG = "DISCONNECT"
ADDR = (SERVER, PORT)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)

def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    cliente.send(send_len)
    cliente.send(message)
    print(cliente.recv(1000).decode(FORMAT))


send_msg("Hello world")
send_msg("Hello Pia")
send_msg("Hello Manuel")
send_msg(DISCONNECT_MSG)
