from collections import deque
from Graph import Graph


class BreadthFirstPaths(object):
    def __init__(self, G: Graph, src: int):
        self.marked = [False] * G.V()
        self.edge_to = [None] * G.V()
        self.src = src

        def bfs(G: Graph, src: int):
            queue = deque()
            self.marked[src] = True
            queue.appendleft(src)
            while queue:
                v = queue.pop()
                for w in G.adj(v):
                    if not self.marked[w]:
                        self.edge_to[w] = v
                        self.marked[w] = True
                        queue.appendleft(w)
        bfs(G, src)

    def has_path_to(self, v: int) -> bool:
        """
        Returns True if there is a path between src and v, else False
        :param v:
        :return:
        """
        return self.marked[v]

    def path_to(self, v: int) -> None or list:
        """
        Returns the shortest path from src (implicit parameter) to v, if a path exists. Returns None if no path exists.
        :param v:
        :return:
        """
        if not self.has_path_to(v):
            print("No path exists.")
            return None
        path = deque()
        x = v
        while x != self.src:
            path.appendleft(x)
            x = self.edge_to[x]
        path.appendleft(self.src)
        path = list(path)
        print("Breadth-first path from", self.src, "to", v, ":", path)
        return path
