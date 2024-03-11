'''
> wordLengthProduct(["fish","fear","boo","egg","cake","abcdef"])
> 16 // "fish" and "cake"

> wordLengthProduct(["a","aa","aaa","aaaa"])
> 0 // all of them share "a"
'''
# Given a string array, find the maximum product of word lengths where the words don't share any letters.

def wordLengthProduct(words):
    n = len(words)
    char_set = [set(words[i]) for i in range(n)]
    print(char_set)


print(wordLengthProduct(["fish","fear","boo","egg","cake","abcdef"]))
print(wordLengthProduct(["a","aa","aaa","aaaa"]))