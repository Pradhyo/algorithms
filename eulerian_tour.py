# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

from collections import defaultdict

def find_eulerian_tour(graph):
    # your code here
    adj = defaultdict(list)
    path = []
    for a,b in graph:
        adj[a].append(b)
        adj[b].append(a)
    nodes = adj.keys()
    print adj
    print nodes
    path.append(nodes[0])
    path.append(adj[nodes[0]][0])
    print path
    
    
    return []

graph = [(1, 2), (1, 4), (3, 4), (2, 3), (3, 8), (4, 8), (4, 5), (3,6), (5,6), (7,8), (6,7),(6,8)]
find_eulerian_tour(graph)


