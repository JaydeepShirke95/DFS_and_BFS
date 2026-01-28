from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# -------- USER INPUT --------
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = {i: [] for i in range(vertices)}

print("Enter edges (u v):")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)   # undirected graph

start = int(input("Enter starting vertex for BFS: "))

print("\nBFS Traversal:")
bfs(graph, start)
