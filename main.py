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

#Funciones analisis lexico
def show_analisis_lexico():
    content=entrada.get()
    lexer.input(content)
    getTokens(lexer)
    popup(lstTokens)  


#Funciones analisis sintáctico
def show_analysis_sintactico(): #comentar el while True del analizador sintactico y colocar el clear a la lista en validarRegla
    s = entrada.get()
    validaRegla(s)  
    popup(lstErrores)

#funciones analisis semantico
def show_analysis_semantico():
    content=entrada.get()
    print(content)


#main
panel = Tk()
ventana = Frame(panel,width=500,height=300)
ventana.pack()


titulo = tk.Label(ventana,text="ANALIZADOR BÁSICO DE RUST",font=("Arial",18), fg="black", bg="aliceblue").place(x=5,y=8)
lb1 = tk.Label( ventana,text="Ingrese código en Rust",fg="black", bg="ivory").place(x=10,y=50)
entrada = tk.StringVar()
tk.Entry(ventana,textvariable=entrada, font=("Arial",8), width=80).place(height=60,x=10,y=80)
botonLexico = tk.Button(ventana,text="Analizador Léxico",  command=show_analisis_lexico).place(width=130,x=10,y=150)
botonSintactico = tk.Button(ventana,text="Analizador Sintáctico",  command=show_analysis_sintactico).place(width=130,x=160,y=150)
botonSemantico = tk.Button(ventana,text="Analizador Semántico",  command=show_analysis_semantico).place(width=130,x=310,y=150)
botonOpenFile = tk.Button(ventana,text="Abrir archivo",  command=open_file).place(width=130,x=160,y=200)
lb2_Title = tk.Label(ventana, text="Salida: ",fg="black", bg="ivory").place(x=10,y=250)


ventana.mainloop()
