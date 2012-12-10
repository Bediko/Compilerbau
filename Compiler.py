#!/usr/bin/python
# -*- coding: utf-8 -*-

from lexi import lexical_analyze
from syntax import syntax_analyze
from pyTree import Tree as T

f = open('program')
file_input = f.read()
tokens = lexical_analyze(file_input)
print("Lexial done")
syntree = syntax_analyze(tokens)
print("Syntax done")
