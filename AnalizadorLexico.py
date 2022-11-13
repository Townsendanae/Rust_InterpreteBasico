import ply.lex as lex

#Palabras reservadas

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
  #completar

}

#definir listado de tokens
signs_tokens = [
    'PLUS','MINUS','TIMES','DIVIDE','MATH_REMINDER','ASSIGN','EQUALS','NOT_EQUALS','LESS_THAN','LESSEQUAL_THAN',
    'MORE_THAN','MOREEQUAL_THAN','AND','OR','NOT','AND_BIT','OR_BIT','XOR_BIT','NOT_BIT','LEFT_MAYUS','RIGHT_MAYUS',
    'LPAREN','RPAREN','VARIABLE'
]

data_type_tokens = [
    'INTEGER','DECIMAL','HEXADECIMAL' ##completar
    ]

tokens = signs_tokens + data_type_tokens + list(reserved.values())

#Expresiones regulares
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'
t_PLUS = r'\+'


