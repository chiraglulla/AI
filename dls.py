# graph = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E'],
#     'C' : ['F'],
#     'D' : [],
#     'E' : ['F'],
#     'F' : []
# }

# graph = {
#     'S' : ['A','B'],
#     'A' : ['C', 'D'],
#     'B' : ['I', 'J'],
#     'C' : ['E', 'F'],
#     'D' : ['G'],
#     'I' : ['H'],
#     'J' : [],
#     'E' : [],
#     'F' : [],
#     'G' : [],
#     'H' : []
# }

# graph = {
#     'A' : ['E', 'B'],
#     'B' : ['C', 'E'],
#     'C' : ['B', 'D'],
#     'D' : ['C', 'E', 'F'],
#     'E' : ['A', 'D'],
#     'F' : ['D']
# }

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['B', 'D'],
    'F': ['C', 'H'],
    'G': ['C'],
    'H': ['F']
}

visited = set()

def dls(graph, visited, node, target, level, maxDepth):
    if node == target:
        print("Found", target)
        result = list()
        result.append(target)
        return result
    
    if level == maxDepth:
        return False

    if node not in visited:
        print("Current Node:")
        print(node)
        visited.add(node)
        for n in graph[node]:
            print("Adjacents:")
            print(n)
            result = dls(graph, visited, n, target, level+1, maxDepth)
            if result:
                result.append(node)
                return result
    return False
path = dls(graph, visited, 'A', 'H', 1, 4)
if path:
    print(path[::-1])
else:
    print("Not found")