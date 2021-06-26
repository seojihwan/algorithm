from collections import defaultdict


def solution(logs):
    data = defaultdict(lambda: defaultdict(int))
    print(logs)
    answer = []

    # 2차원 딕셔너리에 데이터 저장
    # 수험번호, 문제 번호, 받은 점수
    # 들어온 순서대로 덮어씌우는 방식으로 저장
    for log in logs:
        a, b, c = log.split(' ')
        data[a][b] = c

    # n제곱 시간복잡도로 사람간의 푼 문제, 점수 같은지 확인
    for pa in data:
        if len(data[pa]) < 5:
            continue
        for pb in data:
            if pa == pb:
                continue
            if len(data[pb]) < 5:
                continue
            print(data[pa], data[pb])
            # 길이 5 이상, 문제, 점수 같은 경우
            if data[pa] == data[pb]:
                answer.append(pa)
                answer.append(pb)
    # set을 이용해 중복 데이터 제거
    answer = list(set(answer))
    # 오름차순 정렬
    answer = sorted(answer)

    # 데이터 없을때 None 추가
    if not len(answer):
        answer.append('None')
    print(answer)
    return answer


l = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80",
     "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]
solution(l)


# 한 수험자가 같은 문제에 대해 여러 번 답안을 제출할 수 있습니다. 단, 마지막 제출의 채점 결과가 최종 점수입니다.
# 0점을 받는 답안 제출도 문제를 푼 것으로 칩니다.
