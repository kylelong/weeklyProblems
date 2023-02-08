def spreadsheet(column)
	num = 0
	column.each_char.with_index { |c, idx|
		num += c.ord - 65 + 26 ** idx
	}
	num
end
puts spreadsheet("A"); #1
puts spreadsheet("B"); #2
puts spreadsheet("C"); #3
puts spreadsheet("Z"); #26
puts spreadsheet("AA"); #27
puts spreadsheet("AB"); #28
puts spreadsheet("AAA"); #703