def solution(s, op):

    answer = []
    for idx in range(1, len(s)):
        print(idx)
        # 02 같은 경우 2로 바꿀 수 있도록 int로 형변환 후 str로 형변환
        # 인덱스 idx는 1부터 s의 길이 - 1 까지
        # idx 이전 까지의 문자열( ~ idx - 1), idx부터의 문자열(idx ~ )로 나눠서 연산처리
        print(s[:idx], s[idx:])
        f, e = int(s[:idx]), int(s[idx:])
        f, e = str(f), str(e)
        print(f, op, e)
        print(eval(f + op + e))

        # 문자열로 구성된 식을 계산된 결과 값으로 반환
        answer.append(eval(f + op + e))
    return answer


s, op = "1234"	, "+"
solution(s, op)
