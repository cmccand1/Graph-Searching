from Graph import *


class DepthFirstSearch(object):
    """
    This code maintains an array of boolean values to mark all the vertices that are connected to the source. The
    recursive method marks the given vertex and calls itself for any unmarked vertices on its adjacency list. If the
    graph is connected, every adjacency-list entry is checked.
    """
    def __init__(self, G: Graph, src: int):
        self.marked = [False] * G.V()
        self.count = 0

        def dfs(G: Graph, v: int):  # call depth-first search
            self.marked[v] = True
            self.count += 1
            for w in G.adj(v):
                if not self.is_marked(w):
                    dfs(G, w)
        dfs(G, src)

    def is_marked(self, v: int) -> bool:  # is v connected to src?
        """
        Returns True if v is connected to src, else False
        :param v:
        :return:
        """
        return self.marked[v]

    def get_count(self) -> int:  # how many vertices are connected to src?
        """
        Returns the number of vertices that are connected to src (the implicit parameter)
        :return: number of connected vertices
        """
        return self.count
