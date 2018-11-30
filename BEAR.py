# -----------------------------------------------------------------------------
# BEAR - Version 0.01a
#
# Social Network Analysis Language.
# -----------------------------------------------------------------------------

import networkx as nx
#import matplotlib.pyplot as plt
import ply.lex as lex
import ply.yacc as yacc
import Files as f

#lex part
reserved = {
    '//' : 'LSLASHES',
    '\\\\' : 'RSLASHES',
    'Bear' : 'BEAR',
    'if' : 'IF',
    'in' : 'IN',
    'else': 'ELSE',
    'for' : 'FOR',
    'from' : 'FROM',
    'while' : 'WHILE',
    'display' : 'DISPLAY',
    'create' : 'CREATE'
}
tokens = [
    'DIGIT',
    'CHARACTER',
    'ID',
    'LPAREN',
    'RPAREN',
    'LDELIMITER',
    'RDELIMITER',
    'COMMA',
    'SEPARATOR',
    'DOT',
    'PLUS',
    'MINUS',
    'BINOP',
    'BINARY'

] + (list(reserved.values()))
t_ignore = ' '
t_DIGIT = r'[0-9]+'
def t_CHARACTER(t) :
     r'[a-zA-Z-_.]+'
     if t.value in reserved:
         t.type = reserved[t.value]
     return t
t_ID = r'[a-zA-Z0-9-_]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSLASHES = r'//'
t_RSLASHES = r'\\\\'
t_BINARY = r'[\|\|&&]'
t_COMMA = r'\,'
t_BINOP = r'[>=|<|<=|>|!=|==]'
t_DOT = r'\.'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_SEPARATOR = r'\;'
t_LDELIMITER = r'\['
t_RDELIMITER = r'\]'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
# yacc part
# Parser
#underlying parser rules come before anything else, since they establish what the following rules will follow.
#Hierarchy goes top to bottom. ~Enrique

precedence = (
    ('left', 'LSLASHES', 'RSLASHES'),
    ('left', 'LPAREN', 'RPAREN')
)

def p_define(p):
    'test : BEAR function'
    #= ^p[0]   ^p[1]
    #treat p as if it were a list; each separate word is a cell in the list.
    p[0]= p[2]

def p_function(p):
    '''function : term
               | IF function COMMA function SEPARATOR ELSE function
               | FOR LSLASHES term IN function RSLASHES term
               | WHILE LSLASHES term BINOP term RSLASHES term'''
    p[0] = p[1]

def p_add(p) :
    '''add : graph PLUS LDELIMITER file COMMA node RDELIMITER
            | graph PLUS node'''
    p[0] = p[1]
def p_create(p):
    '''create : CREATE LSLASHES CHARACTER RSLASHES
                | CREATE LSLASHES CHARACTER FROM file RSLASHES'''
    p[0]= f.createGraph()
def p_remove(p) :
    'remove : graph MINUS node'
    p[0] = p[1]

def p_display(p):
    'display : DISPLAY graph'
    p[0]=f.displayGraph()

def p_graph(p):
    'graph : CHARACTER'
    p[0] = p[1]

def p_file(p) :
    'file : CHARACTER DOT CHARACTER'
    p[0] = p[1],p[2],p[3]
def p_node(p) :
    'node : CHARACTER'
    p[0] = p[1]

def p_term(p) :
    '''term : add
            | remove
            | display
            | file
            | graph
            | create'''
    p[0] = p[1]

def p_error(p):
    print("Syntax error in provided code! ", s)


parser = yacc.yacc()
option= input('Test file interaction?(Y/N)')
if(option=='Y'):
    import fileTesting
while True:
   try:
       s = input('BEAR> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   if(result):
    print('Success! Code supplied: ', s)
   #print(result)