/**
Given an integer array arr, sort the integers in arr in ascending order by 
the number of 1’s in their binary representation and return the sorted array.

$ sortBits([0,1,2,3,4,5,6,7,8])
$ [0,1,2,4,8,3,5,6,7]
**/

/** 
Sorts a list of numbers by the number
of 1's in a number's binary representation
**/
function sortBits(list){
   list.sort(function (x, y){
   		let a = numOnes(x);
   		let b = numOnes(y);
   		if(a < b) return -1;
   		if(a > b) return 1;
   		return 0;
   });
   return list;
}
/**
Determines the number of ones 
in a number's binary representation
**/
function numOnes(num){
	let count = 0;
	let list = []
	while(num !== 0){
		list.unshift(num % 2 == 0 ? 0 : 1);
		num = Math.floor(num /= 2);
	}
	return list.filter(elem => elem == 1).length;
}
console.log(sortBits([0,1,2,3,4,5,6,7,8])); //[0,1,2,4,8,3,5,6,7]
