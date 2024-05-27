# You are given a string s and an integer array indices of the same length. 
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

# s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# "codeleet" becomes "leetcode" after shuffling.

# completed

def restoreString(s: str, indices: list[int]):
        new_str=[0]*len(indices)
        i=0
        while i<len(indices):
            for c in s:
                new_str[indices[i]]=c
                i+=1
        return "".join(new_str)

print(restoreString("codeleet",[4,5,6,7,0,2,1,3]))