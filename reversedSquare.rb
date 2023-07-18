def reversedSquares(num)
    reversed = num.to_s.reverse.to_i
    return perfectSquare?(num) && perfectSquare?(reversed)
end
def perfectSquare?(num)
    return !fractional?(Math.sqrt(num))
end
def fractional?(num)
    return num % 1 != 0
end

puts reversedSquares(9)
puts reversedSquares(441)
puts reversedSquares(25)