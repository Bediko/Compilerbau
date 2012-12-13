#!/usr/bin/python
# -*- coding: utf-8 -*-

from lexi import lexical_analyze
from syntax import syntax_analyze


f = open('program')
file_input = f.read()
tokens = lexical_analyze(file_input)
#    for token in tokens:
#        print token#
print("Lexial done")
syntree, symboltable = syntax_analyze(tokens)
childs = syntree.getChildren()
for i in range(0, len(childs)):
    syntree.getChild(i).prettyTree()
#syntree.prettyTree()
#for e in symboltable:
#    print (e)
print("Syntax done")
