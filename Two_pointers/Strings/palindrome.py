def ispalindrome(S):
    # "ma$$laya(lam"
    l = 0
    r = len(S)-1
    while l<r:
        while l<r and not (S[l].isalnum()):
            l += 1
        while r>l and not (S[r].isalnum()):
            r -= 1
        if S[l].lower() != S[r].lower():
            return False
        l,r = l+1, r-1
    return True

S = "ma$$laya(lam"
value = ispalindrome(S)
value       
# check if only the alnum chars of the string form a palindrome.