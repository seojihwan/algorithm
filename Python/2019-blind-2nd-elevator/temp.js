const fetch = require('node-fetch');

const url = 'https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users';

let problem = 0; // 문제 번호 선택 0, 1, 2

async function start(user, problem, count) {
  uri = url + '/start' + '/' + user + '/' + String(problem) + '/' + String(count);

  try {
    data = await fetch(uri, {
      method: 'POST',
    });
    return await data.json();
  } catch (error) {
    console.log(error);
  }
}

async function oncalls(token) {
  uri = url + '/oncalls';

  try {
    data = await fetch(uri, {
      headers: { 'X-Auth-Token': token },
    });
    return await data.json();
  } catch (error) {
    console.log(error);
  }
}

async function action(token, cmds) {
  uri = url + '/action';
  try {
    data = await fetch(uri, {
      method: 'POST',
      headers: { 'X-Auth-Token': token, 'Content-Type': 'application/json' },
      body: JSON.stringify({ commands: cmds }),
    });
    return await data;
  } catch (error) {
    console.log(error);
  }
}
const elevCount = [2, 2, 4];
let elevState = Array.from({ length: elevCount[problem] }, () => 'UP');
const limit = [5, 25, 25];
let cnt = -1;
async function move(token) {
  let data = await oncalls(token);
  let calls = data.calls;
  let elevators = data.elevators;
  // console.log(calls, elevators);
  let actionArray = Array.from({ length: elevCount[problem] }, () => 0);
  let visited = []; // ENTER 인원 중복 체크
  let visited2 = []; // EXIT 인원 중복 체크

  for (elevator of elevators) {
    switch (elevator.status) {
      case 'STOPPED':
        // 탈 손님있으면 OPEN
        for (call of calls) {
          if (call.start === elevator.floor && elevator.passengers.length < 8) {
            actionArray[elevator.id] = { elevator_id: elevator.id, command: 'OPEN' };
            break;
          }
        }
        // 내릴 손님있고, 상태 안정해진 경우, OPEN
        if (!actionArray[elevator.id]) {
          for (passenger of elevator.passengers) {
            if (passenger.end === elevator.floor) {
              actionArray[elevator.id] = { elevator_id: elevator.id, command: 'OPEN' };
              break;
            }
          }
        }
        // 최고층,최저층이 아니고, 상태가 안정해진 경우, 저장된 방향으로 계속 이동
        if (1 < elevator.floor && elevator.floor < limit[problem] && !actionArray[elevator.id]) {
          actionArray[elevator.id] = { elevator_id: elevator.id, command: elevState[elevator.id] };
          continue;
        }
        // 최저층인경우, 최고층인 경우, 상태가 안정해진 경우, 방향 전환
        if (elevator.floor === 1 && !actionArray[elevator.id]) {
          elevState[elevator.id] = 'UP';
          actionArray[elevator.id] = {
            elevator_id: elevator.id,
            command: elevState[elevator.id],
          };
          continue;
        }
        if (elevator.floor === limit[problem] && !actionArray[elevator.id]) {
          elevState[elevator.id] = 'DOWN';
          actionArray[elevator.id] = {
            elevator_id: elevator.id,
            command: elevState[elevator.id],
          };
          continue;
        }
        break;
      case 'UPWARD':
        // 탈 손님있으면 STOP
        for (call of calls) {
          if (call.start === elevator.floor && elevator.passengers.length < 8) {
            if (elevState[elevator.id] === 'UP' && call.end - call.start >= 1)
              actionArray[elevator.id] = { elevator_id: elevator.id, command: 'STOP' };
            break;
          }
        }
        // 내릴 손님있고, 상태 안정해진 경우, STOP
        if (!actionArray[elevator.id]) {
          for (passenger of elevator.passengers) {
            if (passenger.end === elevator.floor) {
              actionArray[elevator.id] = { elevator_id: elevator.id, command: 'STOP' };
              break;
            }
          }
        }
        // 최고층인 경우 STOP
        if (elevator.floor === limit[problem] && !actionArray[elevator.id]) {
          actionArray[elevator.id] = { elevator_id: elevator.id, command: 'STOP' };
          continue;
        }

        // 최고층 아닌 경우 UP
        if (elevator.floor < limit[problem] && !actionArray[elevator.id]) {
          actionArray[elevator.id] = { elevator_id: elevator.id, command: 'UP' };
          continue;
        }
        break;
      case 'DOWNWARD':
        // 탈 손님있으면 STOP
        for (call of calls) {
          if (call.start === elevator.floor && elevator.passengers.length < 8) {
            if (elevState[elevator.id] === 'DOWN' && call.end - call.start < 0)
              actionArray[elevator.id] = { elevator_id: elevator.id, command: 'STOP' };
            break;
          }
        }
        // 내릴 손님있고, 상태 안정해진 경우, STOP
        if (!actionArray[elevator.id]) {
          for (passenger of elevator.passengers) {
            if (passenger.end === elevator.floor) {
              actionArray[elevator.id] = { elevator_id: elevator.id, command: 'STOP' };
              break;
            }
          }
        }
        // 최하층인 경우 STOP
        if (elevator.floor === 1 && !actionArray[elevator.id]) {
          actionArray[elevator.id] = { elevator_id: elevator.id, command: 'STOP' };
          continue;
        }
        // 최하층 아닌 경우 DOWN
        if (elevator.floor > 1 && !actionArray[elevator.id]) {
          actionArray[elevator.id] = { elevator_id: elevator.id, command: 'DOWN' };
          continue;
        }
        break;
      case 'OPENED':
        // 탈 사람 있다 ENTER
        let temp = [];
        for (call of calls) {
          if (call.start === elevator.floor && elevator.passengers.length < 8) {
            if (elevator.passengers.length + temp.length < 8 && !visited.includes(call.id)) {
              temp.push(call.id);
              visited.push(call.id);
            }
          }
        }
        if (temp.length)
          actionArray[elevator.id] = { elevator_id: elevator.id, command: 'ENTER', call_ids: temp };

        // 내릴 손님있고, 상태 안정해진 경우, EXIT
        temp = [];
        if (!actionArray[elevator.id]) {
          for (passenger of elevator.passengers) {
            if (passenger.end === elevator.floor && !visited2.includes(passenger.id)) {
              temp.push(passenger.id);
              visited2.push(passenger.id);
            }
          }
          if (temp.length)
            actionArray[elevator.id] = {
              elevator_id: elevator.id,
              command: 'EXIT',
              call_ids: temp,
            };
        }
        // 탈 사람, 내릴사람 없거나 용량 꽉차면 CLOSE
        if (!actionArray[elevator.id]) {
          actionArray[elevator.id] = { elevator_id: elevator.id, command: 'CLOSE' };
        }
        break;
      default:
        break;
    }
  }
  // console.log('action start', actionArray);
  let res = await action(token, actionArray);
  cnt++;
  try {
    return await res.json();
  } catch (error) {
    console.log(error);
    return { is_end: false };
  }
}

async function simulate(p, count) {
  user = 'tester';
  ret = await start(user, p, count);
  token = ret['token'];
  console.log('Token for %s is %s', user, token);

  while (true) {
    let res = await move(token);
    if (res.is_end) {
      console.log('완료');
      console.log('TimeStamp: ', cnt);
      break;
    }
  }
}
console.log('문제번호:', problem, '엘리베이터 수:', elevCount[problem]);
simulate(problem, elevCount[problem]);
