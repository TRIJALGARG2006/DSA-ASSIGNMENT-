from collections import deque


def bfs(graph, start):

    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        for item in graph.get(node, []):
            neighbor = item[0] if isinstance(item, tuple) else item
            if neighbor not in visited:
                queue.append(neighbor)

    return order


def dfs(graph, start):

    visited = set()
    order = []

    def _dfs(node):
        visited.add(node)
        order.append(node)
        for item in graph.get(node, []):
            neighbor = item[0] if isinstance(item, tuple) else item
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)
    return order


if __name__ == "__main__":

    g = {
        "A": [("B", 2), ("C", 1)],
        "B": [("D", 3)],
        "C": [("D", 1)],
        "D": [("E", 4)],
        "E": [],
    }

    start_node = "A"
    print("BFS order:", bfs(g, start_node))
    print("DFS order:", dfs(g, start_node))

