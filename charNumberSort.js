/** 
Sort an array of strings based on the number of distinct characters t
hat occur in the word (followed by the length of the word).

Example:
$ charNumSort([“Bananas”, “do”, “not”, “grow”, “in”, “Mississippi”])
$ do in not Mississippi Bananas grow
**/
let arr = ["Bananas", "do", "not", "grow", "in", "Mississippi"];
arr.sort((a, b) => {
  let setA = new Set(a).size;
  let setB = new Set(b).size;
  if (setA < setB) {
    return -1;
  } else if (setB > setA) {
    return 1;
  }
  return a.length - b.length;
});
console.log(arr); //[ 'do', 'in', 'not', 'grow', 'Bananas', 'Mississippi' ]
