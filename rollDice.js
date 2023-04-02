/**
 * Given a string in dice notation, return a random integer you can get by rolling those dice.
 * https://en.wikipedia.org/wiki/Dice_notation
 */
const rollDice = (notation) => {
  let regex = /[-\/*+]/;
  if (regex.test(notation)) {
    let combos = notation.split(regex);
    let operators = notation.split("").filter((el) => regex.test(el));
    let combo = combos[0],
      parts = combo.split("d"),
      dice = parseInt(parts[0]);
    let sides = parseInt(parts[1]),
      sum = roll(dice, sides);
    for (let i = 1; i < combos.length; i++) {
      combo = combos[i];
      let operator = operators[i - 1];
      parts = combo.split("d");
      dice = parseInt(parts[0]);
      sides = parseInt(parts[1]);

      if (operator === "-") {
        sum -= roll(dice, sides);
      } else if (operator === "+") {
        sum += roll(dice, sides);
      } else if (operator === "/") {
        sum /= roll(dice, sides);
      } else {
        sum *= roll(dice, sides);
      }
    }
    return sum;
  } else {
    // AdX format
    let parts = notation.split("d");
    let dice = parseInt(parts[0]);
    let sides = parseInt(parts[1]);
    return roll(dice, sides);
  }
};

const roll = (dice, sides) => {
  let rolls = Array(dice)
    .fill(null)
    .map(() => Math.floor(Math.random() * sides) + 1);
  let rollSum = rolls.reduce((i, a) => i + a);
  return rollSum;
};
console.log(rollDice("4d4"));
console.log(rollDice("3d20"));
console.log(rollDice("1d8+2d10"));
