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

# HONEY class for auxiliary functions
# class Honey (object):
    #TODO: Add auxiliary operations!
# hola
# HI