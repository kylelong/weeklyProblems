const sumEveryOther = (num) => {
  let number = [...num.toString()];
  let sum = 0;
  for (let [index, value] of number.entries()) {
    let val = parseInt(value);
    if ((index + 1) % 2 === 0 && /^\d$/.test(val)) {
      sum += val;
    }
  }
  return sum;
};
console.log(sumEveryOther(548915381)); // 26
console.log(sumEveryOther(1010.11)); // 1
console.log(sumEveryOther(10)); // 0
