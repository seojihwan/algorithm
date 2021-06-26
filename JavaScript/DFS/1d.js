const DefaultDict = require("../shared/DefaultDict");

const n = 5;

const root = 0;

const childNodes = new DefaultDict(Array);

for (const [s, e] of [
  [0, 1],
  [0, 4],
  [1, 2],
  [2, 3],
  [3, 4],
]) {
  if (!childNodes[s].includes(e)) {
    childNodes[s].push(e);
  }
}

let stack = [root];

const visited = [...Array(n).map(() => 0)];

while (stack.length) {
  const node = stack.pop();
  if (!visited[node]) {
    visited[node] = 1;
    for (const childNode of childNodes[node]) {
      stack.push(childNode);
    }
    console.log(node);
  }
}
