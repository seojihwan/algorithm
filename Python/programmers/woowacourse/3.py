def solution(money, expected, actual):
    # 기본 베팅 100원
    betting = 100
    iswin = True

    # expected, actual의 길이 같음
    for idx in range(len(expected)):

        # 진 경우 + 베팅금액이 보유금액보다 크면 => 나머지 전체 금액을 베팅
        if not iswin and betting > money:
            betting = money

        # 돈 없는 경우 0 값 반환
        if not money:
            return 0

        # 이겻다
        if expected[idx] == actual[idx]:
            iswin = True
            # 베팅 금액만큼 money에 추가
            money += betting
            # 베팅 금액은 100으로 설정
            betting = 100

        # 졋다
        elif expected[idx] != actual[idx]:
            iswin = False
            # 베팅 금액만큼 money 차감
            money -= betting
            # 베팀 금액 2배
            betting *= 2

    # 모든 게임 끝난 후 돈 반환
    return money


m, e, a = 1000, ['H', 'T', 'H', 'T', 'H', 'T', 'H'], [
    'T', 'T', 'H', 'H', 'T', 'T', 'H']
print(solution(m, e, a))

# 이전 판의 2배를 걸어야 하는 상황에서 수중의 돈이 모자라는 경우에는 남은 돈 전부를 건다고 가정합니다.
