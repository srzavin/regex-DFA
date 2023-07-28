from anytree import Node, RenderTree
import intopostfix
regex = "(a|b)*.a.b.b"

regex = regex + ".#"    #augmentation


#"ab|*ac.*|#."
postfix = intopostfix.infix_to_postfix(regex)
print(postfix)



class Node:
    def __init__(self, value, left=None, right=None, parent = None, num=None):
        self.value = value
        self.left = left
        self.right = right
        self.first_pos = set()
        self.last_pos = set()
        self.nullable = False
        self.follow_pos = set()
        self.parent = parent
        self.num = num






def position(regex):
    stack = []
    output = []
    leaf = []
    count = 1
    for i in regex:
        if i.isalpha() or i == '#':
            node1 = Node(value=i, num=count)
            node1.first_pos.add(count)
            node1.last_pos.add(count)
            node1.nullable = False
            leaf.append(node1)
            stack.append(node1)

            count += 1
        elif i == '|' or i == '.':
            newNode = Node(value=i)
            a = stack.pop()
            b = stack.pop()
            if i == "|":
                newNode.nullable = False
                if a.nullable or b.nullable:
                    newNode.nullable = True
                newNode.first_pos = a.first_pos|b.first_pos
                newNode.last_pos  = a.last_pos|b.last_pos
            else:
                if b.nullable and a.nullable:
                    newNode.nullable = True
                if b.nullable == True:
                    newNode.first_pos = a.first_pos|b.first_pos
                    newNode.last_pos = a.last_pos
                if b.nullable!= True:
                    newNode.first_pos = b.first_pos
                    newNode.last_pos = a.last_pos
                for i in b.last_pos:
                    leaf[i - 1].follow_pos = leaf[i - 1].follow_pos | a.first_pos

            newNode.right = a
            newNode.left = b
            stack.append(newNode)
            output.append(newNode)
        elif i == '*':
            a = stack.pop()
            newNode = Node(value = i, left=a)
            newNode.nullable = True
            newNode.first_pos = a.first_pos
            newNode.last_pos = a.last_pos
            for i in newNode.last_pos:
                leaf[i-1].follow_pos = leaf[i-1].follow_pos|newNode.first_pos
            stack.append(newNode)
            output.append(newNode)
        else:
            output.append(Node(value = i))
    return output, leaf

val = position(postfix)



alpha = []
def printfollowPos(flag = False):
    if flag == True:
        for i in val[1]:
            print(i.value)
            print(i.num)
            print("FOllow POS IS : " , i.follow_pos)




def make_DFA():
    visited = []
    marked = []
    dstate = [val[0][-1].first_pos]
    count = 0
    # make list of chars
    for i in postfix:
        if i.isalpha():
            if i not in alpha:
                alpha.append(i)
                marked.append([i])
                count+=1
    while dstate!=[]:
        a = dstate.pop()
        visited.append(a)
        count1= 0
        for i in alpha:
            folpos = set()
            for j in a:
                if i == val[1][j-1].value:
                     folpos = folpos | val[1][j-1].follow_pos
            if folpos not in visited:
                dstate.append(folpos)
            marked[count1].append(a)
            marked[count1].append(folpos)
            count1+=1

    return marked, visited

rawdata = make_DFA()
rawar = rawdata[0]
nodes = rawdata[1]
print(nodes)
def transition(rawarr, char, stat):
    for i in range(0,len(rawarr)):
        if rawarr[i][0] == char:
            for j in range(1,len(rawarr[i])-1,2):
                if rawarr[i][j] == stat:
                    if rawarr[i][j+1] == set():
                        return None
                    else:
                        return rawarr[i][j+1]



def regexChcker(strr):
    nxtStat = val[0][-1].first_pos
    for i in strr:
        if i not in alpha:
            return  print("Rejected")
        a = transition(rawar, i , nxtStat)
        if a != None:
            nxtStat = a
    if len(val[1]) in nxtStat:
        print("Accepted")
    else:
        print("Rejected")



testStr = "aaabababaa"
regexChcker(testStr)



def nodesTree(p = False):
    if p == True:
        for i in range(0,len(val)):
            print(val[0][i])
            print("value: ", val[0][i].value)
            try:
                print("Right: ", val[0][i].right.value)
                print("Left: ",val[0][i].left.value)
                print("Parent First Post: ", val[0][i].first_pos)
                print("Parent last Post: ", val[0][i].last_pos)
                print("NUM Left First Pos: ", val[0][i].left.first_pos  )
                print("NUM Left Last Pos: ", val[0][i].left.last_pos)
                print("NUM Right First Pos: ", val[0][i].right.first_pos  )
                print("NUM Right Last Pos: ", val[0][i].right.last_pos)
                print("NUM Right: ", val[0][i].right.num)
                print("NUM Left Follow Pos: ", val[0][i].left.follow_pos)
                print("NUM Right Follow Pos: ", val[0][i].right.follow_pos  )
            except:
                print("Right: ", val[0][i].right)
                print("Left: ", val[0][i].left)

    else:
        return


nodesTree(p = False)
printfollowPos(False)