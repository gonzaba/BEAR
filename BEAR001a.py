# -----------------------------------------------------------------------------
# BEAR - Version 0.01a
#
# Social Network Analysis Language.
# -----------------------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt
import ply.lex as lex

tokens = ('DIGIT' , 'CHARACTER' , 'DELIMITERS' )

#Tokens

t_DIGIT = r'[0-9]+'
t_CHARACTER = r'[a-zA-Z-_.]+'

# Delimiters unimplemented for now, checking for a solution... ~Enrique
# t_DELIMITERS= '//' | '\\' | '|' | '(' | ')' | '[' | ']' | '{' | '}'

# Parser
import ply.yacc as yacc
# THIS PART IS HIGHLY WIP FOR NOW. IT'S UNRELIABLE! ~Enrique
def p_add(p):
    '''node + [ file , node ] '''
def p_define(p):
    '''  'BEAR' ~ function '''
# Ignore tabs
t_ignore = " \t"
filename=input("Welcome to BEAR! Please enter your code's filename to compile. (NOTE: file must be in .cub format): \n")
if(not filename.__contains__('.cub')):
    print("unsupported file format!")
print(filename)

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

    # method to add person
    def addPerson(self,g,name,age,gender,grade,vax,infect):
        g.add_node(name)
        g.node[name]['name']=name
        g.node[name]['age']=age
        g.node[name]['gender']=gender
        g.node[name]['grade']=grade
        g.node[name]['vaccinated']=vax
        g.node[name]['infected']=infect

    # methods for connections
    def addConnection(self,g,p1,p2):
        g.add_edge(p1,p2)
    def addLink(self,g,p1,p2,att,val):
        g[p1][p2][att]=val

#TODO: Add auxiliary operations!
# hola
# HI