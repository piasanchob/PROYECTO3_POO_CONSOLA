import random
#from space_invaders import *
import keyboard
import msvcrt as m
import win32api
import time
import socket
from tkinter import *
from tkinter import messagebox
import pygame

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

#size = (width, height)

pygame.mixer.music.load("tet.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)


class Consola():
    def __init__(self, matriz, gameOver):
        self.matriz = matriz
        self.gameOver = gameOver

    def adelante_pacman(self):
        # adelante pacman
        coin = False
        for l in self.matriz:

            if 2 in l:

                coin = True
        if coin == False:
            self.gameOver = True
            print("GAME OVER")
            messagebox.showinfo(message="GAME OVER")
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
                        messagebox.showinfo(message="GAME OVER")
                        self.gameOver = True
                        break
                    l[new] = x
                    l[old] = 0
                    break

        pacman.fantasmas()
        for x in self.matriz:
            print(x)
        gui.tablerogui(self.matriz)

        # control.see_key()

    def atras_pacman(self):
        # atras pacman
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
                        messagebox.showinfo(message="GAME OVER")
                        self.gameOver = True
                        break
                    l[new] = x
                    l[old] = 0
                    break
        pacman.fantasmas()
        for x in self.matriz:
            print(x)
        gui.tablerogui(self.matriz)

        # control.see_key()

    def arriba_pacman(self):
        # arriba pacman
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for l in self.matriz:
            for x in self.matriz[indices[0]]:
                if x == 3:
                    c = indices[0]
                    # if self.matriz[c] == l:
                    aux = self.matriz[indices[0]]
                    old = aux.index(x)
                    if self.matriz[c - 1][old] == 7:
                        print("GAME OVER")
                        messagebox.showinfo(message="GAME OVER")
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
        gui.tablerogui(self.matriz)

        # control.see_key()

    def abajo_pacman(self):
        # abajo pacman
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        indices.sort(reverse=True)
        for l in self.matriz:
            for x in self.matriz[indices[0]]:
                if x == 3:
                    c = indices[0]
                    aux = self.matriz[indices[0]]
                    old = aux.index(x)
                    if self.matriz[c + 1][old] == 7:
                        print("GAME OVER")
                        messagebox.showinfo(message="GAME OVER")
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
        gui.tablerogui(self.matriz)

        # control.see_key()

    def adelante_fantasma(self):
        # adelante fantasma
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
                    gui.tablerogui(self.matriz)

                    break

            if huboError:
                break
            indices.pop(0)

    def atras_fantasma(self):
        # atras fantasma
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
                    gui.tablerogui(self.matriz)

                    break

            if huboError:
                break
            indices.pop(0)

    def arriba_fantasma(self):
        # arriba fantasma
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
                    gui.tablerogui(self.matriz)

                    break

            if huboError:
                break
            indices.pop(0)

    def abajo_fantasma(self):
        # abajo fantasma
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        indices.sort(reverse=True)
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
                    gui.tablerogui(self.matriz)

                    break

            if huboError:
                break
            indices.pop(0)

    def disparar(self):
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        indices.sort(reverse=True)

        #indices = [0,1,2,3,4,5,6,7,8,9]
        alien = False
        for l in self.matriz:

            if 4 in l:

                alien = True
        if alien == False:
            self.gameOver = True
            print("GAME OVER")
            messagebox.showinfo(message="GAME OVER")
        for l in self.matriz:
            for x in l:
                if x == 8:
                    old = l.index(x)
                    new = self.matriz.index(l) - 3
                    if self.matriz[new][old] == 4:
                        self.matriz[new][old] = 0
                        gui.tablerogui(self.matriz)
                        break

        for x in self.matriz:
            print(x)

        for l in self.matriz:
            for x in self.matriz[indices[0]]:
                if x == 4:
                    c = indices[0]
                    aux = self.matriz[indices[0]]
                    old = aux.index(x)
                    if self.matriz[c + 1][old] == 8 or self.matriz[c + 1][old] == 6:
                        print("GAME OVER")
                        messagebox.showinfo(message="GAME OVER")
                        self.gameOver = True
                        break

                    self.matriz[c + 1][old] = x
                    self.matriz[c][old] = 0
                    break
            indices.pop(0)

        # pacman.fantasmas()
        for x in self.matriz:
            print(x)
        gui.tablerogui(self.matriz)

    def fantasmas(self):
        while not self.gameOver:
            r = random.randint(1, 4)
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

    def adelante_space(self):
        for l in self.matriz:
            for x in l:
                if x == 8:
                    old = l.index(x)
                    new = old + 1

                    l[new] = x
                    l[old] = 0
                    break

        for x in self.matriz:
            print(x)
        gui.tablerogui(self.matriz)

    def atras_space(self):
        for l in self.matriz:
            for x in l:
                if x == 8:
                    old = l.index(x)
                    new = old - 1

                    l[new] = x
                    l[old] = 0
                    break

        for x in self.matriz:
            print(x)
        gui.tablerogui(self.matriz)


class Controlador():

    def see_key(self, num):
        #print("presione tecla de dirección o presione A para acción")
        if num == 1:
            print("UP")
            action.make_action("UP")
            # Cl.send_msg("UP")
        if num == 2:
            print("DOWN")
            action.make_action("DOWN")
            # Cl.send_msg("DOWN")
        if num == 3:
            print("LEFT")
            action.make_action("LEFT")
            # Cl.send_msg("LEFT")
        if num == 4:
            print("RIGHT")
            action.make_action("RIGHT")
            # Cl.send_msg("RIGHT")
        time.sleep(0.1)
# Servidor.start()


class Pantalla():
    def __init__(self, tab, tablero):
        self.tablero = []

        for i in range(len(tablero)):
            row = []

            for j in range(len(tablero[i])):
                row.append(Button(tab, width=4, heigh=2, font="Arial"))
                row[j].grid(row=i, column=j)

            self.tablero.append(row)

    def tablerogui(self, tablero):
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
                if tablero[i][j] == 8:
                    fontcolor = "lime"
                    bgcolor = "lime"
                if tablero[i][j] == 4:
                    fontcolor = "cyan"
                    bgcolor = "cyan"
                if tablero[i][j] == 6:
                    fontcolor = "purple"
                    bgcolor = "purple"

                self.tablero[i][j].config(
                    text=tablero[i][j], fg=fontcolor, bg=bgcolor, width=4, heigh=2, font="Arial")


pacman = Consola([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 7, 0, 0, 1, 1, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 1, 0, 2, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], False)

spaceinvaders = Consola([
    [0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]], False)

# for x in matriz:
# print(x)


class Action():
    def __init__(self, juego):
        self.juego = juego

    def make_action(self, msg):
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
                spaceinvaders.adelante_space()
            if msg == "LEFT":
                spaceinvaders.atras_space()
            if msg == "UP":
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


control = Controlador()

ventana = Tk()
ventana.geometry("2000x3000")  # dimensiones


ventana.config(bg="gold")
L = Label(ventana, text="ARCADE", fg="blue", font="Arial", bg="gold")
L.config(font=("Courier", 100))
L.place(x=800, y=100)
ventana.bind("<Up>", up_key)
ventana.bind("<Down>", down_key)
ventana.bind("<Left>", left_key)
ventana.bind("<Right>", right_key)

gui = Pantalla(ventana, pacman.matriz)

gui.tablerogui(pacman.matriz)
# if num == 2:
# gui.tablerogui(ventana,si)

print("control")
# control.see_key()
ventana.mainloop()
