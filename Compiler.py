#!/usr/bin/python
# -*- coding: utf-8 -*-

from lexi import lexical_analyze
from syntax import syntax_analyze
from semantic import semantic_analyze
from generation import generate_code

f = open('program')
file_input = f.read()
tokens = lexical_analyze(file_input)
#    for token in tokens:
#        print token#
print("Lexial done")
syntree, symboltable = syntax_analyze(tokens)
syntree.prettyTree()
#for e in symboltable:
#    print (e)
print("Syntax done")
semantic_analyze(syntree, symboltable)
print("Semantics done")
code = generate_code(syntree, symboltable)
