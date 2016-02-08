graph = {
    'a': ['b', 'c'],
    'b': ['c', 'd'],
    'c': ['d'],
    'd': ['c'],
    'e': ['f'],
    'f': ['c']
}

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[node]:
        if node not in path:
            new = find_path(graph, node, end, path)
            return new
    return None