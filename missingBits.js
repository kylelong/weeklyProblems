/**
missingBits([1,2,3,4,20,21,22,23])
"[1,2,3,4,...,20,21,22,23]"

missingBits([1,2,3,5,6])
"[1,2,3,4,5,6]"

missingBits([1,3,20,27])
"[1,2,3,...,20,...,27]"
**/
const missingBits = (nums) => {
	// assuming sorted in ascending order
	let res = [];
	for(i = 0; i <= nums.length - 1; i++){
		let curr = nums[i], next =  nums[i + 1];
		res.push(curr);
		if(next - curr == 2){
		 res.push(next - curr);
		} else if (next - curr > 2){
			res.push("...");
		} 
	}
	return "[" + res.join(",") + "]"
}
console.log(missingBits([1,2,3,4,20,21,22,23]));
console.log(missingBits([1,2,3,5,6]));
console.log(missingBits([1,3,20,27]));