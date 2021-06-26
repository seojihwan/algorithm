def solution(grades, weights, threshold):
    a = dict()
    # 가중치 값 딕셔너리에 저장
    a["A+"] = 10
    a["A0"] = 9
    a["B+"] = 8
    a["B0"] = 7
    a["C+"] = 6
    a["C0"] = 5
    a["D+"] = 4
    a["D0"] = 3
    a["F"] = 0

    answer = 0

    # grades 와 weights의 길이는 같다.
    for idx in range(len(grades)):
        # 각 성적에 해당하는 점수와 가중치를 곱한값을 answer에 더함
        print(a[grades[idx]], weights[idx])
        answer += a[grades[idx]] * weights[idx]
    # 전체 성적 - threshold
    answer -= threshold
    print(answer)
    return answer


g, w, t = ["A+", "D+", "F", "C0"]	, [2, 5, 10, 3]	, 50
solution(g, w, t)
