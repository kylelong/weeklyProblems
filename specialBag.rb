def specialBag(arr)
    bags = (arr.sum.to_f / 3).ceil
    s = bags > 1 ? "bags" : "bag"
    "#{bags} " << s
end
puts specialBag([1,1,3,2])
puts specialBag([2,2,2,1,3,1])
puts specialBag([1,1,1])