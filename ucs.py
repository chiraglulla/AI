# graph = {
#     'Z': [(1,'A'), (3, 'B'), (5, 'C')],
#     'A': [(3,'G')],
#     'G':[(3, 'H'), (1, 'I')],
#     'H': [],
#     'I': [],
#     'B': [(4,'F')],
#     'F': [(1, 'J')],
#     'J': [],
#     'C': [(1, 'D'), (2, 'E')],
#     'D': [(4,'E')],
#     'E': [(2, 'F'),(1, 'Y')],
#     'Y': []
# }

graph = {
    'S': [(1, 'A'), (12, 'G')],
    'A': [(3, 'B'), (1, 'C')],
    'B': [(3,'D')],
    'C': [(1, 'D'), (2, 'G')],
    'D': [(3, 'G')],
    'G': []
}

def ucs(graph, queue, shortest, current_node, goal_node):
    queue.append((0, current_node))
    while queue:
        print(queue)
        current = queue.pop(0)
        node = current[1]
        value = current[0]

        # print(node)
        if node == goal_node:
            print(f"found destination node with cost {value}")
            break

        for neighbor in graph[node]:
            next_node = neighbor[1]
            next_value = neighbor[0]
            there = False
            for i in range(len(queue)):
                check_node = queue[i][1]
                if check_node == next_node:
                    there = True
                    if queue[i][0] < value + next_value:
                        break
                    else:
                        queue.pop(i)
                        queue.append((value + next_value, next_node))
                        # queue[i][0] = value + next_value
                        break
            
            if not there:
                queue.append((value + next_value, next_node))

        queue.sort(key= lambda x: (x[0], x[1]))



queue = []
shortest = []
print(ucs(graph, queue, shortest, 'S', 'G'))