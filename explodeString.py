def explodeString(s):
    char_map = {}
    groups = []
    for c in list(s):
        char_map[c] = 1 + char_map.get(c, 0)
        
    for k,v in char_map.items():
        if k != ' ':
            groups.append(k * v)
    return sorted(groups)
