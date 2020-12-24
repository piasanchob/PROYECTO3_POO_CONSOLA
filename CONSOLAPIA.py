import random 
from space_invaders import * 
import keyboard
import msvcrt as m
import win32api
import time
import socket
from tkinter import *
from tkinter import messagebox

class Consola():
    def __init__(self,matriz,gameOver):
        self.matriz = matriz
        self.gameOver = gameOver
    def adelante_pacman(self):
        #adelante pacman
        coin = False
        for l in self.matriz:
                
            if 2 in l:

                coin = True
        if coin == False:
            self.gameOver = True
            print("GAME OVER")
            messagebox.showinfo(message =  "GAME OVER")
        for l in self.matriz:
            for x in l:
                if x == 3:
                    old = l.index(x)
                    new = old + 1
                    if l[new] == 1:
                        print("invalido")
                        break
                    if l[new] == 7:
                        print("GAME OVER")
                        messagebox.showinfo(message =  "GAME OVER")
                        self.gameOver = True
                        break
                    l[new] = x
                    l[old] = 0
                    break
                
        pacman.fantasmas()
        for x in self.matriz:
            print(x)
        gui.tablerogui(ventana,self.matriz)

        #control.see_key()
                    
                    
    def atras_pacman(self):
        #atras pacman
        for l in self.matriz:
            for x in l:
                if x == 3:
                    old = l.index(x)
                    new = old - 1
                    if l[new] == 1:
                        print("invalido")
                        break
                    if l[new] == 7:
                        print("GAME OVER")
                        messagebox.showinfo(message =  "GAME OVER")
                        self.gameOver = True
                        break
                    l[new] = x
                    l[old] = 0
                    break
        pacman.fantasmas()
        for x in self.matriz:
            print(x)
        gui.tablerogui(ventana,self.matriz)



        #control.see_key()
        
    def arriba_pacman(self):
        #arriba pacman
        indices = [0,1,2,3,4,5,6,7,8,9]
        for l in self.matriz:
            for x in self.matriz[indices[0]]:
                if x == 3:
                    c = indices[0]
                    #if self.matriz[c] == l:
                    aux = self.matriz[indices[0]]
                    old = aux.index(x)
                    if self.matriz[c - 1][old] == 7:
                        print("GAME OVER")
                        messagebox.showinfo(message =  "GAME OVER")
                        self.gameOver = True
                        break
                    if self.matriz[c - 1][old] != 1:
                        self.matriz[c - 1][old] = x
                        self.matriz[c][old] = 0
                        break
            indices.pop(0)
        pacman.fantasmas()
        for x in self.matriz:
            print(x)
        gui.tablerogui(ventana,self.matriz)

            
        #control.see_key()
            
    def abajo_pacman(self):
        #abajo pacman
        indices = [0,1,2,3,4,5,6,7,8,9]
        indices.sort(reverse = True)
        for l in self.matriz:
            for x in self.matriz[indices[0]]:
                if x == 3:
                    c = indices[0]
                    aux = self.matriz[indices[0]]
                    old = aux.index(x)
                    if self.matriz[c + 1][old] == 7:
                        print("GAME OVER")
                        messagebox.showinfo(message =  "GAME OVER")
                        self.gameOver = True
                        break
                    if self.matriz[c + 1][old] != 1:
                        self.matriz[c + 1][old] = x
                        self.matriz[c][old] = 0   
                        break
            indices.pop(0)  

        pacman.fantasmas()
        for x in self.matriz:
            print(x)
        gui.tablerogui(ventana,self.matriz)

            
        #control.see_key()

            
    def adelante_fantasma(self):
        #adelante fantasma
        indices = [0,1,2,3,4,5,6,7,8,9]
        huboError = False
        for l in self.matriz:
            for x in self.matriz[indices[0]]:
                if x == 7:
                    old = self.matriz[indices[0]].index(x)
                    new = old + 1
                    if self.matriz[indices[0]][new] == 1:
                        print("invalido")
                        #messagebox.showinfo(message =  "INVALIDO")
                        huboError = True
                        break
                    if self.matriz[indices[0]][new] == 3:
                        print("invalido")
                        self.gameOver = True
                        huboError = True
                        break
                    self.matriz[indices[0]][new] = x
                    self.matriz[indices[0]][old] = 0
                    gui.tablerogui(ventana,self.matriz)

                    break
            
            if huboError:
                break
            indices.pop(0)
                
    def atras_fantasma(self):
        #atras fantasma
        indices = [0,1,2,3,4,5,6,7,8,9]
        huboError = False
        
        for l in self.matriz:
            for x in self.matriz[indices[0]]:
                if x == 7:
                    old = self.matriz[indices[0]].index(x)
                    new = old - 1
                    if self.matriz[indices[0]][new] == 1:
                        print("invalido")
                        #messagebox.showinfo(message =  "INVALIDO")
                        huboError = True
                        break
                    if self.matriz[indices[0]][new] == 3:
                        print("invalido")
                        self.gameOver = True
                        huboError = True
                        break
                    self.matriz[indices[0]][new] = x
                    self.matriz[indices[0]][old] = 0
                    gui.tablerogui(ventana,self.matriz)

                    break
                
            if huboError:
                break
            indices.pop(0)

    def arriba_fantasma(self):
        #arriba fantasma
        indices = [0,1,2,3,4,5,6,7,8,9]
        huboError = False
        
        for l in self.matriz:
            for x in self.matriz[indices[0]]:
                if x == 7:
                    c = indices[0]
                    old = self.matriz[indices[0]].index(x)
                    if self.matriz[c - 1][old] == 1:
                        print("invalido")
                        #messagebox.showinfo(message =  "INVALIDO")
                        huboError = True
                        break
                    if self.matriz[c - 1][old] == 3:
                        print("GAME OVER")
                        self.gameOver = True
                        huboError = True
                        break    
                    self.matriz[indices[0]][old] = 0
                    self.matriz[c - 1][old] = x
                    gui.tablerogui(ventana,self.matriz)

                    break
                        
            if huboError:
                break
            indices.pop(0)

                    
    def abajo_fantasma(self):
        #abajo fantasma
        indices = [0,1,2,3,4,5,6,7,8,9]
        indices.sort(reverse = True)
        huboError = False
        
        for l in self.matriz:
            for x in self.matriz[indices[0]]:
                if x == 7:
                    c = indices[0]
                    old = self.matriz[indices[0]].index(x)
                    if self.matriz[c + 1][old] == 1:
                        print("invalido")
                        #messagebox.showinfo(message =  "INVALIDO")
                        huboError = True
                        break
                    if self.matriz[c+1][old] == 3:
                        self.gameOver = True
                        print("GAME OVER")
                        huboError = True
                        break
                        
                    self.matriz[indices[0]][old] = 0
                    self.matriz[c + 1][old] = x
                    gui.tablerogui(ventana,self.matriz)

                    break
                        
            if huboError:
                break
            indices.pop(0)

            
                    
    def disparar(self):
        for l in self.matriz:
            for x in l:
                if x == 8:
                    c = self.matriz.index(l)
                    if self.matriz[c] == l:
                        old = l.index(x)
                        if self.matriz[c - 1][old] != 1:
                            l[old] = 0
                            l = self.matriz[c - 1]
                            l[old] = x
                            break
                        print("Invalido")
                        break

    
    def fantasmas(self):
        while not self.gameOver:
            r = random.randint(1,4)
            if r == 1:
                pacman.adelante_fantasma()
                break
            elif r == 2:
                pacman.atras_fantasma()
                break
            elif r == 3:
                pacman.arriba_fantasma()
                break
            elif r == 4:
                pacman.abajo_fantasma()
                break


