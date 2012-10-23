#!/usr/bin/python
import re
def main(scanner,token): return "MAIN"
def identifier(scanner,token): return "IDENTIFIER", token
def program(scanner,token): return "PROGRAM"
def procedure(scanner,token): return "PROCEDURE"
def end(scanner,token): return "END"
def comment(scanner,token): return "COMMENT", token
def parameter(scanner,token): return "PARAMETER"
def integer(scanner,token): return "INTEGER"
def string(scanner,token): return "STRING"
def in_lex(scanner, token): return "IN"
def out_lex(scanner, token): return "OUT"
def inout(scanner, token): return "INOUT"
def declaration(scanner, token): return "DECLARATION"
def exitloop(scanner, token): return "EXITLOOP"
def print_lex(scanner, token): return "PRINT"
def input_lex(scanner, token): return "INPUT"
def set_lex(scanner, token): return "SET"
def add(scanner, token): return "ADD"
def sub(scanner, token): return "SUB"
def concat(scanner, token): return "CONCAT"
def call(scanner, token): return "CALL"
def langle(scanner, token): return "("
def rangle(scanner, token): return ")"
def loop(scanner, token): return "LOOP"
def case(scanner, token): return "CASE"
def when(scanner, token): return "WHEN"
def otherwise(scanner, token): return "OTHERWISE"
def less(scanner, token): return "LESS"
def equal(scanner, token): return "EQUAL"
def greater(scanner, token): return "GREATER"
def constant(scanner, token): return "CONSTANT", token
def digit(scanner, token): return "DIGIT", token


scanner = re.Scanner([
    (r"main", main),
    (r"procedure", procedure),
    (r"program", program),
    (r"end", end),
    (r"#.*", comment),
    (r"parameter", parameter),
    (r"integer", integer),
    (r"string", string),
    (r"input", input_lex),
    (r"inout", inout),
    (r"in", in_lex),
    (r"out", out_lex),
    (r"declaration", declaration),
    (r"exitloop", exitloop),
    (r"print", print_lex),
    (r"set", set_lex),
    (r"add", add),
    (r"sub", sub),
    (r"conctat", concat),
    (r"call",call),
    (r"[(]", langle),
    (r"[)]", rangle),
    (r"loop",loop),
    (r"case", case),
    (r"when", when),
    (r"otherwise", otherwise),
    (r"less", less),
    (r"equal", equal),
    (r"greater",greater),
    (r'["].*["]',constant),
    (r"[0-9]+", digit),
    (r"\s",None),
    (r"[A-Za-z][A-Za-z0-9]+", identifier),
    ])
tokens = []
remainders = ""
f = open("program")
file_input = f.read()
file_input = str(file_input.replace("\t",""))
file_input = file_input.splitlines();

for line in file_input:
    line = line.strip()
    tokenline, remainder = scanner.scan(line)
    remainders+=remainder
    for token in tokenline:
        tokens.append(token)

for token in tokens:
    print token

print remainders
