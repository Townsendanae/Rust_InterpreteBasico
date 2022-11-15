import ply.lex as lex

#reserverd words
reserved = {
  'as':'AS',
  'use':'USE',
  'extern crate':'EXTERN_CRATE',
  'break':'BREAK',
  'const':'CONST',
  'continue':'CONTINUE',
  'crate':'CRATE',
  'else':'ELSE',
  'if':'IF',
  'if let':'IF_LET'
  # --> completar Ronald

}

#definir listado de tokens
punctuation_tokens = [
    'LPAREN','RPAREN'
    ]

math_tokens = [
    'PLUS','MINUS','TIMES','DIVIDE','MATH_REMINDER'
]

compare_tokens = [
    'ASSIGN','EQUALS','NOT_EQUALS','LESS_THAN','LESSEQUAL_THAN',
    'MORE_THAN','MOREEQUAL_THAN'
    ]

logic_tokens = [
    'AND','OR','NOT'
    ]

bit_tokens = [
    'AND_BIT','OR_BIT','XOR_BIT','LEFT_MAYUS','RIGHT_MAYUS'
    ]


data_type_tokens = [
    'VARIABLE','INTEGER','DECIMAL','HEXADECIMAL', 'OCTAL', 'BINARIO', 'BYTE',
     'CHAR', 'STRING', 'BOOL', 'FLOAT'## -->completar David
    ]

tokens = punctuation_tokens + math_tokens + compare_tokens + logic_tokens + bit_tokens + data_type_tokens + list(reserved.values())


#Expresiones regulares - punctuation
t_LPAREN = r'\('
t_RPAREN = r'\)'

#Expresiones regulares - math
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MATH_REMINDER = r'%'

#Expresiones regulares - compare
t_ASSIGN = r'='
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_LESS_THAN = r'<'
t_LESSEQUAL_THAN = r'<='
t_MORE_THAN = r'>'
t_MOREEQUAL_THAN = r'=>'

#Expresiones regulares - logic
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

#Expresiones regulares - bit
t_AND_BIT = r'&'
t_OR_BIT = r'\|'
t_XOR_BIT = r'\^'
t_LEFT_MAYUS = r'<<'
t_RIGHT_MAYUS = r'>>'

#Expresiones regulares con reglas - tipo de datos --> Completar David y Ronald mitad y mitad


def t_HEXADECIMAL(t):
    r'0x[0-9a-f_]*'
    return t

def t_OCTAL(t):
    r'0o[0-7_]*'
    return t

def t_BINARIO(t):
    r'0b[0,1]*'
    return t

def t_FLOAT(t):
  r'\d+\.\d+'
  return t

def t_DECIMAL(t):
    r'[0-9_]{1,}'
    return t

def t_BOOL(t):
  r'(true|false)'
  return t
  
def t_STRING(t):
  r'(\'.*\')|(\".*\")'
  return t

def t_VARIABLE(t):
    r'[a-z][a-z0-9_]*'
    t.type = reserved.get(t.value,'VARIABLE')
    return t


#Agregar t_COMMENTS, t_newline, entre otras pertinentes --> Ronald
#t_ERROR --> David

def t_error(t):
  print("Caracter no permitido'%s'" % t.value[0])
  t.lexer.skip(1)

#Construir el lexer, funcion getTokens y leer el archivo --> David 
lexer = lex.lex()

file = open('./AlgoritmoMarcilloRommel.rs', 'r')
content = file.read()

lexer.input(content)
def getTokens(lexer):
  for token in lexer:
    print(f'Line: {token.lineno} | Type: {token.type} | Value: {token.value}')

linea=" "

getTokens(lexer)

#Mostrar en consola el lexer --> David
while linea!="":
    #lexer.input(linea)
    linea=input(">>")
    lexer.input(linea)
    #getTokens(lexer
    getTokens(lexer)
    
# Tokenize
print("Succesfull")



