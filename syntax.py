#!/usr/bin/python
# -*- coding: utf-8 -*-


def pop(tokens):
    tokens.pop(0)
    return tokens


def main_token(tokens):
    print tokens[0]


def procedure_token(tokens):
    print tokens[0]
    if tokens[0][0] == 'IDENTIFIER':
        tokens = identifier_token(pop(tokens))
        return tokens
    else:
        print 'Unknown token: ' + tokens[0][1] + ' on line ' \
            + str(tokens[0][2])
        exit(0)


def program_token(tokens):
    while tokens[0][0] == 'PROCEDURE':
        tokens = procedure_token(pop(tokens))
    if tokens[0][0] == 'MAIN':
        main_token(pop(tokens))
    else:
        print 'Unknown token: ' + tokens[0][1] + ' on line ' \
            + str(tokens[0][2])
        exit(0)


# def end_token(tokens):
# def parameter_token(tokens):
# def integer_token(tokens):
# def string_token(tokens):
# def input_token(tokens):
# def inout_token(tokens):
# def in_token(tokens):
# def out_token(tokens):
# def declaration_token(tokens):
# def exitloop_token(tokens):
# def print_token(tokens):
# def set_token(tokens):
# def add_token(tokens):
# def sub_token(tokens):
# def conctat_token(tokens):
# def call_token(tokens):
# def langle_token(tokens):
# def rangle_token(tokens):
# def loop_token(tokens):
# def case_token(tokens):
# def when_token(tokens):
# def otherwise_token(tokens):
# def less_token(tokens):
# def equal_token(tokens):
# def greater_token(tokens):
# def constant_token(tokens):
# def digit_token(tokens):

def identifier_token(tokens):
    if tokens[0][0] == 'IDENTIFIER':
        return pop(tokens)
    else:
        print 'Unknown token: ' + tokens[0][1] + ' on line ' \
            + str(tokens[0][2])


def syntax_analyze(tokens):
    code = ''
    if tokens[0][0] == 'PROGRAM':
        program_token(pop(tokens))
    else:
        print 'Unknown token: ' + tokens[0][1] + ' on line ' \
            + str(tokens[0][2])

    return code
