def numBalanced(str)
	stack = []
	num = 0
	str.each_char do |c|
		if c.eql?("(")
			stack.push(c)
		else
			if stack.empty?
				num += 1
			elsif stack[stack.length - 1].eql?("(")
				stack.pop
			end
		end	
	end
	stack.length + num
end
puts numBalanced('()') # 0
puts numBalanced('(()') # 1
puts numBalanced('))()))))()') # 6
puts numBalanced(')))))') # 5