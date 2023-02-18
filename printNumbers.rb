
=begin
	Print the digits 0 through 100 without using the characters 
	0, 1, 2, 3, 4, 5, 6, 7, 8, 9 

	improved one-liner: ([].length..."d".ord).each {|i| puts i}
=end 
	
def printNumbers
	numbers = []
	chars = ["[", "\\", "]", "^", "_", "`", "a", "b", "c", "d",
			 ":", ";", "<", "=", ">", "?", "@"]
	chars.each {|char| numbers << char.ord}
	
	("A".."Z").each_with_index do |letter, index| 
		elements = [
			index, 
			letter.ord,
			letter.downcase.ord - letter.ord + index,
		 	letter.downcase.ord - letter.ord - index
		 ]
		 numbers.push(*elements)
	end

	numbers.sort.uniq
end
puts printNumbers
