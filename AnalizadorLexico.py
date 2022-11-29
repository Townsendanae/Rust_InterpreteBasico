import ply.lex as lex

# reserverd words --> Danaé 1/3
reserved = {
    'as': 'AS',
    'use': 'USE',
    'extern': 'EXTERN',
    'break': 'BREAK',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'crate': 'CRATE',
    'else': 'ELSE',
    'if': 'IF',
    # --> completar Ronald 2/3
    'enum': 'ENUM',
    'extern': 'EXTERN',
    'fn': 'FN',
    'for': 'FOR',
    'impl': 'IMPL',
    'in': 'IN',
    'let': 'LET',
    'loop': 'LOOP',
    'match': 'MATCH',
    'mod': 'MOD',
    'move': 'MOV',
    'mut': 'MUT',
    'pub': 'PUB',
    'impl': 'IMPL',
    'ref': 'REF',
    'return': 'RETURN',
    'self': 'SELF',
    'static': 'STATIC',
    'super': 'SUPER',
    'trait': 'TRAIT',
    'type': 'TYPE',
    'unsafe': 'UNSAFE',
    'use': 'USE',
    'where': 'WHERE',
    'while': 'WHILE',
    'abstract': 'ABSTRACT',
    'alignof': 'ALIGNOF',
    'become': 'BECOME',
    'box': 'BOX',
    'do': 'DO',
    'final': 'FINAL',
    'macro': 'MACRO',
    'offsetof': 'OFFSETOF',
    'override': 'OVERRIDE',
    'priv': 'PRIV',
    'proc': 'PROC',
    'pure': 'PURE',
    'sizeof': 'SIZEOF',
    'typeof': 'TYPEOF',
    'unsized': 'UNSIZED',
    'virtual': 'VIRTUAL',
    'yield': 'YIELD',
    'println': 'PRINTLN',
    'new': 'NEW',
    'struct': 'STRUCT'
}

# definir listado de tokens --> Danaé
punctuation_tokens = [
    'LPAREN', 'RPAREN', 'LKEY', 'RKEY', 'QUO_MARKS', 'COMA', "COMMA_DOT", "POINT", "TWO_POINTS","LBRACKET","RBRACKET"
]

math_tokens = [
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MATH_REMINDER'
]

compare_tokens = [
    'ASSIGN', 'EQUALS', 'NOT_EQUALS', 'LESS_THAN', 'LESSEQUAL_THAN',
    'MORE_THAN', 'MOREEQUAL_THAN'
]

logic_tokens = [
    'AND', 'OR', 'NOT'
]

bit_tokens = [
    'AND_BIT', 'OR_BIT', 'XOR_BIT', 'LEFT_MAYUS', 'RIGHT_MAYUS'
]


data_type_tokens = [
    'VARIABLE', 'INTEGER', 'DECIMAL', 'HEXADECIMAL', 'OCTAL', 'BINARIO', 'BYTE',
    'CHAR', 'STRING', 'BOOL', 'FLOAT', 'GENERIC', 'VEC', 'HASHMAP'  # -->completar David
]

tokens = punctuation_tokens + math_tokens + compare_tokens + \
    logic_tokens + bit_tokens + data_type_tokens + list(reserved.values())# --> Danae


#Expresiones Regulares --> Danaé
# Expresiones regulares - punctuation 
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LKEY = r'{'
t_RKEY = r'}'
t_COMA = r','
t_COMMA_DOT = r';' 
t_POINT = r'\.'
t_TWO_POINTS = r':'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Expresiones regulares - math
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MATH_REMINDER = r'%'

# Expresiones regulares - compare
t_ASSIGN = r'='
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_LESS_THAN = r'<'
t_LESSEQUAL_THAN = r'<='
t_MORE_THAN = r'>'
t_MOREEQUAL_THAN = r'=>'

# Expresiones regulares - logic
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# Expresiones regulares - bit
t_AND_BIT = r'&'
t_OR_BIT = r'\|'
t_XOR_BIT = r'\^'
t_LEFT_MAYUS = r'<<'
t_RIGHT_MAYUS = r'>>'

# Expresiones regulares con reglas - tipo de datos --> Completar David 1/2 y Ronald 1/2
def t_HASHMAP(t):
    r'HashMap'
    t.type = reserved.get(t.value,'HASHMAP')
    return t

def t_VEC(t):
    r'Vec|vec'
    t.type = reserved.get(t.value, 'VEC')
    return t

def t_GENERIC(t):
    r'T|\?|E|K|V|_'
    return t

def t_BOOL(t):
    r'(true|false)|bool'
    return t

def t_FLOAT(t):
    r'\d+\.\d+|f32|f64'
    return t


def t_HEXADECIMAL(t):
    r'0x[0-9a-f_]*'
    return t


def t_OCTAL(t):
    r'0o[0-7_]*'
    return t


def t_BINARIO(t):
    r'0b[0,1]*'
    return t


def t_DECIMAL(t):
    r'([0-9_]{1,})|i8|i16|i32|i64|i128|u8|u16|u32|u64|u128'
    return t


def t_BYTE(t):
    r"(b|B)'[a-zA-Z0-9]'"
    return t

def t_CHAR(t):
    r"'[a-zA-Z0-9]'|char"
    return t

def t_STRING(t):
    r'"[a-zA-Z0-9]*"|\'[a-zA-Z0-9]*\'|string|&str'
    return t

def t_VARIABLE(t):
    r'[a-z_][a-z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


# Agregar t_COMMENTS, t_newline, entre otras pertinentes --> Ronald
# t_ERROR --> David


def t_comments(t):
    r'//.*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t' 


def t_error(t):
    print("Caracter no permitido'%s'" % t.value[0])
    t.lexer.skip(1)


# Construir el lexer, funcion getTokens y leer el archivo --> David
lexer = lex.lex()
"""file = open('./AlgoritmoMarcilloRommel.rs', 'r')
content = file.read

lexer.input("Vec")


def getTokens(lexer):
    for token in lexer:
        print(
            f'Line: {token.lineno} | Type: {token.type} | Value: {token.value}')


linea = " \t"

getTokens(lexer)

# Mostrar en consola el lexer --> Danaé y David
while linea != "":
    # lexer.input(linea)
    linea = input(">>")
    lexer.input(linea)
    # getTokens(lexer
    getTokens(lexer)

# Tokenize
print("Succesfull")
"""