from collections import namedtuple

from BreadthFirstSearch import BreadthFirstSearch
from DepthFirstPaths import *
from DepthFirstSearch import *
from BreadthFirstPaths import *
from Graph import *


def setup_graph():
    with open('tinyG.txt') as graph_file:
        num_vertices = int(graph_file.readline()[:-1])
        num_edges = int(graph_file.readline()[:-1])
        G = Graph(num_vertices)
        lines = graph_file.readlines()
        print(lines)
        for line in lines:
            num1, num2 = line.split(" ")
            num2 = num2[0:-1]
            v = int(num1)
            w = int(num2)
            G.add_edge(v, w)
        G.display()
        return G


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    G = setup_graph()

    for v in G.get_vertices():
        for w in G.get_vertices():
            DepthFirstPaths(G, v).path_to(w)
            BreadthFirstPaths(G, v).path_to(w)
            print()
