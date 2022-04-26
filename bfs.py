graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

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


def bfs(graph, start, dest):
    result = ["Not reachable", list()]

    visited = list()
    queue = list()

    visited.append(start)
    queue.append(start)

    while queue:
        curr = queue.pop(0)

        if curr not in graph.keys():
            continue
        done = False
        for node in graph[curr]:
            if node not in graph.keys():
                continue
            
            if node not in visited:
                visited.append(node)
                queue.append(node)
                print(queue)

            if node == dest:
                result[0] = "reachable"
                done = True
                break
        if done: break
    result[1] = visited
    return result


result = bfs(graph, 'A', 'F')

print("Status:", result[0])
print("Path:", result[1])
