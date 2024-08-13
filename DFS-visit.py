
def dfs(graph, start_node):
    visited = []
    frontier = [start_node]

    while frontier:
        node = frontier.pop(0)
        if node not in visited:
            visited.append(node)
            frontier[:0] = [i for i in graph[node] if i not in visited]

    return visited


graph = {}
n = int(input("Enter the number of the vertices of your graph: "))
for i in range(n):
    vertex = input(f"Vertex {i+1}: ")
    adjs = list(input("Its adjacent vertices: ").split())
    graph[vertex] = adjs

start_node = input("Enter the initial state node name: ")
visited = dfs(graph, start_node)
print(f"The order how DFS visits the graph from node {start_node}: {visited}")
