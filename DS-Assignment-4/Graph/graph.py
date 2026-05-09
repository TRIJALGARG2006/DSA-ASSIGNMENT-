from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, w=1):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append((v, w))

    def print_graph(self):
        for node in self.adj:
            print(f"{node} -> {self.adj[node]}")

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)

                for neighbor, _ in self.adj.get(node, []):
                    queue.append(neighbor)

        return result

    def dfs(self, start, visited=None, result=None):
        if visited is None:
            visited = set()
            result = []

        visited.add(start)
        result.append(start)

        for neighbor, _ in self.adj.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited, result)

        return result