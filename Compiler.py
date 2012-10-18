#!/usr/bin/python
lexi=[]
def striplist(l):
    return([x.strip('\t') for x in l])
def lex(program):
    word = ""
    for c in program:
        if(c == " " or c == "\n"):
            if(word == "program"):
                lexi.append({word:"program"})
                word = ""
            elif(word == "procedure"):
                lexi.append({word:"procedure"})
                word = ""
            elif(word == "parameter"):
                lexi.append({word:"parameter"})
                word = ""
            elif(word == "integer"):
                lexi.append({word:"integer"})
                word = ""
            elif(word == "string"):
                lexi.append({word:"string"})
                word = ""
            elif(word == "in"):
                lexi.append({word:"in"})
                word = ""
            elif(word == "out"):
                lexi.append({word:"out"})
                word = ""
            elif(word == "inout"):
                lexi.append({word:"inout"})
                word = ""
            elif(word == "end"):
                lexi.append({word:"end"})
                word = ""
            elif(word == "declaration"):
                lexi.append({word:"declaration"})
                word = ""
            elif(word[0].isdigit() == False and word[0] != "\""):
                lexi.append({word:"identifier"})
                word = ""
            elif(word.isdigit() or word[0] == "\""):
                lexi.append({word:"constant"})
                word = ""
        else:
            word += c
            
f = open("program")
file_input = f.read()
file_input = file_input.splitlines(True)
file_input = striplist(file_input)
file_input = "".join(file_input)

lex(file_input)
print file_input
print lexi
