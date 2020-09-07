#!/usr/bin/env ruby
=begin

=end
def logicGates(op, a, b = nil)
    if op.eql?("OR")
        a | b
    elsif op.eql?("AND")
        a & b
    elsif op.eql?("NOT")
        ~(a)
    elsif op.eql?("NAND")
        ~(a&b)
    elsif op.to_s.eql?("NOR")
       (a|b)
    elsif op.eql?("XOR")
        a ^ b
    elsif op.eql?("XNOR")
        (a & b) | (~a & ~b)
    end
end
#NOT
puts logicGates("NOT", 1, nil)
#NOR
puts logicGates("NOR", 0, 0)
#XOR
# puts logicGates("XOR", 0, 0)
# puts logicGates("XOR", 0, 1)
# puts logicGates("XOR", 1, 0)
# puts logicGates("XOR", 1, 1)
# #AND
# puts logicGates("AND", 0, 0)
# puts logicGates("AND", 0, 1)
# puts logicGates("AND", 1, 0)
# puts logicGates("AND", 1, 1)