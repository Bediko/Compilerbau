#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from lexi import lexical_analyze
from syntax import syntax_analyze

f = open('program')
file_input = f.read()
tokens = lexical_analyze(file_input)
code = syntax_analyze(tokens)
