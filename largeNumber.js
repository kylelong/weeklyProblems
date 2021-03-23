/*
You’re given two integer arrays (n and m), and an integer k. Using the digits from n and m, return the largest number you can of length k.

n = [3,4,6,5]
m = [9,0,2,5,8,3]
k = 5
$ maxNum(n, m, k)
$ 98653
*/
function largeNumbers(n,m,k){
    let length = n.length + m.length;
    if(k > length) return [];
    return n.concat(m).sort().splice(length - k, length).reverse().join("");
}
console.log(largeNumbers([3,4,6,5],[9,0,2,5,8,3],5)); //98655