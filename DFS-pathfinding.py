def dfs(graph, start_node, target_node):
    frontier = [(start_node, [start_node])]

    while frontier:
        node, path = frontier.pop(0)
        if node == target_node:
            return path
        for neighbor in graph[node]:
            if neighbor not in path:
                frontier[:0] = [(neighbor, path + [neighbor])]
    return None

graph = {}
n = int(input("Enter the number of the vertices of your graph: "))
for i in range(n):
    vertex = input(f"Vertex {i+1}: ")
    adjs = list(input("Its adjacent vertices: ").split())
    graph[vertex] = adjs

start_node = input("Enter the initial state node name: ")
target_node = input("Enter the goal state node name: ")
path = dfs(graph, start_node, target_node)

if path:
    print(f"Path found from {start_node} to {target_node}: {path}")
else:
    print(f"No path found from {start_node} to {target_node}")
