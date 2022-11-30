from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from AnalizadorLexico import *
from AnalizadorSintactico import *
from tkinter import filedialog

#funciones extras
def open_file():
    archivo_Ruta = filedialog.askopenfilename(
        initialdir = "/", title = "Seleccione archivo", 
        filetypes = (("Rust files",".rs"), ("all files",".*")))
    print(archivo_Ruta)
    archivo = open(archivo_Ruta)
    content = ""
    for line in archivo: 
        content += line
    print(content)
    entrada.set(content)

def popup(lst):
    lexer.lineno = 1
    panel2 = Tk()
    ventana2 = Frame(panel2,width=500,height=500)
    ventana2.pack()
    scrollbar = Scrollbar(ventana2)
    scrollbar.pack( side = RIGHT, fill = BOTH )
    mylist = Listbox(ventana2, yscrollcommand = scrollbar.set , width=100)
    mylist.place(x = 10,
        y = 10,
        width=250,
        height=150)
    mylist.pack()
    scrollbar.config( command = mylist.yview )
    for line in lst:
        mylist.insert(END, line + '\n')
    if len(lst) == 0:
        mylist.insert(END,'¡No se encontraron errores! Póngale 100!  \n')

def clear():
    entrada.set("")

#Funciones analisis lexico
def show_analisis_lexico():
    content=entrada.get()
    lexer.input(content)
    getTokens(lexer)
    popup(lstTokens)  


#Funciones analisis sintáctico
def show_analysis_sintacticoYSemantico(): #comentar el while True del analizador sintactico y colocar el clear a la lista en validarRegla
    s = entrada.get()
    validaRegla(s)  
    popup(lstErrores)

#funciones analisis semantico



#main
panel = Tk()
ventana = Frame(panel,width=580,height=300)
ventana.pack()


titulo = tk.Label(ventana,text="ANALIZADOR BÁSICO DE RUST",font=("Arial",18), fg="black", bg="aliceblue").place(x=5,y=8)
lb1 = tk.Label( ventana,text="Ingrese código en Rust",fg="black", bg="ivory").place(x=10,y=50)
entrada = tk.StringVar()
tk.Entry(ventana,textvariable=entrada, font=("Arial",8), width=90).place(height=60,x=10,y=80)
botonLexico = tk.Button(ventana,text="Analizador Léxico",  command=show_analisis_lexico).place(width=130,x=10,y=150)
botonSintacticoYSemantico = tk.Button(ventana,text="Analizador Sintáctico y Semántico",  command=show_analysis_sintacticoYSemantico).place(width=200,x=160,y=150)
botonClear = tk.Button(ventana,text="Clear",  command=clear).place(width=130,x=380,y=150)
botonOpenFile = tk.Button(ventana,text="Abrir archivo",  command=open_file).place(width=130,x=190,y=200)
ventana.mainloop()