class Controlador():

    def see_key(self,num):
        #print("presione tecla de dirección o presione A para acción")
            if num == 1:
                print("UP")
                action.make_action("UP")
                #Cl.send_msg("UP")
            if num == 2:
                print("DOWN")
                action.make_action("DOWN")
                #Cl.send_msg("DOWN")
            if num == 3:
                print("LEFT")
                action.make_action("LEFT")
                #Cl.send_msg("LEFT")
            if num == 4:
                print("RIGHT")
                action.make_action("RIGHT")
                #Cl.send_msg("RIGHT")
            time.sleep(0.1)
#Servidor.start()

class Pantalla():
    def tablerogui(self,tab,tablero):
    
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                if tablero[i][j] == 0:
                    fontcolor = "black"
                    bgcolor = "black"
                if tablero[i][j] == 3:
                    fontcolor = "yellow"
                    bgcolor = "yellow"
                if tablero[i][j] == 2:
                    fontcolor = "hotpink"
                    bgcolor = "hotpink"
                if tablero[i][j] == 1:
                    fontcolor = "blue"
                    bgcolor = "blue"
                if tablero[i][j] == 7:
                    fontcolor = "red"
                    bgcolor = "red"
                

                b = Button(tab, text=tablero[i][j], fg=fontcolor, bg = bgcolor, width=4, heigh=2, font="Arial")
                b.grid(row=i, column=j)

        
pacman = Consola([
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,1,1,0,1,1,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,2,0,0,0,0,7,0,0,1,1,0,0,1],
[1,0,0,0,0,0,0,0,0,0,2,0,0,1],
[1,0,0,1,0,1,1,1,0,0,0,0,0,1],
[1,2,0,1,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,2,0,0,1,1,1,0,1,1],
[1,3,0,0,0,0,0,0,0,0,0,0,0,1]],False)

spaceinvaders = Consola([
[0,0,0,3,0,3,0,3,0,3,0,0,0,0],
[0,0,0,0,3,0,3,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,5,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1]],False)

#for x in matriz:
    #print(x)

class Action():
    def __init__(self,juego):
        self.juego = juego
    def make_action(self,msg):
        if self.juego == 1:
            if msg == "RIGHT":
                pacman.adelante_pacman()
                pacman.fantasmas()
            if msg == "LEFT":
                pacman.atras_pacman()
            if msg == "UP":
                pacman.arriba_pacman()
            if msg == "DOWN":
                pacman.abajo_pacman()
            if msg == "A":
                print("A")
        

        if self.juego == 2:
            if msg == "RIGHT":
                pass
                #spaceinvaders.adelante_space()
            if msg == "LEFT":
                pass
                #spaceinvaders.atras_space()
            if msg == "A":
                spaceinvaders.disparar()
            

def up_key(event):
    control.see_key(1)
def down_key(event):
    control.see_key(2)
def left_key(event):
    control.see_key(3)
def right_key(event):
    control.see_key(4)

action = Action(1)
num = 1

control = Controlador()

ventana = Tk()
ventana.geometry("2000x3000") #dimensiones



ventana.config(bg="blue")  
ventana.bind("<Up>", up_key)
ventana.bind("<Down>", down_key)
ventana.bind("<Left>", left_key)
ventana.bind("<Right>", right_key)

gui = Pantalla()

gui.tablerogui(ventana,pacman.matriz)
#if num == 2:
    #gui.tablerogui(ventana,si)

print("control")
#control.see_key()
ventana.mainloop()
