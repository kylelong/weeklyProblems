squares = lambda x : sum(i ** 2 for i in range(x + 1))
assert squares(5) == 55
assert squares(10) == 385
assert squares(25) == 5525
assert squares(100) == 338350