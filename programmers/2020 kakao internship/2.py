from re import findall


def calc(op, a, b):
    a, b = int(a), int(b)
    if op == '-':
        return a - b
    elif op == '+':
        return a + b
    elif op == '*':
        return a * b


def solution(expression):
    answer = 0
    nums = findall('[0-9][0-9][0-9]|[0-9][0-9]|[0-9]', expression)
    ops = findall('\D', expression)
    ds = [['-', '+', '*'], ['-', '*', '+'], ['+', '-', '*'],
          ['+', '*', '-'], ['*', '+', '-'], ['*', '-', '+']]
    for d in ds:
        nums_init = nums
        ops_init = ops
        for i in range(3):
            nums_temp = []
            ops_temp = []
            nums_temp.append(nums_init[0])
            for idx, op in enumerate(ops_init):
                if op == d[i]:
                    nums_temp.append(
                        calc(op, nums_temp.pop(), nums_init[idx + 1]))
                else:
                    nums_temp.append(nums_init[idx + 1])
                    ops_temp.append(ops_init[idx])
            nums_init = nums_temp
            ops_init = ops_temp
        answer = max(answer, abs(nums_init[0]))
    return answer


expression = "50*6-3*2"
solution(expression)
