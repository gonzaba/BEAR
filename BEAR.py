# -----------------------------------------------------------------------------
# BEAR - Version 0.01a
#
# Social Network Analysis Language.
# -----------------------------------------------------------------------------

import networkx as nx
import ply.lex as lex
import ply.yacc as yacc
import HONEY as f


def help():
    print('''BEAR: The Social Network Analysis (SNA) language.\n
            Creating networks: Bear create || Bear create // nameOfGraph \\\\ || Bear create // nameOfGraph from fileName \\\\ \n 
            Adding Nodes to a Graph: Bear nameOfGraph + [ node ] || Bear nameOfGraph + [ fileName ] \n
            Removing Nodes from a Graph: Bear nameOfGraph - node \n
            Displaying a Graph: Bear display nameOfGraph \n
            Graph Operations menu: Bear nameOfGraph operations
    ''')
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
    'node'  :   'NODE',
    '-' :   'MINUS',
    '+' :   'PLUS',
    'operations'    :   'OPERATIONS',
    'create' : 'CREATE'
}
tokens = [
    'CHARACTER',
    'ID',
    'LDELIMITER',
    'RDELIMITER',
    'COMMA',
    'SEPARATOR',
    'DOT',
    'BINOP',

] + (list(reserved.values()))
t_ignore = ' '
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


t_LSLASHES = r'//'
t_RSLASHES = r'\\\\'
t_COMMA = r'\,'
t_BINOP = r'[>=|<|<=|>|!=|==]'
t_DOT = r'\.'
t_MINUS = r'-'
t_PLUS = r'\+'
t_SEPARATOR = r'\;'
t_LDELIMITER = r'\['
t_RDELIMITER = r'\]'


def t_error(t):
    print("Illegal character '%s" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
# yacc part
# Parser
#underlying parser rules come before anything else, since they establish what the following rules will follow.
#Hierarchy goes top to bottom. ~Enrique

def p_define(p):
    'define : BEAR function'
    #= ^p[0]   ^p[1]
    #treat p as if it were a list; each separate word is a cell in the list.
    p[0]= p[2]
def p_function(p):
    '''function : term
               | FOR LSLASHES term IN term RSLASHES function
               | WHILE LSLASHES term BINOP term RSLASHES term'''
    if('for' in p):
        print('for loop')
    if('while' in p):
        print("while loop")
    p[0] = p[1]

def p_add(p) :
    '''add : graph PLUS LDELIMITER file RDELIMITER
            | graph PLUS ID'''
    if(len(p)>4):
        p[0] = f.add(p[4], p[1])
    else: f.addNode(p[1], p[3])
def p_create(p):
    '''create : CREATE LSLASHES ID RSLASHES
                | CREATE LSLASHES ID FROM file RSLASHES
                | CREATE'''
    if(len(p)>6):
        p[0] = f.createGraphFromFile(p[3], p[5])
    elif(len(p)>3):
        p[0]= f.createGraph(p[3])
    else:
        p[0]= f.createNewGraph()
def p_remove(p) :
    'remove : graph MINUS node'
    p[0] = f.remove(p[3], p[1])

def p_display(p):
    'display : DISPLAY graph'
    p[0]=f.displayGraph(p[2])

def p_operations(p):
    'operations : graph OPERATIONS'
    p[0] = f.operations(p[1])

def p_graph(p):
    'graph : ID'
    p[0] = p[1]

def p_file(p) :
    'file : ID DOT ID'
    p[0] = p[1]+p[2]+p[3]
def p_node(p) :
    'node : NODE ID'
    p[0] = f.getNode(p[2])

def p_term(p) :
    '''term : add
            | remove
            | display
            | file
            | graph
            | node
            | create
            | operations'''
    p[0] = p[1]

def p_error(p):
    print('Syntax error in code provided!', s)

parser = yacc.yacc()
while True:
   try:
       s = input('BEAR> ')
   except EOFError:
       break
   if(s=="exit"):
       input('Thanks for using BEAR! Press the enter key to exit.')
       break
   if(s=='help'): help()
   if not s: continue
   result = parser.parse(s)