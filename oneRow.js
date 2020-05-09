//Week of May 3rd 2020
//Given an array of words, return the words that can be typed using letters of only one row on a keyboard.
//QWERTY keyboard only
let rowOne = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
let rowTwo = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
let rowThree = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
//Looks at eache character of each word and dtermines if they are on the same row (in the saw array)
function oneRow (arr) {
  words = []
  for (let i = 0; i < arr.length; i++) {
    let word = arr[i]
    let singleRow = true

    //assumes word.length > 0
    let row = []
    if (rowOne.includes(word[0])) {
      row = rowOne
    }
    if (rowTwo.includes(word[0])) {
      row = rowTwo
    }
    if (rowThree.includes(word[0])) {
      row = rowThree
    }
    for (let j = 0; j < word.length; j++) {
      if (row.includes(word[j]) == false) {
        singleRow = false
        break
      }
    }
    if (singleRow) {
      words.push(word)
    }
  }
  console.log(words)
}
oneRow(['candy', 'doodle', 'pop', 'shield', 'lag', 'typewriter'])
