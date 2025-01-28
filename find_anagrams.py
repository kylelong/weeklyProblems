from typing import *

def findAnagrams(s: str, p: str) -> List[int]:
        if len(p) > len(s): return []

        s_map, p_map = {}, {}
        res = []
        l = 0
        n = len(p)

        for c in p:
            p_map[c] = p_map.get(c, 0) + 1

        for r in range(len(s)):
            c = s[r]
            s_map[c] = s_map.get(c, 0) + 1

            if r - l + 1 > n:
                s_map[s[l]] -= 1
                if s_map[s[l]] == 0:
                    del s_map[s[l]]
                l += 1
            
            if r - l + 1 == n and s_map == p_map:
                res.append(l)
        return res

assert findAnagrams("cbaebabacd", "abc") == [0,6]
assert findAnagrams("fish", "cake") == []
assert findAnagrams("abab", "ab") == [0,1,2]