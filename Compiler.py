#!/usr/bin/python

import re
from lexi import lex

f = open("program")
file_input = f.read()
lex(file_input)
