/** 
 * You’re given a string of characters that are only 2s and 0s. 
 * Return the index of the first occurrence of “2020” without 
 * using the indexOf (or similar) function, and -1 if it’s not found in the string.
 **/
function find2020(year){
    let str = "";
    for(let i= 0,j=3; j<year.length; j++,i++){
        str = "";
        for(let k = i; k <=j; k++){
            str += year.charAt(k)
        }
        if(str == "2020") return i;
    }
    return -1;
}
console.log(find2020("2220000202220020200"))//14