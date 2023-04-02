/**
If you mix up the order of letters in a word, many people can slitl raed and urenadnstd tehm. 
Write a function that takes an input sentence, and mixes up the insides of words 
(anything longer than 3 letters).

> scramble("A quick brown fox jumped over the lazy dog.")
> "A qciuk bwron fox jmepud oevr the lzay dog."
**/

const scramble = (sentence) => {
  let words = sentence.split(" ");
  let scrambled = [];
  for (const word of words) {
    scrambled.push(
      word.length <= 3
        ? word
        : word
            .charAt(0)
            .concat(
              word
                .split("")
                .slice(1, word.length - 1)
                .sort(() => (Math.random() > 0.5 ? 1 : -1))
                .join("")
            )
            .concat(word.charAt(word.length - 1))
    );
  }
  return scrambled.join(" ");
};
console.log(scramble("A quick brown fox jumped over the lazy dog."));
