const fractionMath = (fractionOne, operation, fractionTwo) => {
  let one = fractionOne.toFraction();
  let two = fractionTwo.toFraction();
  let fraction = 0.0;
  switch (operation) {
    case "add":
      fraction = one + two;
      break;
    case "multiply":
      fraction = one * two;
      break;
    case "divide":
      fraction = one / two;
      break;
    case "subtract":
      fraction = one - two;
      break;
    default:
      fraction = 0.0;
  }
  let fractionString = fraction.toString();
  let mantissa = fractionString.substring(
    fractionString.indexOf("."),
    fractionString.length
  );
  let tens = Math.pow(10, mantissa.length - 1);
  let num = parseFloat(mantissa) * tens;
  let denom = tens;
  if (mantissa.length - 1 === 1) {
    num = fraction * 10;
  }

  if (denom % num === 0) {
    return `${1}/${denom / num}`;
  }
  const gcd = function (a, b) {
    if (!b) return a;
    return gcd(b, a % b);
  };
  let divisor = gcd(num, denom);
  return `${num / divisor}/${denom / divisor}`;
};

String.prototype.toFraction = function () {
  let content = this.split("/");
  let num = parseInt(content[0]);
  let denom = parseInt(content[1]);
  return num / denom;
};

console.log(fractionMath("3/4", "add", "3/4")); // 3/2
console.log(fractionMath("1/8", "multiply", "2/2")); // 1/8
