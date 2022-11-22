import ply.yacc as yacc
from AnalizadorLexico import tokens

#Rommel
def p_cuerpo(p):
  '''cuerpo : asignacion
  | asignacionMutable
  | eMatch
  | instruccion
  | funcion
  | funcionDiv'''

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
def p_eMatch(p):
 'eMatch : MATCH VARIABLE LKEY content RKEY'

def p_content(p):
  '''content : valor MOREEQUAL_THAN instruccion
  | valor MOREEQUAL_THAN instruccion COMA content'''

def p_instruccion(p):
  '''instruccion : imprimir
  | hashMap'''

def p_imprimir(p):
  'imprimir : PRINTLN NOT LPAREN valor RPAREN'

#loop: Ronald



#for: Danae



#Estructuras de datos
#vectores: Danae



#hashmap: Rommel
def p_hashMap(p):
  'hashMap : LET MUT VARIABLE ASSIGN HASHMAP TWO_POINTS TWO_POINTS NEW LPAREN RPAREN COMMA_DOT'

#structs: Ronald



#Reglas
#definicion de funciones y mutabilidad: Rommel
def p_asignacionMutable(p):
  'asignacionMutable : LET MUT VARIABLE ASSIGN valor COMMA_DOT'

def p_funcion(p):
  'funcion : FN VARIABLE parametros LKEY instruccion RKEY'

def p_parametros(p):
  '''parametros : LPAREN RPAREN
  | LPAREN parametro RPAREN'''

def p_parametro(p):
  '''parametro : VARIABLE
  | VARIABLE COMA parametro'''

def p_funcionDiv(p):
  'funcionDiv : FN VARIABLE parametros MINUS MORE_THAN NOT LKEY instruccion RKEY'
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