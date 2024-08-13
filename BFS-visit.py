def bfs(graph, start):
    visited = [] 
    queue = [start]  

    while queue:  
        node = queue.pop(0)
        if node in visited:
            continue
        visited.append(node)

        for neighbour in graph[node]:
            queue.append(neighbour)  

    return visited  

graph = {}
n = int(input("Enter the number of the vertices of your graph: "))
for i in range(n):
    vertex = input(f"Vertex {i+1}: ")
    adjs = list(input("Its adjacent vertices: ").split())
    graph[vertex] = adjs

start_node = input("Enter the initial state node name: ")

visited = bfs(graph, start_node)

print(f"The order how BFS visits the graph from node {start_node}: {visited}")
