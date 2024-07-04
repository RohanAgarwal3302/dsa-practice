# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

# operations = ["--X","X++","X++"]
# ans: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.

# complete

def finalValueAfterOperations(operations: list[str]):
    x=0
    for v in operations:
        if v=="X++" or v=="++X":
            x+=1
        if v=="--X" or v=="X--":
            x-=1
    return x

import re

def finalValueAfterOperations(operations: list[str]):
    sum
    for op in operations:
        if re.search(r'\B-',op):
            sum-=1
        else:
            sum+=1
    return sum
    
print(finalValueAfterOperations(["--X","++X","X--"]))