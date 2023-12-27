import graphviz
import networkx as nx
import random

input = open('in25').read().strip().split('\n')
print(len(input))
input = [i.split(':') for i in input]
graph = {}
for i in input:
    key = i[0]
    val = i[1].split()
    cur = []
    if key in graph:
        cur = graph[key]
    graph[key] = cur+val
    for j in val:
        cur = []
        if j in graph:
            cur = graph[j]
        graph[j] = cur +[key]


# [print(i,':',graph[i]) for i in graph]
print(len(graph))  
s = sum([len(graph[i]) for i in graph])
print(int(s/2))

part1 = []
def intersection(cluster):
    new = []
    for i1 in range(len(cluster)):
        for i2 in range(i1+1,len(cluster)):
            newp = list(set(graph[cluster[i1]])&set(graph[cluster[i2]]))
            for i in newp:
                if i not in new and i not in cluster:
                    new.append(i)

    return cluster+new

def findcluster(p1,p2):
    l = 0
    cluster = [p1,p2]
    nl = len(cluster)
    while l != nl:
        l = nl
        cluster = intersection(cluster)
        nl = len(cluster)

    return(len(cluster))    


graaf = graphviz.Graph(name='graph2',filename='graph2.gv',format='SVG')
g = nx.Graph()
seen = set()
for i in graph:
    for j in graph[i]:
        seen.add((i,j))
        if (j,i) not in seen:
            graaf.edge(i,j)
            g.add_edge(i,j,capacity=1)

vertexis = [i for i in graph]
# graaf.view()
print(graph['dhn'])
print(random.choice(vertexis))
cut = 0
while cut != 3:
    cut,part = nx.minimum_cut(g,random.choice(vertexis),random.choice(vertexis))
print(len(part[0])*len(part[1]))
#'ptj'