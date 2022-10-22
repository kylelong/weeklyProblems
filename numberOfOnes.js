const numberOfOnes = (num) => {
	let sum = 0;
	for(let i = 0; i <= num; i++){
		sum +=  i.toString().split("").filter(number => number === '1').length;
	}
	return sum;
}
console.log(numberOfOnes(14));