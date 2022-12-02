import pprint


class Graph(object):
    """
    An implementation of an undirected graph.
    """

    def __init__(self, v: int):
        self.vertices = v  # number of vertices
        self.edges = 0  # number of edges
        self.graph = {}  # adjacency lists

    def V(self) -> int:
        """
        Returns the number of vertices in the graph
        :return: number of vertices
        """
        return self.vertices

    def E(self) -> int:
        """
        Returns the number of edges in the graph
        :return: number of vertices
        """
        return self.edges

    def get_vertices(self):
        """
        Returns a list of the vertices in this graph
        :return: a list of the vertices in the graph
        """
        return self.graph.keys()

    def add_edge(self, v: int, w: int):
        """
        Adds a new edge between vertices v and w
        :param v: the first vertex
        :param w: the second vertex
        """
        # check if the vertices are already in the graph, if not, add them
        if v not in self.graph:
            self.graph[v] = []
        if w not in self.graph:
            self.graph[w] = []

        self.graph[v].append(w)  # add w to v's adjacency list
        self.graph[w].append(v)  # add v to w's adjacency list
        self.edges += 1

    def adj(self, v: int):
        """
        Returns the adjacency list of the vertex v
        :param v: the vertex
        :return: the adjacency list of the vertex
        """
        return self.graph[v]

    def display(self):
        """
        Displays the visual representation of the graph
        """
        print("Vertices: " + str(self.V()) + "\nEdges: " + str(self.E()))
        pp = pprint.PrettyPrinter()
        pp.pprint(self.graph)


def degree(G: Graph, v: int) -> int:
    """
    Returns the degree of the vertex v or graph G
    :param G: the graph in question
    :param v: the vertex of G
    :return: the integer degree of the vertex
    """
    return len(G.adj(v))


def max_degree(G: Graph) -> int:
    """
    Returns the maximum vertex degree of the graph G
    :param G:
    :return:
    """
    _max = 0
    for v in G.get_vertices():
        _max = max(_max, degree(G, v))
    return _max


def avg_degree(G: Graph) -> int:
    """
    Return the average degree of the graph
    :param G: the graph to analyze
    :return: average degree of the graph (rounded down to the nearest integer)
    """
    return 2 * G.E() // G.V()


def number_of_self_loops(G: Graph) -> int:
    """
    Returns the number of self loops in the graph
    :param G: the graph to analyze
    :return: the number of self loops
    """
    count = 0
    for v in G.get_vertices():
        for w in G.adj(v):
            if w == v:
                count += 1
    return count // 2
