def compress(letters):
    l, res = 0, []
    for r in range(len(letters)):
        if letters[l] != letters[r]:
            res.append(letters[l])
            freq = r - l 
            if freq > 1:
                res.append(str(freq))
            l = r
    res.append(letters[l])
    freq = r - l + 1
    if freq > 1:
        res.append(str(freq))
    return res


assert compress(["a", "b", "b", "b", "c"]) == ["a", "b", "3", "c"]
assert compress(["a", "a", "b", "b", "c", "c", "c"]) == ["a", "2", "b", "2", "c", "3"]
assert compress(['a']) == ['a']
assert compress(['a', 'b', 'c']) == ['a', 'b', 'c']
assert compress(["a", "a", "b", "b", "c"]) == ["a", "2", "b", "2", "c"]