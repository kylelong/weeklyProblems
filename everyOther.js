/*
Given a string str containing only the characters x and y,
change it into a string such that there are no matching 
adjacent characters. You’re allowed to delete zero or more
 characters in the string. Find the minimum number of required deletions.
*/
function everyOther(s){
    let arr = s.split("");
    return arr.filter((elem,index) => arr[index - 1 ] !== elem).join("");
}
console.log(everyOther('xxyxxy')); //xyxy
console.log(everyOther('yyyyy')); //y