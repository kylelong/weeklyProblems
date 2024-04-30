
# https://buttondown.email/cassidoo/archive/sometimes-it-takes-a-long-time-to-sound-like/

def translateRightShift(s):
    ANSI, res = r"1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./", ""
    keyMap = {v:k for k, v in enumerate(ANSI)}
    indexMap = {v:k for k,v in keyMap.items()}
    for c in s.lower():
        if c == ' ':
            res += " "
            continue
        prev = indexMap[keyMap[c] - 1]
        res += prev
    return res
assert(translateRightShift(';p; epeor') == "lol wowie")
assert(translateRightShift('ejp s, o') == "who am i")
assert(translateRightShift(',u ms,r od lu;r/') == "my name is kyle.")
assert(translateRightShift('JR;;P') == "hello")