def traverse_tree(st):

    if str(st) == 'program':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'main':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'procedure':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            print (i)
            name = traverse_tree(st.getChild(i))
            if name != None:
                print(name)
        return
    elif str(st) == 'proc_name':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            name = traverse_tree(st.getChild(i))
            return name
        return
    elif str(st) == 'parameter':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'pvar':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'var_name':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'declaration':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'var':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'controlflow':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'statement':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'printstm':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'inputstm':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'assignstm':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'localvar':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'integeroperation':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'stringoperation':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'integeroperator':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'stringoperator':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'resultvar':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'callstm':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'actualparameter':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'loop':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'case':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'when':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'otherwise':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'expression':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'logoperator':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'operand1':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'operand2':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'operand':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'identifier':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            name = (st.getChild(i))
            return str(name)
        return
    elif str(st) == 'prompt':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    elif str(st) == 'end':
        for i in range(len(st.getChildren()) - 1, -1, -1):
            traverse_tree(st.getChild(i))
        return
    else:
        return


def generate_code(syntree, symboltable):
    traverse_tree(syntree.getChild(0))
    return
