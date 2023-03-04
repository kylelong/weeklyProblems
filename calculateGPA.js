let scale = {
  A: 4.0,
  "A-": 3.7,
  "B+": 3.3,
  B: 3,
  "B-": 2.7,
  "C+": 2.3,
  C: 2.0,
  "C-": 1.7,
  "D+": 1.3,
  D: 1,
  "D-": 0.7,
  F: 0,
};
const calculateGPA = (grades) => {
  let sum = grades.reduce(
    (accumulator, currentValue) => accumulator + scale[currentValue],
    0
  );
  return sum / grades.length;
};
console.log(calculateGPA(["A"])); // 4
console.log(calculateGPA(["F", "F", "F"])); // 0
console.log(calculateGPA(["A", "A-", "B+", "B", "B-"])); // 3.34
console.log(calculateGPA(["A", "B+", "C-", "A"])); // 3.325
