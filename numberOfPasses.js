let n = 7;
let numberOfPasses = 3;

// 0 means open, 1 means closed

const passDoors = (n, numberOfPasses) => {
	if(numberOfPasses === 0 || n === 0) return 0;
	if(numberOfPasses === 1) return n;

	let doors = Array(n).fill(1);
	for(let i = 1; i <= numberOfPasses; i++) {
		for(let index = 0; index < doors.length; index++) {
			if( (index + 1) % i == 0 ) {
				doors[index] = !doors[index];
			}
		}
	}
	return doors.filter(item => item === false).length;
}

console.log(passDoors(n, numberOfPasses)); // 4