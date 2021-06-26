import requests
from collections import deque

url = 'https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users'
x_auth_token = 'f2d506e419d9223cabfb585b349e7f21'


def start(problem):
    uri = url + '/start'
    return requests.post(uri, headers={'X-Auth-Token': x_auth_token}, json={'problem': problem}).json()


def locations(auth_key):
    uri = url + '/locations'
    return requests.get(uri, headers={'Authorization': auth_key}).json()


def trucks(auth_key):
    uri = url + '/trucks'
    return requests.get(uri, headers={'Authorization': auth_key}).json()


def simulate(auth_key, commands):
    uri = url + '/simulate'
    return requests.put(uri, headers={'Authorization': auth_key}, json={'commands': commands}).json()


def score(auth_key):
    uri = url + '/score'
    return requests.get(uri, headers={'Authorization': auth_key}).json()

# 맨밑이 y = 0 맨 왼쪽이 x = 0


def findPos(id, gl):
    y = id // gl
    x = id % gl
    return y, x


def findIdByPos(act, pos, gl):
    y, x = pos
    # 위 아래 오른쪽 왼쪽
    if act == 1:
        y += 1
    elif act == 3:
        y -= 1
    elif act == 2:
        x += 1
    elif act == 4:
        x -= 1
    id = y * gl + x
    return id


[1, 2, 3, 4, 5, 6, 7]


def truckCommand(s, averageBike, locs, trucks, tcnt):
    commands = []
    for i in range(tcnt):
        command = []
        state = True
        for _ in range(10):
            id = trucks[i]['location_id']
            if state and locs[id]['located_bikes_count'] > averageBike + 2 and trucks[i]['loaded_bikes_count'] + 1 <= 20:
                command.append(5)
                trucks[i]['loaded_bikes_count'] += 1
                locs[id]['located_bikes_count'] -= 1
                state = False
                continue
            elif state and 0 <= locs[id]['located_bikes_count'] < 1 and trucks[i]['loaded_bikes_count'] >= 1:
                command.append(6)
                trucks[i]['loaded_bikes_count'] -= 1
                locs[id]['located_bikes_count'] += 1
                state = False
                continue
            currentIdx = s[i].popleft()
            s[i].append(currentIdx)
            command.append(currentIdx)
            state = True

        commands.append({"truck_id": i, "command": command})
    return commands


def firstMove(problemNumber):
    if problemNumber == 1:
        commands = []
        command = [[1, 1], [1, 1, 1, 1], [1, 1, 1, 2],
                   [1, 1, 2, 2], [1, 1, 1, 1, 2, 2]]
        for i in range(5):
            commands.append({"truck_id": i, "command": command[i]})

        return commands


def main(problemNumber):
    ret = start(problemNumber)
    auth = ret['auth_key']
    loc = locations(auth)['locations']
    tru = trucks(auth)['trucks']
    truckCnt = len(tru)
    print(loc)
    print(trucks(auth)['trucks'])
    # 각자 포지션으로 이동
    res = simulate(auth, firstMove(1))
    # 움직임설정
    s = [deque([2, 2, 3, 4, 4, 3, 2, 2, 1, 1, 4, 3, 3, 4, 1, 1])
         for _ in range(truckCnt)]
    c = 0
    while True:
        loc = locations(auth)['locations']
        tru = trucks(auth)['trucks']
        # 전체 바이크, 평균 바이크 갯수 구하기
        totalBike = 0
        for e in loc:
            totalBike += e['located_bikes_count']
        averageBike = totalBike // len(loc)
        commands = truckCommand(s, averageBike, loc, tru, truckCnt)
        res = simulate(auth, commands)
        print(res)
        if (res['status'] == 'finished'):
            print("end")
            print(score(auth))
            break
        c += 1


main(1)
