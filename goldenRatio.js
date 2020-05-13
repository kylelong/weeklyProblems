//Week of 5/10
/*
Golden ratio: (https://www.mathsisfun.com/numbers/golden-ratio.html)
the long part divided by the short part == the whole length divided by the long part
(a/b) = (a+b / a)
*/
//round to 2 decimal places
function round (a) {
  return Math.round(a * 100) / 100
}
//Determines if two numbers are in the golden ration
function goldenRatio (a, b) {
  let max = Math.max(a, b)
  let min = Math.min(a, b)
  return round(max / min) == round((a + b) / max)
}
console.log(goldenRatio(61.8, 38.2)) //true
