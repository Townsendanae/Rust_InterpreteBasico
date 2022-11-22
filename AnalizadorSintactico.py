import ply.yacc as yacc
from AnalizadorLexico import tokens

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
    | link'''

# Rommel


def p_asignacion(p):
    'asignacion : LET VARIABLE ASSIGN valor COMMA_DOT'

# Rommel


def p_valor(p):
    '''valor : STRING
    | CHAR
    | DECIMAL
    | HEXADECIMAL
    | OCTAL
    | BINARIO
    | BOOL
    | FLOAT'''

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
    'vector : LET VARIABLE ASSIGN VEC NOT LBRACKET valores RBRACKET '


def p_valores(p):
    '''valores : valor
    | valor COMA valores'''


#hashmap: Rommel
def p_hashMap(p):
    'hashMap : LET MUT VARIABLE ASSIGN HASHMAP TWO_POINTS TWO_POINTS NEW LPAREN RPAREN COMMA_DOT'

#structs: Ronald


def p_struct(p):
    'struct : STRUCT VARIABLE LKEY atributos RKEY'


def p_atributos(p):
    '''atributos : VARIABLE TWO_POINTS valor
    | VARIABLE TWO_POINTS valor COMA atributos'''

# Reglas
# definicion de funciones y mutabilidad: Rommel


def p_asignacionMutable(p):
    'asignacionMutable : LET MUT VARIABLE ASSIGN valor COMMA_DOT'


def p_funcion(p):
    'funcion : FN VARIABLE parametros LKEY instruccion RKEY'


def p_parametros(p):
    '''parametros : LPAREN RPAREN
    | LPAREN parametro RPAREN'''


def p_parametro(p):  # Corrección por Danae
    '''parametro : VARIABLE TWO_POINTS valor 
    | VARIABLE TWO_POINTS valor COMA parametro'''


def p_funcionDiv(p):
    'funcionDiv : FN VARIABLE parametros MINUS MORE_THAN NOT LKEY instruccion RKEY'


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
    'trait : LESS_THAN GENERIC TWO_POINTS VARIABLE MORE_THAN '


def p_apuntador(p):
    'apuntador : LET VARIABLE TWO_POINTS FN parametros MINUS MORE_THAN valor ASSIGN VARIABLE COMMA_DOT'

# Por hacer: entrada y salida de datos


def p_error(p):
    if p:
        print(
            f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
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
    if not s:
        continue
    validaRegla(s)
