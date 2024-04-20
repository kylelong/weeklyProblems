# https://buttondown.email/cassidoo/archive/the-bird-a-nest-the-spider-a-web-man-friendship/

def uniqueSubstr(s):
    l = r = res = 0
    chars, k = {}, 2
    while r < len(s):
        c = s[r]
        size = len(chars)
        if c in chars:
            if size <= k:
                chars[c] = chars[c] + 1
        else:
            if size < k:
                chars[c] = chars.get(c, 0) + 1
            else:
                if size > 1: res = max(res, r - l)
                while len(chars) == k:
                    left_char = s[l]
                    if left_char in chars:
                        chars[left_char] = chars[left_char] - 1
                        if chars[left_char] == 0:
                            del chars[left_char]
                    l += 1
                chars[c] = 1
                
        r += 1 
        if size > 1: res = max(res, r - l)
    return res

assert(uniqueSubstr('eceba') == 3)
assert(uniqueSubstr('ccaabbb') == 5)
assert(uniqueSubstr('abcabcabc') == 2)
assert(uniqueSubstr('') == 0)
assert(uniqueSubstr('aaaaaa') == 0)
assert(uniqueSubstr('aabbc') == 4)
assert(uniqueSubstr('cabbbc') == 4)
assert(uniqueSubstr('abcdef') == 2)
assert(uniqueSubstr('ababababab') == 10)