#!/usr/bin/env ruby
=begin
Cassido's interview of the week problem 8/11/2019
Given strings n and m, find the minimum number of times n
 has to be repeated such that m is a substring of it
(and if it's not possible, return -1).
@param n string to extend
@param m string to check as substring of n once n is repeated i times
@return true/false depending on if n can be multiplied to be contain m as a substring
=end
def repeatedSubstring(n, m)
    for i in  1..(m.length * 2)
        n = n * i
        if n.include?(m)
            return i
        end
    end
    -1
end
puts repeatedSubstring('ab', 'cab')