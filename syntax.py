#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyTree import Tree as T

code = ''
statements = ["PRINT", "INPUT", "SET", "ADD", "SUB", "CONCAT", "CALL"]
operands = ["CONSTANT", "IDENTIFIER"]
integer_operators = ["ADD", "SUB"]
log_operators = ["LESS", "GREATER", "EQUAL"]
controlflows = ["EXITLOOP", "LOOP", "CASE", "PRINT", "INPUT", "SET", "ADD", "SUB", "CONCAT", "CALL"]


def pop(tokens):
    tokens.pop(0)
    return tokens


def program_token(tokens, parent):
    child = T.Tree("program")
    parent.addChild(child)
    parent = child
    tokens = pop(tokens)
    while True:
        if tokens[0][0] != "PROCEDURE":
            break
        else:
            tokens = procedure_token(tokens, child)
    if tokens[0][0] == 'MAIN':
        tokens = main_token(tokens, child)
    else:
        unknown_token(tokens)
    if tokens[0][0] == 'END':
        child = T.Tree("end")
        parent.addChild(child)
        tokens = pop(tokens)
    else:
        unknown_token(tokens)
    return tokens


def main_token(tokens, parent):
    tokens = pop(tokens)
    child = T.Tree("main")
    parent.addChild(child)
    if tokens[0][0] == 'IDENTIFIER':
        tokens = proc_name_token(tokens, child)
    else:
        unknown_token(tokens)
    return tokens


def procedure_token(tokens, parent):
    tokens = pop(tokens)
    child = T.Tree("procedure")
    parent.addChild(child)
    parent = child
    if tokens[0][0] == 'IDENTIFIER':
        tokens = proc_name_token(tokens, child)
    else:
        unknown_token(tokens)
    if tokens[0][0] == 'PARAMETER':
        tokens = parameter_token(tokens, child)
    else:
        unknown_token(tokens)
    if tokens[0][0] == 'DECLARATION':
        tokens = declaration_token(tokens, child)
    else:
        unknown_token(tokens)
    while tokens[0][0] in controlflows:
        tokens = controlflow_token(tokens, child)
    if tokens[0][0] == "END":
        child = T.Tree("end")
        parent.addChild(child)
        tokens = pop(tokens)
    else:
        unknown_token(tokens)
    return tokens


def proc_name_token(tokens, parent):
    child = T.Tree("proc_name")
    parent.addChild(child)
    tokens = identifier_token(tokens, child)
    return tokens


def parameter_token(tokens, parent):
    tokens = pop(tokens)
    child = T.Tree("parameter")
    parent.addChild(child)
    parent = child
    while tokens[0][0] == 'IDENTIFIER':
        tokens = pvar_token(tokens, child)
    if tokens[0][0] == 'END':
        child = T.Tree("end")
        parent.addChild(child)
        tokens = pop(tokens)
    else:
        unknown_token(tokens)
    return tokens


def pvar_token(tokens, parent):
    child = T.Tree("pvar")
    parent.addChild(child)
    tokens = var_name_token(tokens, child)
    if tokens[0][0] == 'INTEGER':
        child = T.Tree("integer")
        parent.addChild(child)
        parent = child
        tokens = pop(tokens)
        if tokens[0][0] == 'IN':
            child = T.Tree("in")
            parent.addChild(child)
            tokens = pop(tokens)
        elif tokens[0][0] == 'OUT':
            child = T.Tree("out")
            parent.addChild(child)
            tokens = pop(tokens)
        elif tokens[0][0] == 'INOUT':
            child = T.Tree("inout")
            parent.addChild(child)
            tokens = pop(tokens)
        else:
            unknown_token(tokens)
    elif tokens[0][0] == 'STRING':
        child = T.Tree("string")
        parent.addChild(child)
        parent = child
        tokens = pop(tokens)
        if tokens[0][0] == 'IN':
            child = T.Tree("in")
            parent.addChild(child)
            tokens = pop(tokens)
        elif tokens[0][0] == 'OUT':
            child = T.Tree("out")
            parent.addChild(child)
            tokens = pop(tokens)
        elif tokens[0][0] == 'INOUT':
            child = T.Tree("inout")
            parent.addChild(child)
            tokens = pop(tokens)
        else:
            unknown_token(tokens)
    else:
        unknown_token(tokens)
    return tokens


def var_name_token(tokens, parent):
    child = T.Tree("var_name")
    parent.addChild(child)
    tokens = identifier_token(tokens, child)
    return tokens


def declaration_token(tokens, parent):
    tokens = pop(tokens)
    child = T.Tree("declaration")
    parent.addChild(child)
    parent = child
    while tokens[0][0] != "END":
        tokens = var_token(tokens, child)
    tokens = pop(tokens)
    child = T.Tree("end")
    parent.addChild(child)
    return tokens


