const spreadsheet = (column) => {
	let num = column.charCodeAt(0) - 65 + 1 * 26;
	for(let i = 1; i < column.length; i++){
		num +=   column.charCodeAt(i) - 65 + 26 ** i;
	}
	return num;
}
console.log(spreadsheet("BA"));