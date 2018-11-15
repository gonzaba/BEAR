# -----------------------------------------------------------------------------
# BEAR - Version 0.01a
#
# Social Network Analysis Language.
# -----------------------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt
import ply.lex as lex
import Files

#lex part
reserved = {
    '//' : 'LSLASHES',
    '\\\\' : 'RSLASHES',
    'Bear' : 'BEAR',
    'if' : 'IF',
    'else': 'ELSE',
    'for' : 'FOR'
}
tokens = [
    'DIGIT',
    'CHARACTER',
    'ID',
    'LPAREN',
    'RPAREN',
    'DELIMITER',
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
t_BINARY = r'\||&&'
t_DELIMITER = r'\['

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
# yacc part
# Parser
import ply.yacc as yacc
# THIS PART IS HIGHLY WIP FOR NOW. IT'S UNRELIABLE! ~Enrique
#def p_add(p):
 #   '''node + [ file , node ] '''
#def p_define(p):
 #   '''  'BEAR' ~ function '''

precedence = (
    ('left', 'LSLASHES', 'RSLASHES'),
    ('left', 'LPAREN', 'RPAREN')
)

def p_test(p):
    'test : BEAR LSLASHES function RSLASHES'
    #= ^p[0]   ^p[1]
    #treat p as if it were a list; each separate word is a cell in the list.
    p[0]= p[3]


#underlying parser rules come before anything else, since they establish what the following rules will follow.
#Hierarchy goes top to bottom. ~Enrique
def p_function(p):
    '''function : DIGIT
               | CHARACTER
               | BINARY
               | DELIMITER
               | ID
               | LPAREN
               | RPAREN
               | LSLASHES
               | RSLASHES '''
    p[0]= p[1]



def p_error(p):
    print('Syntax error in input!')





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
# hola
# HI

filename=input("Welcome to BEAR! Please enter your code's filename to compile. (NOTE: file must be in .cub format): \n")
if(not filename.__contains__('.cub')):
    print("unsupported file format!")
print(filename)

parser = yacc.yacc()

while True:
   try:
       s = input('>> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)