from bigtree import DAGNode, dag_to_dot
import intopostfix


regex = "(a|b)*.a.b.b.#"
postRegex = intopostfix.infix_to_postfix(regex)
#regex = "ab|*ac.*|#."


def bintreeIMG(regex):
    stack = []
    output = []
    count = 1
    count2 = 1
    for i in regex:
        if i.isalpha() or i == '#':
            stack.append(DAGNode(i+str(count)))
            count += 1

        elif i == '|' or i== '.':
            a = stack.pop()
            b = stack.pop()
            newNode = DAGNode(i+str(count2))
            a.parents = [newNode]
            b.parents = [newNode]
            stack.append(newNode)
            output.append(newNode)
        elif i == '*':

            a = stack.pop()
            newNode = DAGNode(i+str(count2), children=[a])
            stack.append(newNode)
            output.append(newNode)

        else:
            output.append(DAGNode(i))
        count2 += 1



    graph = dag_to_dot(output[-1], node_colour="gold")
    graph.write_png("Syntax Tree.png")



bintreeIMG(postRegex)