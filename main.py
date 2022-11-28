from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from AnalizadorLexico import *

#funciones Complementarias
def getTokens(lexer):
    lstTokens = []
    for token in lexer:
        output = f'Line: {token.lineno} | Type: {token.type} | Value: {token.value}'
        lstTokens.append(output)
        print(f'Line: {token.lineno} | Type: {token.type} | Value: {token.value}')
    string_output.set("\n".join(lstTokens))  
    

#Funciones analisis lexico
def show_analisis_lexico():
    content=entrada.get()
    lexer.input(content)
    getTokens(lexer)


#Funciones analisis sintáctico
def show_analysis_sintactico():
    content=entrada.get()
    print(content)
    
#funciones analisis semantico
def show_analysis_semantico():
    content=entrada.get()
    print(content)




#main
panel = Tk()
ventana = Frame(panel,width=500,height=500)
ventana.pack()
titulo = tk.Label(text="ANALIZADOR BÁSICO DE RUST",font=("Arial",18), fg="black", bg="aliceblue").place(x=5,y=8)
lb1 = tk.Label( text="Ingrese código en Rust",fg="black", bg="ivory").place(x=10,y=50)
entrada = tk.StringVar()
tk.Entry(textvariable=entrada, font=("Arial",8), width=80).place(height=60,x=10,y=80)
botonLexico = tk.Button(text="Analizador léxico",  command=show_analisis_lexico).place(width=130,x=10,y=150)
botonSintactico = tk.Button(text="Analizador Sintáctico",  command=show_analysis_sintactico).place(width=130,x=160,y=150)
botonSemantico = tk.Button(text="Analizador Semántico",  command=show_analysis_semantico).place(width=130,x=310,y=150)
lb2_Title = tk.Label( text="Salida: ",fg="black", bg="ivory").place(x=10,y=200)
string_output = StringVar()
string_output.set("")
lb3_Output = tk.Label(textvariable=string_output,fg="black", bg="ivory").place(x=10,y=230)
ventana.mainloop()
