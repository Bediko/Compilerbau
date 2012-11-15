#!/usr/bin/python
# -*- coding: utf-8 -*-

code = ''


def pop(tokens):
    tokens.pop(0)
    return tokens


def main_token(tokens):
    tokens = pop(tokens)
    if tokens[0][0] == 'IDENTIFIER':
        tokens = proc_name_token(tokens)
    else:
        print 'Unknown token: ' + tokens[0][1] + ' on line ' \
            + str(tokens[0][2])
        exit(0)


def procedure_token(tokens):
    tokens = pop(tokens)
    if tokens[0][0] == 'IDENTIFIER':
        tokens = proc_name_token(tokens)
    if tokens[0][0] == 'PARAMETER':
        tokens = parameter_token(tokens)
    if tokens[0][0] == 'DECLARATION':

        # tokens = declaration_token(tokens)

        tokens = pop(tokens)
    else:
        print 'Unknown token: ' + tokens[0][1] + ' on line ' \
            + str(tokens[0][2])
        exit(0)
    while tokens[0][0] != 'END':
        print tokens[0]
        # tokens = control_flow_token(tokens)
        tokens = pop(tokens)
    if tokens[0][0] == "END":
        tokens = end_token(tokens)
    return tokens


def program_token(tokens):
    tokens = pop(tokens)
    while tokens[0][0] == 'PROCEDURE':
        tokens = procedure_token(tokens)
    if tokens[0][0] == 'MAIN':
        tokens = main_token(tokens)
    if tokens[0][0] == 'END':
        tokens = end_token(tokens)
        return tokens
    else:
        print 'Unknown token: ' + tokens[0][1] + ' on line ' \
            + str(tokens[0][2])
        exit(0)


def end_token(tokens):
    return pop(tokens)


def parameter_token(tokens):
    tokens = pop(tokens)
    while tokens[0][0] == 'IDENTIFIER':
        tokens = pvar_token(tokens)
    if tokens[0][0] == 'END':
        tokens = end_token(tokens)
    else:
        print 'Unknown token: ' + tokens[0][1] + ' on line ' \
            + str(tokens[0][2])
        exit(0)
    return tokens


def pvar_token(tokens):
    tokens = identifier_token(tokens)
    if tokens[0][0] == 'INTEGER':
        tokens = pop(tokens)
        if tokens[0][0] == 'IN':
            tokens = pop(tokens)
        if tokens[0][0] == 'OUT':
            tokens = pop(tokens)
        if tokens[0][0] == 'INOUT':
            tokens = pop(tokens)
    elif tokens[0][0] == 'STRING':
        tokens = pop(tokens)
        if tokens[0][0] == 'IN':
            tokens = pop(tokens)
        if tokens[0][0] == 'OUT':
            tokens = pop(tokens)
        if tokens[0][0] == 'INOUT':
            tokens = pop(tokens)
    else:
        print 'Unknown token: ' + tokens[0][1] + ' on line ' \
            + str(tokens[0][2])
    return tokens


def proc_name_token(tokens):
    tokens = identifier_token(tokens)
    return tokens


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
    return pop(tokens)


def syntax_analyze(tokens):
    if tokens[0][0] == 'PROGRAM':
        program_token(tokens)
    else:
        print 'Unknown token: ' + tokens[0][1] + ' on line ' \
            + str(tokens[0][2])

    return code
