# 0,1,2,3,4,5,6,7,8,9 의 모든 순열 backtracking으로 구해보기 시간복잡도 O(최악 10^10 - pruning)
n = 10

visited = [0 for _ in range(n)]

cnt = 0


def dfs(idx, path):  # idx로 탈출조건, path는 방문 경로
    global cnt
    if idx == n:
        return
    for i in range(n):  # 0부터 9까지
        cnt += 1
        if not visited[i]:
            visited[i] = 1
            path.append(i)
            dfs(idx + 1, path)
            visited[i] = 0
            path.pop()


dfs(0, [])
print(cnt)  # 62353010
