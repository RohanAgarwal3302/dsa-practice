# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# haystack = "sadbutsad", needle = "sad"
# "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# completed

def strStr(haystack: str, needle: str):
    j=0
    while j<=(len(haystack)-len(needle)):
        if haystack[j]==needle[0]:
            index=j
            for i in range(len(needle)):
                if haystack[j+i]!=needle[i]:
                    j+=1
                    break
                print(j,i)
            else: 
                return index
        else: j+=1
    return -1

def strStr(haystack: str, needle: str): ## faster and less memory required
        try :
            return haystack.find(needle)
        except ValueError:
            return -1

print(strStr("butsad","sad"))