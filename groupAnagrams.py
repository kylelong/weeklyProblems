from collections import defaultdict

def groupAnagrams(words):
    groups = defaultdict(list)
    for w in words:
        sorted_word = tuple(sorted(w))
        groups[sorted_word].append(w)
    return list(groups.values())

assert groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
assert groupAnagrams(["vote", "please"]) == [["vote"],["please"]]
assert groupAnagrams(["debitcard", "badcredit"]) == [["debitcard", "badcredit"]]