#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


def tokenizer(scanner, token):
    return (token.upper(), token)


def identifier(scanner, token):
    return ('IDENTIFIER', token)


def constant(scanner, token):
    return ('CONSTANT', token)


def digit(scanner, token):
    return ('DIGIT', token)


scanner = re.Scanner([
    (r"main\b", tokenizer),
    (r"procedure\b", tokenizer),
    (r"program\b", tokenizer),
    (r"end\b", tokenizer),
    (r"#.*", None),
    (r"parameter\b", tokenizer),
    (r"integer\b", tokenizer),
    (r"string\b", tokenizer),
    (r"input\b", tokenizer),
    (r"inout\b", tokenizer),
    (r"in\b", tokenizer),
    (r"out\b", tokenizer),
    (r"declaration\b", tokenizer),
    (r"exitloop\b", tokenizer),
    (r"print\b", tokenizer),
    (r"set\b", tokenizer),
    (r"add\b", tokenizer),
    (r"sub\b", tokenizer),
    (r"conctat\b", tokenizer),
    (r"call\b", tokenizer),
    (r"[(]", tokenizer),
    (r"[)]$", tokenizer),
    (r"loop\b", tokenizer),
    (r"case\b", tokenizer),
    (r"when\b", tokenizer),
    (r"otherwise\b", tokenizer),
    (r"less\b", tokenizer),
    (r"equal\b", tokenizer),
    (r"greater\b", tokenizer),
    (r'["].*["]', constant),
    (r"[0-9]+", constant),
    (r"[A-Za-z][A-Za-z0-9]+", identifier),
    (r"\s", None),
    ])


def lexical_analyze(file_input):
    tokens = []
    remainders = ''

    file_input = str(file_input.replace('\t', ''))
    file_input = file_input.splitlines()
    codeline = 1
    for line in file_input:
        line = line.strip()
        (tokenline, remainder) = scanner.scan(line)

        if remainder != '':
            print 'Unknown sequence in line: ' + line
            exit(0)
        for token in tokenline:
            token += (codeline,)
            tokens.append(token)
        codeline += 1
    # for token in tokens:
    #  print token

    # print remainders
    return tokens
