def wrapGifts(gifts, width):
    gifts.sort()
    total = count = 0
    for gift in gifts:
        if gift + total <= width:
            total += gift
            count += 1
        else:
            break
    return count

print(wrapGifts([2, 3, 4, 5], 7))  # Output: 2
print(wrapGifts([1, 1, 1, 1, 1, 1, 1], 3))  # Output: 3
print(wrapGifts([1, 2, 3, 4, 5], 6))  # Output: 3