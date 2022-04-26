graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()

def dfs(graph, visited, node, target):
    if node == target:
        print("Found", target)
        result = list()
        result.append(target)
        return result
    
    if node not in visited:
        print(node)
        visited.add(node)
        for n in graph[node]:
            result = dfs(graph, visited, n, target)
            if result:
                result.append(node)
                return result
    return False
            
path = dfs(graph, visited, 'A', 'F')
if path:
    print(path[::-1])
else:
    print("Not found")
