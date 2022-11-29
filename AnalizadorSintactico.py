import ply.yacc as yacc
from datetime import datetime
from AnalizadorLexico import tokens
"""
# Rommel

# Rommel



# Estructuras de control
#match: Rommel



def p_imprimir(p):
    'imprimir : PRINTLN NOT LPAREN valor RPAREN'

#loop: Ronald


# for: Danae


# Estructuras de datos
#vectores: Danae



#structs: Ronald



# Reglas
# definicion de funciones y mutabilidad: Rommel 


# casting, alias y enlaces a variables: Ronald

def p_casting(p):
    '''casting : valor AS valor
    | valor AS casting
    | VARIABLE AS valor
    | VARIABLE AS casting'''


def p_alias(p):
    'alias : TYPE VARIABLE ASSIGN valor COMMA_DOT'


def p_link(p):
    'link : LET LPAREN variables RPAREN ASSIGN LPAREN valores RPAREN COMMA_DOT'


def p_variables(p):
    '''variables : VARIABLE 
    | VARIABLE COMA variables'''

# apuntadores, traits y parametros:Danae


# Por hacer: entrada y salida de datos

"""

def p_cuerpo(p):
    '''cuerpo : asignacion
    | struct
    | varEnVar
    | definirFuncion
    | hashMap
    | vector
    | for
    | loop
    | eMatch
    '''    

def p_asignacion(p):
    '''asignacion : definicion ASSIGN valorAsignado COMMA_DOT
    | VARIABLE ASSIGN valorAsignado COMMA_DOT
    | VARIABLE ASSIGN varEnVar COMMA_DOT
    | definicion'''

def p_varEnVar(p):
    'varEnVar : VARIABLE POINT VARIABLE'

def p_definicion(p):
    '''definicion : creacion
    | creacion COMMA_DOT
    | creacion tipoDato'''

def p_creacion(p):
    '''creacion : LET MUT VARIABLE
    | LET VARIABLE
    | CONST VARIABLE'''

def p_tipoDato(p):
    '''tipoDato : TWO_POINTS dato
    | TWO_POINTS dato tipoDato
    | LESS_THAN dato MORE_THAN
    | TWO_POINTS apuntador
    '''

def p_dato(p):
    '''dato : STRING
    | CHAR
    | DECIMAL
    | HEXADECIMAL
    | OCTAL
    | BINARIO
    | BOOL
    | FLOAT
    | VEC
    | GENERIC
    '''

def p_valorAsignado(p):
    '''valorAsignado : dato
    | llamadaAfuncion
    | llamadaAfuncionPorAlias
    | vector
    | hashMap
    | VARIABLE'''

def p_llamadaAfuncionPorAlias(p):
    '''llamadaAfuncionPorAlias : VARIABLE POINT llamadaAfuncion'''

def p_llamadaAfuncion(p):
    '''llamadaAfuncion : VARIABLE argumentos
    | VARIABLE argumentos POINT llamadaAfuncion
    | VARIABLE TWO_POINTS TWO_POINTS argumentos
    | VARIABLE TWO_POINTS TWO_POINTS
    | VARIABLE TWO_POINTS TWO_POINTS llamadaAfuncion'''

def p_argumentos(p):
    '''argumentos : LPAREN argumento RPAREN
    | LPAREN RPAREN'''

def p_argumento(p):
    '''argumento : VARIABLE
    | dato
    | VARIABLE COMA argumento
    | dato COMA argumento
    | llamadaAfuncion
    | llamadaAfuncionPorAlias
    | llamadaAfuncion COMA argumento
    | llamadaAfuncionPorAlias COMA argumento'''

def p_definirFuncion(p):
    ''' definirFuncion : FN VARIABLE trait parametros LKEY cuerpoFuncion RKEY
    | FN VARIABLE parametros LKEY cuerpoFuncion RKEY
    '''

def p_trait(p):
    'trait : LESS_THAN GENERIC TWO_POINTS VARIABLE MORE_THAN '

def p_datoAretornar(p):
    ''' datoARetornar : MINUS MORE_THAN dato
    | MINUS MORE_THAN NOT
    '''

def p_parametros(p):
    '''parametros : LPAREN RPAREN datoARetornar
    | LPAREN parametro RPAREN datoARetornar
    | LPAREN RPAREN
    | LPAREN parametro RPAREN'''


def p_parametro(p):  # Corrección por Danae
    '''parametro : VARIABLE TWO_POINTS dato 
    | VARIABLE TWO_POINTS dato COMA parametro
    | dato COMA parametro
    | dato
    '''

def p_cuerpoFuncion(p):
    ''' cuerpoFuncion : cuerpo
    '''

#structs: Ronald
def p_struct(p):
    'struct : STRUCT VARIABLE LKEY atributos RKEY'

def p_atributos(p):
    '''atributos : VARIABLE TWO_POINTS dato
    | VARIABLE TWO_POINTS dato COMA atributos'''

#vectores: Danae, agregar la otra forma de definir vectores
def p_vector(p):
    '''vector : VEC NOT LBRACKET datos RBRACKET '''

def p_datos(p):
    '''datos : dato
    | dato COMA datos'''

#hashmap: Rommel
def p_hashMap(p):
    'hashMap : HASHMAP TWO_POINTS TWO_POINTS NEW LPAREN RPAREN'

# for: Danae
def p_for(p):
    'for : FOR VARIABLE IN rango LKEY cuerpoFuncion RKEY'


def p_rango(p):
    ''' rango : DECIMAL POINT POINT DECIMAL
    | DECIMAL POINT POINT ASSIGN DECIMAL '''
    
#match: Rommel
def p_eMatch(p):
    'eMatch : MATCH VARIABLE LKEY content RKEY'


def p_content(p):
    '''content : dato MOREEQUAL_THAN cuerpoFuncion
    | dato MOREEQUAL_THAN cuerpoFuncion COMA content'''

#loop: Ronald
def p_loop(p):
    'loop : LOOP LKEY cuerpoFuncion RKEY'

def p_apuntador(p):
    'apuntador : FN parametros'

def p_error(p):
    if p:
        msg = f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}" 
        # print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
        lstErrores.append(msg)
        parser.errok()
    else:
        msg = "Error de sintaxis Fin de Linea"
        lstErrores.append(msg)
        # print("Error de sintaxis Fin de Linea")


parser = yacc.yacc()
lstErrores = list()

def validaRegla(s):
  lstErrores.clear()
  print(lstErrores) 
  result = parser.parse(s)
  logs = open('logs.txt','a')
  logs.write(s+' '+str(datetime.now())+'\n')
  return result
  
  

# while True:
#     try:
#         s = input('calc > ')
#         lstErrores = []
#     except EOFError:
#         break
#     if not s:
#         continue
#     validaRegla(s)
#     print(lstErrores)

    

