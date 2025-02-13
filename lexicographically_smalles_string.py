# Given a string s containing only digits, return the 
# lexicographically smallest string that can be obtained after swapping 
# adjacent digits in s with the same parity at most once.

# Digits have the same parity if both are odd or both are even. 
# For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

# s = "45320"
# ans: "43520"

# completed

def getSmallestString(s: str) -> str:
    s=list(s)
    swapped=False
    i=0
    while i<(len(s)-1):
        if int(s[i])%2==int(s[i+1])%2:
            if s[i]>s[i+1]:
                s[i],s[i+1]=s[i+1],s[i]
                return (lambda lst: "".join(a for a in lst))(s)
        i+=1    
    return (lambda lst: "".join(a for a in lst))(s)

print(getSmallestString("45320"))