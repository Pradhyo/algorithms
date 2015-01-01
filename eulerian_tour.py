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
    total_edges = len(graph)
    current_edges = 0
    path.append(nodes[0])
    path_index = 0
    while (current_edges < total_edges):
        if current_edges == 0:
            path.append(adj[path[path_index]][0])
            path_index += 1
            current_edges += 1
            adj[path[path_index-1]].remove(path[path_index])
            adj[path[path_index]].remove(path[path_index-1])

        if (len(adj[path[path_index]]) == 1):
            path.append(adj[path[path_index]][0])
            path_index += 1
            current_edges += 1
            adj[path[path_index-1]].remove(path[path_index])
            adj[path[path_index]].remove(path[path_index-1])
        

        elif (current_edges != total_edges -2):
            if (len(adj[adj[path[path_index]][0]]) == 2) and ((adj[adj[path[path_index]][0]][0] == path[0]) or (adj[adj[path[path_index]][0]][1] == path[0])):
                path.append(adj[path[path_index]][0])
            else:
                path.append(adj[path[path_index]][1])
            path_index += 1
            current_edges += 1
            adj[path[path_index-1]].remove(path[path_index])
            adj[path[path_index]].remove(path[path_index-1])
        print path
        
    
    return path

graph = [(1, 2), (1, 4), (3, 4), (2, 3), (3, 8), (4, 8), (4, 5), (3,6), (5,6), (7,8), (6,7),(6,8)]
find_eulerian_tour(graph)


