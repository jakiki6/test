#! /usr/bin/python3
import networkx as nx 
import matplotlib.pyplot as plt
import copy


G = nx.MultiGraph()
#edges = [(0,1),(1,2),(2,3),(3,5),(5,3),(3,4),(4,5),(5,0),(0,5),(0,5)]
edges = [(0,1),(1,2),(2,0),(0,3),(3,4),(4,5),(5,3),(3,0)]

G.add_edges_from(edges)


def get_other_node(edge, node):
    if edge[0] == node:
        return edge[1]
    else:
        return edge[0]

def draw(G, edges):
    pos = nx.circular_layout(G)

    # draw it
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='k', width=0.5) # show all edges, thin lines
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='b', width=2) # highlight edges

    plt.show()

def bridge_edge(G, edge):
    H = copy.deepcopy(G)
    startnode = edge[0]
    endnode = edge[1]
    H.remove_edge(*edge)#wenn edge eine brückenkante war, gibt es jetzt keinen pfad von startnode nach endnode

    visitednodes = [startnode]
    i = 0
    while i < len(visitednodes):#we went through all nodes in visitednodes and found no new neighbours to add
        nextnodes = list(H.neighbors(visitednodes[i]))
        if endnode in nextnodes:
            return False #if we find endnode here, there is a path from startnode to endnode
        for node in nextnodes:
            if node not in visitednodes:
                visitednodes.append(node) #add neighbour nodes to visitednodes
        i += 1
   
    return True # it is a bridge edge

def get_euler_kreis(H):
    G = copy.deepcopy(H)
    euleredges = []
    startnode = None
    unevencounter = 0
    for n in G.nodes():
        if G.degree(n) %2 != 0:
            unevencounter += 1
            node = n

    if unevencounter == 0:
        node = n

    if unevencounter > 2:
        print("Graph enthält keinen Eulerweg")
        return None

    while G.number_of_edges() > 0: # as long as there are edges in the graph
        #draw(H, euleredges) #little visualisation what is happening

        newedge = None
        #probiere alle nachbarkanten durch, bis eine kante nicht brückenkante ist, oder es keine kanten mehr gibt
        for edge in G.edges(node):
            newedge = edge
            if not bridge_edge(G, newedge):
                break
        
        if newedge: #es wurde eine kante gefunden, in einem eulerschen Graphen geht das immer (außer im letzen schritt)
            euleredges.append(newedge) #füge die kante dem eulerkreis hinzu
            G.remove_edge(*newedge) #entferne sie aus G
            
            if G.degree(node) == 0:#unnötig, aber nice für visualisierung
                G.remove_node(node)
            node = get_other_node(newedge, node) #nimm den anderen knoten aus der neuen kante als neuen knoten
            #extra funktion, da wir nicht wissen, ob unser knoten der erste oder der zweite in der kante ist
        else:
            break
        
    #draw(H, euleredges)
    return euleredges


def get_hamilton_kreis(eulerkreis):

    #finde den start- und endknoten vom eulerkreis heraus
    node = None
    for n in eulerkreis[0]:
        if n in eulerkreis[-1]:
            node = n
    
    if not node:
        print("Eingabe muss ein Kreis sein!")
        return None

    visitednodes = [node]
    for edge in eulerkreis:
        node = get_other_node(edge, node) #finde den nächsten Knoten, der besucht wird
        if node not in visitednodes:# wenn der Knoten schon besucht wurde, überspringen wir ihn einfach
            visitednodes.append(node)
    
    #jetzt wollen wir eine Liste von Kanten aus der Liste von Knoten erstellen
    hamiltonkreis = []
    n = len(visitednodes)
    for i in range(n):
        newedge = (visitednodes[i], visitednodes[(i+1) % n]) #die letze kante soll wieder zum starknoten zurückgehen, wir nutzen aus, dass (n % n = 0)
        hamiltonkreis.append(newedge)

    return hamiltonkreis

eulerkreis = get_euler_kreis(G)
print(eulerkreis)
hamiltonkreis = get_hamilton_kreis(eulerkreis)
print(hamiltonkreis)
draw(G, hamiltonkreis)