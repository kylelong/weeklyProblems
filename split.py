class String(str):
    def split(self, c):
        res, substring = [], ''
        if len(c) == 0: return [c for c in self]
        for ch in self:
            if c == ch: 
                res.append(substring)
                substring = ''
            else:
                substring += ch
        if len(substring) > 0: res.append(substring)
        return res



string = String("This is so, so silly!")
assert string.split("") == ["T", "h", "i", "s", " ", "i", "s", " ", "s", "o", ",", " ", "s", "o", " ", "s", "i", "l", "l", "y", "!"]
assert string.split(",") == ["This is so", " so silly!"]
assert string.split(" ") == ["This", "is", "so,", "so", "silly!"]
