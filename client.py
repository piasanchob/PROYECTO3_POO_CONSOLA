import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((socket.gethostbyname(socket.gethostname()),5050))

class Cliente():
    def __init__(self,HEADER,PORT,SERVER,ADDR,FORMAT,DISCONNECT_MSG):
        self.HEADER = HEADER
        self.PORT = PORT
        self.SERVER = SERVER
        self.ADDR = ADDR
        self.FORMAT = FORMAT
        self.DISCONNECT_MSG = DISCONNECT_MSG
        #self.client = client
        #self.client2 = client2


    def send_msg(self,msg):
        #self.client.connect(self.ADDR)
        message = msg.encode(self.FORMAT)
        msg_len = len(message)
        send_len = str(msg_len).encode(self.FORMAT)
        send_len += b' ' * (self.HEADER - len(send_len))
        #self.client.connect(self.ADDR)
        cliente.send(send_len)
        cliente.send(message)
        print(cliente.recv(1000).decode(self.FORMAT))
        



Cl = Cliente(64,5050,socket.gethostbyname(socket.gethostname()),(socket.gethostbyname(socket.gethostname()),5050),'utf-8',"!DISCONNECT")

