# -----------------------------------------------------------------------------
# BEAR - Version 0.01a
#
# Social Network Analysis Language.
# -----------------------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt
import ply.lex as lex

tokens = ( 'ADD' , 'DEFINE' , 'FILE' , 'FUNCTION' , 'DISPLAY' , 'DIGIT' , 'CHARACTER' , 'DELIMITERS' )

#Tokens

t_DIGIT = r'[0-9]+'
t_CHARACTER = r'[a-zA-Z-_.]+'
t_DELIMITERS= '//' | '\\' | '|' | '(' | ')' | '[' | ']' | '{' | '}'


# Ignore tabs
t_ignore = " \t"
G= nx.Graph()
G.add_nodes_from([1,5])
print (list(G.nodes))


# hola
# HI