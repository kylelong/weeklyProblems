=begin
Let's say you have some special bags that can only hold up to 3kgs of weight.
Given an array of integers (where each integer is between 1 and 3) that
represent weights, determine how many bags you need to carry all of them.

@param arr the array representing the weight of the bags
@return the number of bags needed to carry all weights
=end
def specialBag(arr)
    bags = (arr.sum.to_f / 3).ceil
    s = bags > 1 ? "bags" : "bag"
    "#{bags} " << s
end
puts specialBag([1,1,3,2]) #3 bags
puts specialBag([2,2,2,1,3,1]) #4 bags
puts specialBag([1,1,1]) #1 bag
