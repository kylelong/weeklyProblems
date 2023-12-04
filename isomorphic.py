def isIsomorphic(s,t):
    def mapping(s):
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        return counts
    s_mapping = mapping(s)
    t_mapping = mapping(t)
    s_values = list(s_mapping.values())
    t_values = list(t_mapping.values())
    s_values.sort()
    t_values.sort()
    return s_values == t_values
