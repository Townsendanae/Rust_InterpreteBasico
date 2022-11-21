import ply.yacc as yacc
from AnalizadorLexico import tokens

#Rommel
def p_cuerpo(p):
  '''cuerpo : asignacion
  | asignacionMutable'''

#Rommel
def p_asignacion(p):
  'asignacion : LET VARIABLE ASSIGN valor COMMA_DOT'

#Rommel
def p_valor(p):
  '''valor : STRING
  | CHAR
  | DECIMAL
  | HEXADECIMAL
  | OCTAL
  | BINARIO
  | BOOL
  | FLOAT'''

#Estructuras de control
#match: Rommel



#loop: Ronald



#for: Danae



#Estructuras de datos
#vectores: Danae



#hashmap: Rommel



#structs: Ronald



#Reglas
#definicion de funciones y mutabilidad: Rommel
def p_asignacionMutable(p):
  'asignacionMutable : LET MUT VARIABLE ASSIGN valor COMMA_DOT'


#casting, alias y enlaces a variables: Ronald



#apuntadores, traits y parametros:Danae


#Por hacer: entrada y salida de datos

def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
 
parser = yacc.yacc()

def validaRegla(s):
  result = parser.parse(s)
  print(result)

while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)