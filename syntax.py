#!/usr/bin/python
# -*- coding: utf-8 -*-

code = ''
statements = ["PRINT", "INPUT", "SET", "ADD", "SUB", "CONCAT", "CALL"]


def pop(tokens):
    tokens.pop(0)
    return tokens


def main_token(tokens):
    tokens = pop(tokens)
    if tokens[0][0] == 'IDENTIFIER':
        tokens = proc_name_token(tokens)
    else:
        unknown_token(tokens)
        exit(0)


def procedure_token(tokens):
    tokens = pop(tokens)
    if tokens[0][0] == 'IDENTIFIER':
        tokens = proc_name_token(tokens)
    else:
        unknown_token(tokens)
    if tokens[0][0] == 'PARAMETER':
        tokens = parameter_token(tokens)
    else:
        unknown_token(tokens)
    if tokens[0][0] == 'DECLARATION':
        tokens = declaration_token(tokens)
    else:
        unknown_token(tokens)
        exit(0)
    while tokens[0][0] != 'END':
        tokens = control_flow_token(tokens)

    tokens = end_token(tokens)
    return tokens


def program_token(tokens):
    tokens = pop(tokens)
    while tokens[0][0] == 'PROCEDURE':
        tokens = procedure_token(tokens)
    if tokens[0][0] == 'MAIN':
        tokens = main_token(tokens)
    else:
        unknown_token(tokens)
    if tokens[0][0] == 'END':
        tokens = end_token(tokens)
    else:
        unknown_token(tokens)
        exit(0)
    return tokens


def end_token(tokens):
    return pop(tokens)


def parameter_token(tokens):
    tokens = pop(tokens)
    while tokens[0][0] == 'IDENTIFIER':
        tokens = pvar_token(tokens)
    if tokens[0][0] == 'END':
        tokens = end_token(tokens)
    else:
        unknown_token(tokens)
        exit(0)
    return tokens


def pvar_token(tokens):
    tokens = var_name_token(tokens)
    if tokens[0][0] == 'INTEGER':
        tokens = pop(tokens)
        if tokens[0][0] == 'IN':
            tokens = pop(tokens)
        else:
            unknown_token(tokens)
        if tokens[0][0] == 'OUT':
            tokens = pop(tokens)
        else:
            unknown_token(tokens)
        if tokens[0][0] == 'INOUT':
            tokens = pop(tokens)
        else:
            unknown_token(tokens)
    elif tokens[0][0] == 'STRING':
        tokens = pop(tokens)
        if tokens[0][0] == 'IN':
            tokens = pop(tokens)
        else:
            unknown_token(tokens)
        if tokens[0][0] == 'OUT':
            tokens = pop(tokens)
        else:
            unknown_token(tokens)
        if tokens[0][0] == 'INOUT':
            tokens = pop(tokens)
        else:
            unknown_token(tokens)
    else:
        unknown_token(tokens)
    return tokens


def proc_name_token(tokens):
    tokens = identifier_token(tokens)
    return tokens


def var_name_token(tokens):
    tokens = identifier_token(tokens)
    return tokens


def declaration_token(tokens):
    tokens = pop(tokens)
    while tokens[0][0] != "END":
        tokens = var_token(tokens)
    tokens = pop(tokens)
    return tokens


def var_token(tokens):
    if tokens[0][0] == "IDENTIFIER":
        tokens = var_name_token(tokens)
    if tokens[0][0] == "INTEGER":
        tokens = pop(tokens)
    elif tokens[0][0] == "STRING":
        tokens = pop(tokens)
    else:
        unknown_token(tokens)
    return tokens


def controlflow_token(tokens):
    if tokens[0][0] == "EXITLOOP":
        tokens = exitloop_token(tokens)
    elif tokens[0][0] == "LOOP":
        tokens = loop_token(tokens)
    elif tokens[0][0] == "CASE":
        tokens = case_token(tokens)
    elif tokens[0][0] in statements:
        tokens = statement_token(tokens)
    else:
        unknown_token(tokens)
    return tokens


def statement_token(tokens):
    if tokens[0][0] == "PRINT":
        tokens = print_stmt_token(tokens)
    elif tokens[0][0] == "INPUT":
        tokens = input_stmt_token(tokens)
    elif tokens[0][0] == "SET":
        tokens = assign_stmt_token(tokens)
    elif tokens[0][0] == "ADD" or tokens[0][0] == "SUB":
        tokens = integer_operation_token(tokens)
    elif tokens[0][0] == "CONCAT":
        tokens = string_operation_token(tokens)
    elif tokens[0][0] == "CALL":
        tokens = call_stmt_token(tokens)
    else:
        unknown_token(tokens)
    return tokens


def exitloop_token(tokens):
    return pop(tokens)


#def print_token(tokens):
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


def unknown_token(tokens):
    print 'Unknown token: ' + tokens[0][1] + ' on line ' \
        + str(tokens[0][2])
    exit(0)


def syntax_analyze(tokens):
    if tokens[0][0] == 'PROGRAM':
        program_token(tokens)
    else:
        unknown_token(tokens)

    return code
