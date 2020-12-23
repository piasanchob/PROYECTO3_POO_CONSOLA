import socket


class Cliente():
    def __init__(self,HEADER,PORT,SERVER,ADDR,FORMAT,DISCONNECT_MSG,client):
        self.HEADER = HEADER
        self.PORT = PORT
        self.SERVER = SERVER
        self.ADDR = ADDR
        self.FORMAT = FORMAT
        self.DISCONNECT_MSG = DISCONNECT_MSG
        self.client = client


    def send_msg(self,msg):
        self.client.connect(self.ADDR)
        message = msg.encode(self.FORMAT)
        msg_len = len(message)
        send_len = str(msg_len).encode(self.FORMAT)
        send_len += b' ' * (self.HEADER - len(send_len))
        #self.client.connect(self.ADDR)
        self.client.send(send_len)
        self.client.send(message)
        print(self.client.recv(1000).decode(self.FORMAT))
        



Cl = Cliente(64,5050,socket.gethostbyname(socket.gethostname()),(socket.gethostbyname(socket.gethostname()),5050),'utf-8',"!DISCONNECT",socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((socket.gethostbyname(socket.gethostname()),5050)))

