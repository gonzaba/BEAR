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
def t_ID(t):
    r'[a-zA-Z0-9-_]+'
    if t.value in reserved:
         t.type = reserved[t.value]
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
               | FOR LSLASHES term IN term RSLASHES function
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
    p[0]= 'removed ', p[3]

def p_display(p):
    'display : DISPLAY graph'
    p[0]=f.displayGraph()

def p_graph(p):
    'graph : CHARACTER'
    p[0] = p[1]

def p_file(p) :
    'file : ID DOT CHARACTER'
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


"""
HONEY class for auxiliary functions
User must input data as specified in order to comply with data types
newNetwork
    name is a string
addPerson
    g is a graph
    name, gender are string
    age, grade are int
    vax, infect are bool
editPerson
    g is a graph
    p is a node
    att is a string
    val is a free type value
    ######SHOULD VERIFY VALID ATTRIBUTE######
addConnection
    g is a graph
    p1, p2 are node
addLink
    g is a graph
    p1, p2 are node
    att is a string
    val is a free type value
"""

class Honey:
    # adding a new network
    def newNetwork(self,name):
        self = nx.DiGraph()
        self.graph['name']=name

    # methods for persons
    def addPerson(self,g,name,age,gender,grade,vax,infect):
        g.add_node(name)
        g.node[name]['name']=name
        g.node[name]['age']=age
        g.node[name]['gender']=gender
        g.node[name]['grade']=grade
        g.node[name]['vaccinated']=vax
        g.node[name]['infected']=infect
    def editPerson(self,g,p,att,val):
        g.node[p][att]=val

    # methods for connections
    def addConnection(self,g,p1,p2):
        g.add_edge(p1,p2)
    def addLink(self,g,p1,p2,att,val):
        g[p1][p2][att]=val

#TODO: Add auxiliary operations!
parser = yacc.yacc()
option= input('Test file interaction?(Y/N)')
if(option=='Y'):
    import fileTester
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
