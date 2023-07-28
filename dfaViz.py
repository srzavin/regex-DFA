import graphviz
import main
nodes = main.nodes
transitions = main.rawar
leng = len(main.val[1])
f = graphviz.Digraph('finite_state_machine', filename='dfa.gv')
f.attr(rankdir='LR', size='8,5')
accStat = []
normalNode = []

for i in range(0,len(transitions)):
    for j in range(1,len(transitions[i])-1, 2):
        alpha = transitions[i][0]
        nxtstat = main.transition(transitions ,alpha,transitions[i][j] )
        if leng in transitions[i][j] or leng in transitions[i][j+1] :
            f.attr('node', shape='doublecircle')
            if nxtstat != None:
                f.edge(str(transitions[i][j]) , str(nxtstat), label = alpha)

        else:
            f.attr('node', shape='circle')
            if nxtstat != None:
                f.edge(str(transitions[i][j]) , str(nxtstat),  label = alpha)

f.view()