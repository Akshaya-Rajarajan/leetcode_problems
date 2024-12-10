def substrs(S):
    # "ma$$laya(lam"
    list1 = []
    length = len(S)
    for l in range(length):
        r = l+1
        while r< length+1:
            list1.append(S[l:r])
            r += 1
    return list1

S = "aksha"
substrList = substrs(S)
set(substrList)    