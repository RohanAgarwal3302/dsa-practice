# a=76
# b=46

# a=a^b
# b=a^b
# a=a^b

# print(a,b)

# x=1
# y1=1
# y2=2
# y3=3
# a=y1^x
# b=y2^a
# c=y3^b

# print(x,a,b,c)

def decode(encoded: list[int], first: int):
        arr=[first]
        for v in encoded:
            first=v^first
            arr.append(first)
        return arr

print(decode([1,2,3],1))