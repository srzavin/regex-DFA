def infix_to_postfix(infix):

    operators = {"|": 1, ".": 2, "*": 3, "(": 4, ")": 4}


    tokens = []
    i = 0
    while i < len(infix):
        if infix[i].isdigit() or infix[i].isalpha():

            j = i + 1
            while j < len(infix) and (infix[j].isdigit() or infix[j].isalpha()):
                j += 1
            tokens.append(infix[i:j])
            i = j
        else:

            tokens.append(infix[i])
            i += 1

    output = ""
    opstack = []
    for token in tokens:
        if token.isdigit() or token.isalpha() or token == '#':

            output += token
        elif token == "(":

            opstack.append(token)
        elif token == ")":

            while opstack and opstack[-1] != "(":
                output += opstack.pop()
            if opstack and opstack[-1] == "(":
                opstack.pop()
        else:


            while opstack and opstack[-1] != "(" and operators[token] <= operators[opstack[-1]]:
                output += opstack.pop()
            opstack.append(token)

    while opstack:
        output += opstack.pop()

    return output
