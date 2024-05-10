import string

def wrap(s, l):
    alphaNum = set(string.ascii_letters + string.digits)
    i, n, res = 0, len(s), ""
    while i < n:
        slice, currIndex, nextIndex = s[i:i+l], i+l-1, i+l+1
        if currIndex < n and s[currIndex] in alphaNum and nextIndex < n and s[nextIndex] != " ":
            slice = s[i:currIndex] + "-"
            i += currIndex
        else:
            i += l
        if slice[0] not in alphaNum or slice[0] == " ":
            slice = "-" + slice
        res += slice + "\n"
    return res

wrap("Hello, world! I am hungry.",10)