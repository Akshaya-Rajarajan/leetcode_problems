def longestsubstrs(S):
    charSet = set()
    l = 0
    length = len(S)
    res = 0
    for r in range(length):
        while S[r] in charSet:
            charSet.remove(S[l])
            l += 1
        charSet.add(S[r])
        res = max(res, len(charSet))
    return res

S = "abcabcbb"
length = longestsubstrs(S)
   
length    