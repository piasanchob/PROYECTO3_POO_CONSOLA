import keyboard
import msvcrt as m
import win32api
import time
import socket
from client import *
from server import *



class Controlador():

    def see_key(self):
        while True:
        
            a = win32api.GetKeyState(0x41)
            if a < 0:
                print("ACTION")
                
                
                Cl.send_msg("ACTION")
            up = win32api.GetKeyState(0x26)
            if up < 0:
                print("UP")
                Cl.send_msg("UP")
            down = win32api.GetKeyState(0x28)
            if down < 0:
                print("DOWN")
                Cl.send_msg("DOWN")
            left = win32api.GetKeyState(0x25)
            if left < 0:
                print("LEFT")
                Cl.send_msg("LEFT")
            right = win32api.GetKeyState(0x27)
            if right < 0:
                print("RIGHT")
                Cl.send_msg("RIGHT")
            time.sleep(0.1)
Servidor.start()
control = Controlador()
print("presione tecla de dirección o presione A para acción")
control.see_key()

