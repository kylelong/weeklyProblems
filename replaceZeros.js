const replaceZeros = (string) => {
  let queue = [],
    result = [];
  [...string].forEach((s) => queue.push(s));

  while (queue.length > 0) {
    let number = queue.shift();
    if (number === "0") {
      let zeroCount = 1;
      while (number === "0") {
        number = queue[0];
        if (number === "0") {
          zeroCount++;
          queue.shift();
        }
      }
      result.push(zeroCount);
    } else {
      result.push(number);
    }
  }
  return result.join("");
};
console.log(replaceZeros("1234500362000440")); // 1234523623441
console.log(replaceZeros("123450036200044")); // 123452362344
console.log(replaceZeros("000000000000")); // 12
console.log(replaceZeros("123456789")); // 123456789
