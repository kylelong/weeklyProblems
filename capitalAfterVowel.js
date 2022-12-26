const capitalAfterVowel = (phrase) => {
  if (phrase.length === 0) return;
  let indices = [];
  for (let i = 1; i < phrase.length; i++) {
    if (/^[aeiou]$/.test(phrase[i - 1]) && !/^[aeiou]$/.test(phrase[i])) {
      indices.push(i);
    }
  }
  let copy = [];
  phrase.split("").map((elem, index) => {
    indices.includes(index)
      ? copy.push(elem.toLocaleUpperCase())
      : copy.push(elem);
  });
  return copy.join("");
};
console.log(capitalAfterVowel("hello world")); //heLlo woRld
console.log(capitalAfterVowel("xaabeuekadii")); //xaaBeueKaDii
