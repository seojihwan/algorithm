class DefaultDict {
  constructor(defaultInit) {
    return new Proxy(
      {},
      {
        get: (target, name) =>
          name in target
            ? target[name]
            : (target[name] =
                typeof defaultInit === "function"
                  ? new defaultInit().valueOf()
                  : defaultInit),
      }
    );
  }
}

/*
new DefaultDict(Array);
{'0': []}

new DefaultDict(new DefaultDict(Array));
{'0': {'0': []}}
*/

exports = DefaultDict;
