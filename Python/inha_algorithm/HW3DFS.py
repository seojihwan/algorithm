# defaultdict를 이용하여 노드값을 key로 갖고 자식값을 데이터로 갖는 dictionary 사용합니다.
from collections import defaultdict
print("12141718서지환 과제3 DFS")
print("정점의 수 m 간선의수 n : ", end='')
m, n = map(int, input().split())    # 그래프에서 노드의 수 m과 간선의 수 n을 입력받습니다.
print("간선 입력")

data = defaultdict(set)  # 간선 정보를 저장한 dictionary로 기본 데이터는 set을 갖습니다.
parent = defaultdict(int)  # 부모 노드 정보를 저장한 dictionary로 기본 데이터는 int를 갖습니다.
for _ in range(n):  # n개의 간선 정보를 입력받아 저장합니다.
    a, b = map(int, input().split())
    data[a].add(b)  # 양 방향의 간선 정보를 저장합니다.
    data[b].add(a)


print("DFS 수행 결과")
root = 0
stack = [root]  # 스택을 사용하여 DFS를 구현하였습니다.
visited = []  # 방문했던 노드를 기록합니다.
while stack:  # 스택에 데이터가 없을때 까지 깊이 탐색을 수행합니다.
    node = stack.pop()  # 스택에서 node를 꺼냅니다.
    if node != root:
        print("(", parent[node], ")-(", node, ")")  # 부모에서 자식노드로의 이동 간선을 출력합니다.
    for childNode in data[node]:      # 자식 노드들에 대하여 방문여부를 확인합니다.
        if childNode not in visited:
            stack.append(childNode)   # 방문한 노드의 자식 노드들을 스택에 추가합니다.
            parent[childNode] = node  # 노드의 부모 정보를 dictionary에 저장합니다.
            visited.append(childNode)  # 방문했던 노드를 기록합니다.
