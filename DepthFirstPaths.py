from Graph import Graph
from collections import deque


class DepthFirstPaths(object):
    """
    This Graph client uses depth-first search to find paths to all the vertices in a graph that are connected to a
    given start vertex src. To save known paths to each vertex,this code maintains a vertex-indexed array edgeTo[]
    such that edgeTo[w] = v means that v-w was the edge used to access w for the first time. The edgeTo[] array is a
    parent-link representation of a tree rooted at src that contains all the vertices connected to src.
    """
    def __init__(self, G: Graph, src: int):
        self.marked = [False] * G.V()  # has dfs been called on this vertex?
        self.edge_to = [None] * G.V()  # last vertex on known path to this vertex
        self.src = src                 # source

        def dfs(G: Graph, v: int):  # call depth-first search
            self.marked[v] = True
            for w in G.adj(v):
                if not self.marked[w]:
                    self.edge_to[w] = v
                    dfs(G, w)
        dfs(G, self.src)

    def has_path_to(self, v: int) -> bool:
        """
        Returns True if there is a path between src and v, else False
        :param v:
        :return:
        """
        return self.marked[v]

    def path_to(self, v: int) -> list:
        """
        Returns a path from src (implicit parameter) to v as a list, if a path exists. Returns empty list if no path
        exists.
        :param v: the destination node
        :return:
        """
        if not self.has_path_to(v):
            print("No path exists.")
            return []
        path = deque()
        x = v
        while x != self.src:
            path.appendleft(x)
            x = self.edge_to[x]
        path.appendleft(self.src)
        path = list(path)
        print("Depth-first path from", self.src, "to", v, ":", path)
        return path
