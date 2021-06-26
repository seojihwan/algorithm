def solution(penter, pexit, pescape, data):
    # data의 길이는 1 이상 100,000 이하인 penter의 길이의 배수
    answer = ''
    print(len(data))
    # 0 부터 시작
    s = 0
    # penter, pexit, pescape 길이 같음
    plength = len(penter)
    p = [penter, pexit, pescape]
    print(p)
    # s 는 0 부터 len(data) - penter까지
    while s < len(data):
        # 인덱스 s 부터 s + plength - 1까지 하나의 원소로 취급
        print(s, s + plength)
        e = data[s:s + plength]
        print(e)
        if e in p:
            # penter, pexit, pescape 중 하나라면 pescape를 앞에 더함
            answer += pescape + e
        else:
            answer += e
        # 다음 e를 찾기 위해 plength만큼 더해줌
        s += plength

    # 앞에 penter 끝에 pexit를 붙여줌
    answer = penter + answer + pexit
    return answer


penter = "1100"
pexit = "0010"
pescape = "1001"
data = "1101100100101111001111000000"
print(solution(penter, pexit, pescape, data))
110011011001100110010010111100111001110000000010

110011011001100110010010111100111001110000000010
