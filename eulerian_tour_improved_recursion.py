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

# Checking if degree of all nodes is even
# which would ensure an eulerian tour exists
def is_tour(nodes):
    for i in nodes:
        if len(nodes[i]) % 2 != 0:
            return False
    return True


def find_eulerian_tour(graph):
    nodes = defaultdict(list)
    for k,l in graph:
        nodes[k].append(l)
        nodes[l].append(k)
    if is_tour(nodes):
