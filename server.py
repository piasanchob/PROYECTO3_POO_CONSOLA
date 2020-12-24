import socket
import threading


class Socket():
    def __init__(self,HEADER,PORT,SERVER,ADDR,FORMAT,DISCONNECT_MSG,server1):
        self.HEADER = HEADER
        self.PORT = PORT
        self.SERVER = SERVER
        self.ADDR = ADDR
        self.FORMAT = FORMAT
        self.DISCONNECT_MSG = DISCONNECT_MSG
        self.server1 = server1


    def handle_client(self,conn,addr):
        print(f"[NEW CONNECTION] {addr} connected")
        connected = True
        while connected:
            msg_len = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_len:

                msg_len = int(msg_len)
                global msg
                msg = conn.recv(msg_len).decode(self.FORMAT)
                print(f"message is {msg}")
                
                if msg == self.DISCONNECT_MSG:
                    connected = False
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(self.FORMAT))
        conn.close()

    def start(self):
        self.server1.bind(self.ADDR)
        self.server1.listen()
        print(f"[SERVER LISTENING ON {self.SERVER}]")
        while True:
            self.conn, self.addr = self.server1.accept()
            thread = threading.Thread(target=self.handle_client, args = (self.conn,self.addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS],{threading.activeCount() - 1}")
    print("starting...")
    #start()

    

Servidor = Socket(64,5050,socket.gethostbyname(socket.gethostname()),(socket.gethostbyname(socket.gethostname()),5050),'utf-8',"!DISCONNECT",socket.socket(socket.AF_INET, socket.SOCK_STREAM))

Servidor.start()