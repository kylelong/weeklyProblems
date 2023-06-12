# Write a function to find out whether the binary representation of a number is palindrome or not.

def binaryPal(number)
	binary = number.to_s(2)
	binary.eql?(binary.reverse)
end

puts(binaryPal(5)) # true
puts(binaryPal(10)) # false