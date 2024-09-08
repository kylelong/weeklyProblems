# https://buttondown.com/cassidoo/archive/to-lead-people-walk-behind-them-lao-tzu/
def maxPairs(pairs):
    shoes, total = {}, 0
    for pair in pairs:
        foot, size = pair.split("-")
        size = int(size)
        if size in shoes:
            shoes[size][0 if foot == "L" else 1] += 1
        else:
            shoes[size] = [1,0] if foot == "L" else [0,1]

    for v in shoes.values():
        total += min(v[0], v[1])
    return total

assert maxPairs(["L-10", "R-10", "L-11", "R-10", "L-10", "R-11"]) == 3
assert maxPairs(["L-10", "L-11", "L-12", "L-13"]) == 0
assert maxPairs(["L-8", "L-8", "L-8", "R-8"]) == 1