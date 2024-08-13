def bfs(graph, start, goal):
    visited = [] 
    queue = [[start]]  

    while queue:  
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        for neighbour in graph[node]:
            new_path = path + [neighbour] 
            queue.append(new_path)  

    return None  

graph = {}
n = int(input("Enter the number of the vertices of your graph: "))
for i in range(n):
    vertex = input(f"Vertex {i+1}: ")
    adjs = list(input("Its adjacent vertices: ").split())
    graph[vertex] = adjs

start_node = input("Enter the initial state node name: ")
goal_node = input("Enter the goal state node name: ")

path = bfs(graph, start_node, goal_node)

print(f"Path from {start_node} to {goal_node}: {path}")
