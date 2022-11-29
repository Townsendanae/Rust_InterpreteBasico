import ply.yacc as yacc
from datetime import datetime
from AnalizadorLexico import tokens
"""
# Rommel


def p_cuerpo(p):
    '''cuerpo : asignacion
    | asignacionMutable
    | eMatch
    | instruccion
    | funcion
    | funcionDiv
    | vector
    | for
    | apuntador
    | trait 
    | loop
    | struct
    | casting
    | alias
    | link
    | parametro''' agregado

# Rommel


def p_asignacion(p):
    'asignacion : LET VARIABLE ASSIGN valor COMMA_DOT' agregado

# Rommel


def p_valor(p):
    '''valor : STRING
    | CHAR
    | DECIMAL
    | HEXADECIMAL
    | OCTAL
    | BINARIO
    | BOOL
    | FLOAT''' agregado

# Estructuras de control
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


def p_loop(p):
    'loop : LOOP LKEY instruccion RKEY'


# for: Danae
def p_for(p):
    'for : FOR VARIABLE IN rango LKEY instruccion RKEY'


def p_rango(p):
    ''' rango : DECIMAL POINT POINT DECIMAL
    | DECIMAL POINT POINT ASSIGN DECIMAL '''

# Estructuras de datos
#vectores: Danae


def p_vector(p):
    'vector : LET VARIABLE ASSIGN VEC NOT LBRACKET valores RBRACKET ' agregado


def p_valores(p):
    '''valores : valor
    | valor COMA valores''' agregado


#hashmap: Rommel
def p_hashMap(p):
    'hashMap : LET MUT VARIABLE ASSIGN HASHMAP TWO_POINTS TWO_POINTS NEW LPAREN RPAREN COMMA_DOT' agregado

#structs: Ronald


def p_struct(p):
    'struct : STRUCT VARIABLE LKEY atributos RKEY' agregado


def p_atributos(p):
    '''atributos : VARIABLE TWO_POINTS valor
    | VARIABLE TWO_POINTS valor COMA atributos''' agregado

# Reglas
# definicion de funciones y mutabilidad: Rommel 


def p_asignacionMutable(p):
    'asignacionMutable : LET MUT VARIABLE ASSIGN valor COMMA_DOT' agregado


def p_funcion(p):
    'funcion : FN VARIABLE parametros LKEY instruccion RKEY' agregado


def p_parametros(p):
    '''parametros : LPAREN RPAREN
    | LPAREN parametro RPAREN''' agregado


def p_parametro(p):  # Corrección por Danae
    '''parametro : VARIABLE TWO_POINTS valor 
    | VARIABLE TWO_POINTS valor COMA parametro
    | VARIABLE TWO_POINTS GENERIC
    | VARIABLE TWO_POINTS GENERIC COMA parametro''' agregado


def p_funcionDiv(p):
    'funcionDiv : FN VARIABLE parametros MINUS MORE_THAN NOT LKEY instruccion RKEY' agregado


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


def p_trait(p):
    'trait : LESS_THAN GENERIC TWO_POINTS VARIABLE MORE_THAN ' agregado


def p_apuntador(p):
    'apuntador : LET VARIABLE TWO_POINTS FN parametros MINUS MORE_THAN valor ASSIGN VARIABLE COMMA_DOT'

# Por hacer: entrada y salida de datos

"""

def p_cuerpo(p):
    '''cuerpo : asignacion
    | definicion
    | struct
    | varEnVar
    | definirFuncion
    | hashMap
    | vector
    '''    

def p_asignacion(p):
    '''asignacion : definicion ASSIGN valorAsignado COMMA_DOT
    | VARIABLE ASSIGN valorAsignado COMMA_DOT
    | VARIABLE ASSIGN varEnVar COMMA_DOT'''

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
    | hashMap'''

def p_llamadaAfuncionPorAlias(p):
    '''llamadaAfuncionPorAlias : VARIABLE POINT llamadaAfuncion'''

def p_llamadaAfuncion(p):
    '''llamadaAfuncion : VARIABLE argumentos
    | VARIABLE argumentos POINT llamadaAfuncion
    | VARIABLE TWO_POINTS TWO_POINTS argumentos'''

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
  result = parser.parse(s)
  logs = open('logs.txt','a')
  logs.write(s+' '+str(datetime.now())+'\n')
  return result
  
  

while True:
    try:
        s = input('calc > ')
        lstErrores = []
    except EOFError:
        break
    if not s:
        continue
    validaRegla(s)
    print(lstErrores)

