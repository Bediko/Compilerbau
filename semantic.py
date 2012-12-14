
sym = []


def iterate(st, scope):
    item = str(st)
    if item == 'procedure':
        scope = str(st.getNode("proc_name").getChild(0).getChild(0))

    elif item == "identifier":
        if str(st.getParent().getParent()) != "procedure":
            for e in sym:
                if e["scope"] == scope:
                    if e["name"] == str(st.getChild(0)):
                        break
                elif e["type"] == "procedure":
                    if e["name"] == str(st.getChild(0)):
                        break
            else:
                st.getParent().getParent().prettyTree()
                print("Variable used without declaration: " + str(st.getChild(0)))

    for i in range(0, len(st.getChildren())):
        try:
            iterate(st.getChild(i), scope)
        except IndexError:
            return


def semantic_analyze(syntree, symboltable):
    global sym
    sym = symboltable
    iterate(syntree.getChild(0), "global")
