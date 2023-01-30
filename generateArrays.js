let result = [];
const generateArrays = (num) => {
	helper(num);
	return result.reverse();

}
const helper = (num) =>{
	if(num === 0){
		return result;
	}
	let arr = [];
	for(let i = 1; i <= num; i++){
		arr.push(i);
	}
 	result.push(arr);
	return helper(num - 1);
}
console.log(generateArrays(4)); // [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]
console.log(generateArrays(1));  // [[1]]
