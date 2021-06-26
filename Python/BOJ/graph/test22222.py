graph = [[] for _ in range(4)]

print(graph[2])
graph[2].append([3, 5])
print(graph)
print(graph[2])
graph[2].append([3, 5])
for a, b in graph[2]:
    print(a, b)
print(graph[2][1])
