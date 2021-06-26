const n = 5;

const root = [0, 0];

const g = [...Array(n)].map(() => [...Array(n)].map(() => 0));

let stack = [root];

const visited = [...Array(n)].map(() => [...Array(n)].map(() => 0));

while (stack.length) {
  const node = stack.pop();
  const [sy, sx] = node;
  if (!visited[sy][sx]) {
    visited[sy][sx] = 1;

    for (const [ay, ax] of [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ]) {
      const [dy, dx] = [sy + ay, sx + ax];

      if (0 <= dy && dy < n && 0 <= dx && dx < n && !visited[dy][dx]) {
        stack.push([dy, dx]);
      }
    }

    console.log(node);
  }
}
