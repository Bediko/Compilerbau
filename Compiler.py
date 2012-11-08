#!/usr/bin/python

import re

def tokenizer(scanner,token): return token.upper(),token
def identifier(scanner,token): return "IDENTIFIER", token
def constant(scanner, token): return "CONSTANT", token
def digit(scanner, token): return "DIGIT", token


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
    (r"call\b",tokenizer),
    (r"[(]", tokenizer),
    (r"[)]$", tokenizer),
    (r"loop\b",tokenizer),
    (r"case\b", tokenizer),
    (r"when\b", tokenizer),
    (r"otherwise\b", tokenizer),
    (r"less\b", tokenizer),
    (r"equal\b", tokenizer),
    (r"greater\b",tokenizer),
    (r'["].*["]',constant),
    (r"[0-9]+", digit),
    (r"[A-Za-z][A-Za-z0-9]+", identifier),
    (r"\s",None),
    ])
tokens = []
remainders = ""
f = open("program")
file_input = f.read()
file_input = str(file_input.replace("\t",""))
file_input = file_input.splitlines();

count =0

for line in file_input:
    count+=1
    line = line.strip()
    tokenline, remainder = scanner.scan(line)
   
    if(remainder !=""):
        print("Unknown sequence in line "+str(count)+" :"+line)
        exit(0)
    for token in tokenline:
        tokens.append(token)

for token in tokens:
    print token

print remainders
