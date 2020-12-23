from tkinter import *
from consola import *

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
                    fontcolor = "orange"
                    bgcolor = "orange"
                if tablero[i][j] == 1:
                    fontcolor = "blue"
                    bgcolor = "blue"
                if tablero[i][j] == 7:
                    fontcolor = "red"
                    bgcolor = "red"
                

                b = Button(tab, text=tablero[i][j], fg=fontcolor, bg = bgcolor, width=2, heigh=4, font="Arial")
                b.grid(row=i, column=j)

ventana = Tk()
ventana.geometry("1000x500") #dimensiones

ventana.config(bg="pink")  
gui = Pantalla()
gui.tablerogui(ventana,pacman.matriz)   

