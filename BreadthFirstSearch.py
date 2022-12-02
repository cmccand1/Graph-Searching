from collections import deque
from Graph import Graph

class BreadthFirstSearch(object):
    def __init__(self, G: Graph, src: int):
        self.marked = [False] * G.V()
        self.count = 0

        def bfs(G: Graph, src: int):
            queue = deque()
            self.marked[src] = True
            self.count += 1
            queue.appendleft(src)
            while queue:
                v = queue.pop()
                for w in G.adj(v):
                    if not self.is_marked(w):
                        self.marked[w] = True
                        self.count += 1
                        queue.appendleft(w)
        bfs(G, src)

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
