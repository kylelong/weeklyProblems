def spreadsheet(column)
	a = 65
	return column[0].ord - a + 1 unless column.length > 1
	num = 26 * (column[0].ord - a + 1)
	for i in 1...column.length - 1 
		c = column[i];
		num += c.ord - a + 26 ** (i + 1)
	end
	num += column[-1].ord - a + 1
	num
end
puts spreadsheet("A"); # 1
puts spreadsheet("B"); # 2
puts spreadsheet("C"); # 3
puts spreadsheet("Z"); # 26
puts spreadsheet("AA"); # 27
puts spreadsheet("AB"); # 28
puts spreadsheet("BA"); # 53
puts spreadsheet("PP"); # 432
puts spreadsheet("AAA"); # 703
puts spreadsheet("UK"); # 557
puts spreadsheet("CA"); # 79