import ply.lex as lex

count = 0

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'MOD',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'COLON',
    'SEMICOLON',
    'WORD',
    'ID',
    'DOT',
    'MIDFUNC',
    'QUOTE',
    'EMIT',
    'EXCLAMATION',
    'INTERROGATION',
    'CR',
    'KEY',
    'IF',
    'THEN',
    'ELSE',
    'SUP',
    'INF',
    'EQUALS'
)

t_MINUS = r'-'
t_RPAREN = r'\)'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PLUS = r'\+'
t_MOD = r'%'
t_COLON = r':'
t_SEMICOLON = r';'
t_DOT = r'\.'
t_QUOTE = r'"'
t_EXCLAMATION = r'!'
t_INTERROGATION = r'\?'
t_CR = r'\n'
t_SUP = r'\>'
t_INF = r'\<'
t_EQUALS = r'='

parameter_list = False


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_KEY(t):
    r'KEY'
    return t

def t_IF(t):
    r'if'
    return t

def t_THEN(t):
    r'then'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WORD(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    global parameter_list
    if parameter_list or t.value == '(':
        t.type = 'ID'
    return t


def t_ID(t):
    r'[a-z]'
    global parameter_list
    if t.value == '-':
        t.type = 'WORD'
    return t


def t_LPAREN(t):
    r'\('
    global parameter_list
    parameter_list = True
    return t


def t_MIDFUNC(t):
    r'\-{2}'
    global parameter_list
    parameter_list = False
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def count_id(tokens):
    count = 0
    for token in tokens:
        if token.type == 'ID':
            count += 1
    return count


def count_number(tokens):
    count = 0
    for token in tokens:
        if token.type == 'NUMBER':
            count += 1
    return count


lexer = lex.lex()

# def lexer_debug(example):
#     lexer.input(example)
#     tokens = []
#     while token := lexer.token():
#         print(token)
#         tokens.append(token)
#     print(count_id(tokens))


# exemplo = ": maior > if pessego else banana then ; "
# lexer_debug(exemplo)
