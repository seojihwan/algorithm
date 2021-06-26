print("12141718서지환 과제3 Bellman-ford")
print("정점의 수 m 간선의수 n : ", end='')
m, n = map(int, input().split())    # 그래프에서 노드의 수 m과 간선의 수 n을 입력받습니다.
print("간선 입력")

# m x m 행렬의 각 data를 INF로 초기화합니다.
INF = float("inf")
weight = [[INF for _ in range(m)] for _ in range(m)]
for _ in range(n):  # n개의 간선 정보를 입력받아 저장합니다.
    a, b, w = map(int, input().split())
    weight[a][b] = w  # 간선 정보와 가중치를 저장합니다.


def BellmanFord(weight, root):
    dist = [INF] * m
    dist[root] = 0
    for _ in range(m - 1):  # 정점의 수 - 1 만큼 정점의 최단거리를 업데이트합니다.
        for u in range(m):  # 시작점 root에서 u를 거쳐 v로 이동하였을 때
            for v, w in enumerate(weight[u]):
                # u를 거쳤을 때 더 가깝거나
                # , 아직 거리가 갱신되지 않아 INF인 경우 업데이트됩니다.
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    # 음의 사이클을 찾기 위해 한번 더 각 정점에 대한 최단거리를 구합니다.
    for u in range(m):
        for v, w in enumerate(weight[u]):
            if dist[u] != INF and dist[u] + w < dist[v]:
                # 정점의 수 - 1만큼 반복한 이후, 각 정점의 최단거리를 다시 구했더니
                # 최단거리가 업데이트 된 경우, 음의 사이클이 존재함을 알 수 있습니다.
                dist[v] = dist[u] + w
                print("음의 사이클이 존재합니다.")
                return False
    print("Dist: ", dist)


BellmanFord(weight, 0)
