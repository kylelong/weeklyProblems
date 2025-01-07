# Find all permutations in a string 

def permute(str):

    res = []

    def backtrack(curr, visited):

        if len(curr) == len(str):
            res.append(''.join(curr))
            return
        for i, c in enumerate(str):
            if visited[i] is True:
                continue

            curr.append(c)
            visited[i] = True
            backtrack(curr, visited)
            visited[i] = False
            curr.pop()

    backtrack([], [False] * len(str))
    return res

assert permute("abc") == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']