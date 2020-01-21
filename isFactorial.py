'''
Cassido's interview question of the week - 1/20/2020
Given a number, return true if the input is a factorial of any natural number.
'''
import math
def isFactorial(n):
	result = 1
	for i in range(1, int(math.ceil(math.sqrt(n))) + 1):
		result = i * result
		if result == n:
			return True
	return False
print(isFactorial(3))#False
print(isFactorial(6))#True
print(isFactorial(120))#True
print(isFactorial(15))#False
print(isFactorial(24))#True
print(isFactorial(720))#True