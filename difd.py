# graph = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E'],
#     'C' : ['F'],
#     'D' : [],
#     'E' : ['F'],
#     'F' : []
# }

graph = {
    'S' : ['A','B'],
    'A' : ['C', 'D'],
    'B' : ['I', 'J'],
    'C' : ['E', 'F'],
    'D' : ['G'],
    'I' : ['H'],
    'J' : [],
    'E' : [],
    'F' : [],
    'G' : [],
    'H' : []
}

# graph = {
#     'A' : ['E', 'B'],
#     'B' : ['C', 'E'],
#     'C' : ['B', 'D'],
#     'D' : ['C', 'E', 'F'],
#     'E' : ['A', 'D'],
#     'F' : ['D']
# }

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B', 'E'],
#     'E': ['B', 'D'],
#     'F': ['C', 'H'],
#     'G': ['C'],
#     'H': ['F']
# }

def dfid(graph, visited, node, target, level, maxDepth):
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
            result = dfid(graph, visited, n, target, level+1, maxDepth)
            if result:
                result.append(node)
                return result
    return False


maxDepth = int(input("Enter next Depth if not found - "))
for i in range(1, maxDepth+1):
    visited = set()
    path = dfid(graph, visited, 'S', 'J', 1, i)
    if path:
        print(path[::-1], "found at depth", i)
        break
    else:
        print("Not found")