def var_token(tokens, parent):
    child = T.Tree("var")
    parent.addChild(child)
    parent = child
    if tokens[0][0] == "IDENTIFIER":
        tokens = var_name_token(tokens, child)
    if tokens[0][0] == "INTEGER":
        child = T.Tree("integer")
        parent.addChild(child)
        tokens = pop(tokens)
    elif tokens[0][0] == "STRING":
        child = T.Tree("string")
        parent.addChild(child)
        tokens = pop(tokens)
    else:
        unknown_token(tokens)
    return tokens


def controlflow_token(tokens, parent):
    child = T.Tree("controlflow")
    parent.addChild(child)
    parent = child
    if tokens[0][0] == "EXITLOOP":
        child = T.Tree("exitloop")
        parent.addChild(child)
        tokens = pop(tokens)
    elif tokens[0][0] == "LOOP":
        tokens = loop_token(tokens, child)
    elif tokens[0][0] == "CASE":
        tokens = case_token(tokens, child)
    elif tokens[0][0] in statements:
        tokens = statement_token(tokens, child)
    else:
        unknown_token(tokens)
    return tokens


def statement_token(tokens, parent):
    child = T.Tree("statement")
    parent.addChild(child)
    if tokens[0][0] == "PRINT":
        tokens = print_stmt_token(tokens, child)
    elif tokens[0][0] == "INPUT":
        tokens = input_stmt_token(tokens, child)
    elif tokens[0][0] == "SET":
        tokens = assign_stmt_token(tokens, child)
    elif tokens[0][0] in integer_operators:
        tokens = integer_operation_token(tokens, child)
    elif tokens[0][0] == "CONCAT":
        tokens = string_operation_token(tokens, child)
    elif tokens[0][0] == "CALL":
        tokens = call_stmt_token(tokens, child)
    else:
        unknown_token(tokens)
    return tokens


def print_stmt_token(tokens, parent):
    child = T.Tree("printstm")
    parent.addChild(child)
    tokens = pop(tokens)
    if tokens[0][0] in operands:
        tokens = local_var_token(tokens, child)
    else:
        unknown_token(tokens)
    return tokens


def input_stmt_token(tokens, parent):
    child = T.Tree("inputstm")
    parent.addChild(child)
    tokens = pop(tokens)
    if tokens[0][0] == "CONSTANT":
        tokens = prompt_token(tokens, child)
    else:
        unknown_token(tokens)
    if tokens[0][0] == "IDENTIFIER":
        tokens = local_var_token(tokens, child)
    else:
        unknown_token(tokens)
    return tokens


def prompt_token(tokens, parent):
    child = T.Tree("prompt")
    parent.addChild(child)
    tokens = constant_token(tokens, child)
    return tokens


def assign_stmt_token(tokens, parent):
    child = T.Tree("assignstm")
    parent.addChild(child)
    tokens = pop(tokens)
    if tokens[0][0] == "IDENTIFIER":
        tokens = result_var_token(tokens, child)
    else:
        unknown_token(tokens)
    if tokens[0][0] in operands:
        tokens = operand_token(tokens, child)
    else:
        unknown_token(tokens)
    return tokens


def local_var_token(tokens, parent):
    child = T.Tree("localvar")
    parent.addChild(child)
    if tokens[0][0] == "IDENTIFIER":
        tokens = identifier_token(tokens, child)
    elif tokens[0][0] == "CONSTANT":
        tokens = constant_token(tokens, child)
    else:
        unknown_token(tokens)
    return tokens


def integer_operation_token(tokens, parent):
    child = T.Tree("integeroperation")
    parent.addChild(child)
    tokens = integer_operator_token(tokens, child)
    if tokens[0][0] in operands:
        tokens = result_var_token(tokens, child)
    else:
        unknown_token(tokens)
    if tokens[0][0] in operands:
        tokens = operand1_token(tokens, child)
    else:
        unknown_token(tokens)
    if tokens[0][0] in operands:
        tokens = operand2_token(tokens, child)
    else:
        unknown_token(tokens)
    return tokens


def string_operation_token(tokens, parent):
    child = T.Tree("stringoperation")
    parent.addChild(child)
    tokens, parent = string_operator_token(tokens, parent)
    if tokens[0][0] == "IDENTIFIER":
        tokens, parent = result_var_token(tokens, parent)
    else:
        unknown_token(tokens)
    if tokens[0][0] in operands:
        tokens, parent = operand1_token(tokens, parent)
    else:
        unknown_token(tokens)
    if tokens[0][0] in operands:
        tokens, parent = operand2_token(tokens, parent)
    else:
        unknown_token(tokens)
    return tokens, parent


def integer_operator_token(tokens, parent):
    child = T.Tree("integeroperator")
    parent.addChild(child)
    parent = child
    if tokens[0][0] == "ADD":
        child = T.Tree("add")
        parent.addChild(child)
        tokens = pop(tokens)
    elif tokens[0][0] == "SUB":
        child = T.Tree("sub")
        parent.addChild(child)
        tokens = pop(tokens)
    else:
        unknown_token(tokens)
    return tokens


