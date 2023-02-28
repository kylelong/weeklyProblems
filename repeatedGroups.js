/**
> repeatedGroups([1, 2, 2, 4, 5])
	[[2, 2]]

> repeatedGroups([1, 1, 0, 0, 8, 4, 4, 4, 3, 2, 1, 9, 9])
	[[1, 1], [0, 0], [4, 4, 4], [9, 9]]
**/

const repeatedGroups = (numbers) => {
 	let l = 0, r = 1;
 	let groups = [];
 	while (l < numbers.length){
 		if(numbers[r] === numbers[l]){
 			while(numbers[r] === numbers[l]){
 				r++;
 			}
 			groups.push(numbers.slice(l,r));
 			l = r;
 			r++;
 		} else {
 			l++;
 			r++;
 		}

 	}
	
	return groups;

}
console.log(repeatedGroups([1, 2, 2, 4, 5]));
console.log(repeatedGroups([1, 1, 0, 0, 8, 4, 4, 4, 3, 2, 1, 9, 9])); 