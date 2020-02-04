'''
Given that an "even word" is a word in which each character appears an even number of times,
write a function that takes in a string and returns the minimum number of letters to be 
removed to make that string an even word.

Add one for every character occurence that is odd to to opposite parity 
(removing 1 of the letters of a letter that has an odd count would make that count for the character even)

'''
def evenWord(s):
	dict = {}
	for c in s:
		if c not in dict:
			dict[c] = 1
		else:
			dict[c] = dict[c] + 1
	remove = 0
	for v in dict.values():
		if v % 2 != 0:
			remove = remove + 1
	return remove
print(evenWord("potato"))
print(evenWord('aaaa'))