import ply.lex as lex

#reserverd words
reserved = {
  'as':'AS',
  'use':'USE',
  'extern crate':'EXTERN CRATE',
  'break':'BREAK',
  'const':'CONST',
  'continue':'CONTINUE',
  'crate':'CRATE',
  'else':'ELSE',
  'if':'IF',
  'if let':'IF LET'
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
    'VARIABLE','INTEGER','DECIMAL','HEXADECIMAL' ## -->completar David
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
t_XOR_BIT = r'^'
t_LEFT_MAYUS = r'<<'
t_RIGHT_MAYUS = r'>>'

#Expresiones regulares con reglas - tipo de datos --> Completar David y Ronald mitad y mitad

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'VARIABLE')
    return t

def t_INTEGER(t):
    pass

def t_DECIMAL(t):
    pass

def t_HEXADECIMAL(t):
    pass


#Agregar t_COMMENTS, t_ERROR, t_newline, entre otras pertinentes --> Ronald

#Construir el lexer, funcion getTokens y leer el archivo --> David 

#Mostrar en consola el lexer --> Danae
linea=" "
while linea!="":
    linea=input(">>")
    #lexer.input(linea)
    #getTokens(lexer)
# Tokenize
print("Succesfull")



