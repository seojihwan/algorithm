# 위상정렬

# 노드 수, 간선 수 입력
v, e = map(int, input().split())

# 각 노드 진입 차수 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드의 간선 정보 저장 위한 배열
graph = [[] for _ in range(v + 1)]

# 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 초기 진입 차수 0인 노드 정보 저장
q = []
for i in range(1, v + 1):
    if not indegree[i]:
        q.append(i)

# 위상 정렬을 이용한 전체 노드 방문
while q:
    temp = []
    for node in q:
        for i in graph[node]:
            indegree[i] -= 1
            if not indegree[i]:
                temp.append(i)
    q = temp
