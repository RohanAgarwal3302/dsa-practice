# Given a string s, find the length of the longest substring without repeating characters.

# s = "abcabcbb"
# ans: 3
# Explanation: The answer is "abc", with the length of 3.

# completed

def lengthOfLongestSubstring(s: str) -> int:
    res=""
    length=[]
    for char in s:
        if char in res:
            res=res[res.index(char)+1:]+char
        else:
            res+=char
        length.append(len(res))
    try:
        return max(length)
    except Exception as e:
        return 0

def lengthOfLongestSubstring(s: str) -> int:
    if s=='':
        return 0
    res=""
    length=[]
    for char in s:
        if char in res:
            res=res[res.index(char)+1:]+char
        else:
            res+=char
        length.append(len(res))
    return max(length)

def lengthOfLongestSubstring(s: str) -> int:
    if s=='':
        return 0
    res=""
    length=0
    for char in s:
        if char in res:
            res=res[res.index(char)+1:]+char
        else:
            res+=char
        if len(res)>length:
            length=len(res)
    return length

print(lengthOfLongestSubstring("abcabcbb"))