def string_operator_token(tokens, parent):
    child = T.Tree("string_operator")
    parent.addChild(child)
    parent = child
    child = T.Tree("concat")
    parent.addChild(child)
    tokens = pop(tokens)
    return tokens


def result_var_token(tokens, parent):
    child = T.Tree("resultvar")
    parent.addChild(child)
    tokens = identifier_token(tokens, child)
    return tokens


def call_stmt_token(tokens, parent):
    tokens = pop(tokens)
    child = T.Tree("callstm")
    parent.addChild(child)
    if tokens[0][0] == "IDENTIFIER":
        tokens = identifier_token(tokens, child)
    else:
        unknown_token(tokens)
    if tokens[0][0] == "(":
        tokens = pop(tokens)
    else:
        unknown_token(tokens)
    while tokens[0][0] != ")":
        tokens = actualparameter_token(tokens, child)
    tokens = pop(tokens)
    return tokens


def actualparameter_token(tokens, parent):
    child = T.Tree("actualparameter")
    parent.addChild(child)
    tokens = local_var_token(tokens, child)
    return tokens


def loop_token(tokens, parent):
    child = T.Tree("loop")
    parent.addChild(child)
    parent = child
    tokens = pop(tokens)
    while tokens[0][0] != "END":
        tokens = controlflow_token(tokens, child)
    child = T.Tree("end")
    parent.addChild(child)
    tokens = pop(tokens)
    return tokens


def case_token(tokens, parent):
    child = T.Tree("case")
    parent.addChild(child)
    parent = child
    tokens = pop(tokens)
    while True:
        if tokens[0][0] != "WHEN":
            break
        else:
            tokens = when_token(tokens, child)
    if tokens[0][0] == "OTHERWISE":
        tokens = otherwise_token(tokens, child)
    if tokens[0][0] == "END":
        child = T.Tree("end")
        parent.addChild(child)
        tokens = pop(tokens)
    else:
        unknown_token(tokens)
    return tokens


def when_token(tokens, parent):
    child = T.Tree("when")
    parent.addChild(child)
    tokens = pop(tokens)
    if tokens[0][0] in log_operators:
        tokens = expression_token(tokens, child)
    else:
        unknown_token(tokens)
    while tokens[0][0] in controlflows:
        tokens = controlflow_token(tokens, child)
    return tokens


def otherwise_token(tokens, parent):
    child = T.Tree("otherwise")
    parent.addChild(child)
    tokens = pop(tokens)
    while tokens in controlflows:
        tokens = controlflow_token(tokens, child)
    return tokens


def expression_token(tokens, parent):
    child = T.Tree("expression")
    parent.addChild(child)
    if tokens[0][0] in log_operators:
        tokens = log_operator_token(tokens, child)
    else:
        unknown_token(tokens)
    if tokens[0][0] in operands:
        tokens = operand1_token(tokens, child)
    else:
        unknown_token(tokens)
    if tokens[0][0] in operands:
        tokens = operand2_token(tokens, child)
    else:
        unknown_token(tokens)
    return tokens


def log_operator_token(tokens, parent):
    child = T.Tree("logoperator")
    parent.addChild(child)
    parent = child
    if tokens[0][0] == "LESS":
        child = T.Tree("less")
        parent.addChild(child)
        tokens = pop(tokens)
    elif tokens[0][0] == "EQUAL":
        child = T.Tree("equal")
        parent.addChild(child)
        tokens = pop(tokens)
    elif tokens[0][0] == "GREATER":
        child = T.Tree("greater")
        parent.addChild(child)
        tokens = pop(tokens)
    else:
        unknown_token(tokens)
    return tokens


def operand1_token(tokens, parent):
    child = T.Tree("operand1")
    parent.addChild(child)
    tokens = operand_token(tokens, child)
    return tokens


def operand2_token(tokens, parent):
    child = T.Tree("operand2")
    parent.addChild(child)
    tokens = operand_token(tokens, child)
    return tokens


def operand_token(tokens, parent):
    child = T.Tree("operand")
    parent.addChild(child)
    if tokens[0][0] == "IDENTIFIER":
        tokens = identifier_token(tokens, child)
    elif tokens[0][0] == "CONSTANT":
        tokens = constant_token(tokens, child)
    else:
        unknown_token(tokens)
    return tokens


def constant_token(tokens, parent):
    child = T.Tree("constant")
    parent.addChild(child)
    return pop(tokens)


def identifier_token(tokens, parent):
    child = T.Tree("identifier")
    parent.addChild(child)
    return pop(tokens)


def unknown_token(tokens):
    print('Unknown token: ' + tokens[0][1] + ' on line ' \
        + "".join(tokens[0][2]))
    exit(0)


def syntax_analyze(tokens):

    if tokens[0][0] == 'PROGRAM':
        syntree = T.Tree('root')
        tokens = program_token(tokens, syntree)
    else:
        unknown_token(tokens)
    syntree.prettyTree()
    return syntree
