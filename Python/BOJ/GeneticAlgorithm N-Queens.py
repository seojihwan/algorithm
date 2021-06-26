from random import randrange as random
from time import time

SIZE = 100
n = int(input())
start = time()  # 시작 시간 저장

# 초기 유전자 생성


def genarate():
    chromosome = []
    while len(chromosome) < n:
        # 1에서 n까지의 랜덤한 정수 값 n개로 구성된 유전자 생성
        el = random(1, n + 1)       # 1 에서 n 까지
        if el not in chromosome:    # 중복이 없도록 구성하여 Permutation Encoding을 수행합니다.
            chromosome.append(el)
    return chromosome


def tournament(chromosomes):    # 평가된 적응도를 바탕으로 임의의 크기의 토너먼트를 시행한 후
    # 1등 2등이 부모로 선택됩니다.
    scale = random(2, SIZE)
    group = []
    for _ in range(scale):
        group.append(chromosomes[random(0, SIZE)])
    group = sorted(group, key=lambda x: x[n], reverse=True)
    return group[0], group[1]


def fit(chromosome):  # 적응도를 측정하기 위한 함수로 대각선의 중복에 따라 0에서 100까지 부여됩니다.
    t1, t2 = 0, 0
    f1, f2 = [], []
    for y, x in enumerate(chromosome):  # 대각선 정보를 계산하여 f1,f2에 저장합니다.
        f1.append(x + y)
        f2.append((x - y))
    f1.sort()
    f2.sort()
    for i in range(1, n - 1):   # 정렬한 후 좌우의 중복 횟수를 확인합니다.
        if f1[i] == f1[i - 1]:
            t1 += 1
        if f2[i] == f2[i - 1]:
            t2 += 1
    return (1 - (t1 + t2) / (2 * (n - 1))) * 100    # 적응도 값이 반환됩니다.


def crossover(p1, p2):  # Order-based crossover
    # 부모 p1, p2 를 전달받으면 Two Point를 설정하여
    # 구간내의 부분은 p1으로 부터 물려받고,
    # 나머지는 중복이 없는 정수에대해 p2의 순서대로 child 에게 물려줍니다.

    # 서로 다른 랜덤 값 r1, r2를 구합니다.
    r1, r2 = random(1, n), random(1, n)
    while r1 == r2:
        r1, r2 = random(1, n), random(1, n)
    if r1 > r2:
        r1, r2 = r2, r1

    child = []*n

    # 먼저 r1 ~ r2내에 존재하지 않는 p2의 정보를 순서대로 추가한후에
    for e in p2:
        if e not in p1[r1:r2]:
            child.append(e)
    # r1 ~ r2 구간내의 정보를 r1위치에 삽입합니다.
    child[r1:r1] = p1[r1:r2]

    # 만들어진 child가 반환됩니다.
    return child


def mutation(chromosome):   # displacement Mutation
    if random(0, 100) < 85:     # 0 ~ 99 랜덤중에 85 보다 작은 경우 종료합니다.
        return chromosome
    # 15% 확률로 mutation이 이루어집니다.

    # 임의의 r1, r2선정
    r1, r2 = random(0, n), random(0, n)
    while r1 == r2:
        r1, r2 = random(0, n), random(0, n)
    if r1 > r2:
        r1, r2 = r2, r1
    # 유전자의 r1, r2 위치의 정보를 교환합니다.
    chromosome[r1], chromosome[r2] = chromosome[r2], chromosome[r1]

    # 교환된 유전자가 반환됩니다.
    return chromosome


chromosomes = [[0 for _ in range(n + 1)]] * SIZE
for i in range(SIZE):
    genarated = genarate()
    chromosomes[i] = genarated + [fit(genarated)]
generations = 1
chromosomes = sorted(chromosomes, key=lambda x: x[n], reverse=True)

while True:
    if chromosomes[0][n] == 100.0:
        print(chromosomes[0][:n])
        break
    nextchromosomes = []
    for i in range(SIZE):
        p1, p2 = tournament(chromosomes)
        child = crossover(p1[:n], p2[:n])
        child = mutation(child)
        nextchromosomes.append(child + [fit(child)])
    nextchromosomes = sorted(nextchromosomes, key=lambda x: x[n], reverse=True)
    chromosomes = nextchromosomes
    generations += 1

print("generation: ", generations)
print("chromosome: ", chromosomes[0][:n])
board = [[" " for _ in range(n)] for _ in range(n)]
for y, x in enumerate(chromosomes[0][:n]):
    board[y][x - 1] = "Q"
for e in board:
    print(e)

print("12141718서지환 Genetic Algorithm 수행시간:",
      round((time() - start) * 1000, 4), "ms")  # 현재시각 - 시작시간 = 수행 시간
