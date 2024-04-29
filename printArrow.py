# https://buttondown.email/cassidoo/archive/all-creative-people-want-to-do-the-unexpected/
def printArrow(d,h):
    if d == "left":
        for i in range(h - 1,-h,-1):
             print(" " * abs(i) + "*")
    elif d == "right":
        for i in range(h + 2):
             print(" " * abs(i - (h + 1)) + "*") if i >= h  else print(" " * i + "*")
    elif d == "up":
        for i in range(1,h+1):
            print(" " * (h - i) + "* " * (i))
    elif d == "down":
        for i in range(h, -1, -1):
            print(" " * (h - i) + "* " * (i))


printArrow("left", 5)
printArrow('right', 3)
printArrow("up", 3)
printArrow("down", 5)