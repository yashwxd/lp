graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['6'],
    '8': [],
    '6': []
}

def bfs(graph, root):
    visited = set()
    queue = [root]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex])

bfs(graph, '5')
