# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# nums = [2,5,1,3,4,7], n = 3
# Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

# completed

def shuffle(nums: list[int], n: int):
        x=nums[:n]
        y=nums[n:]
        ar=[]
        for i in range(n):
            ar.append(x[i])
            ar.append(y[i])
        return ar

def shuffle(nums: list[int], n: int):
        ar=[]
        j=0
        for i in range(n):
            ar.insert(j,nums[i])
            ar.insert(j+1,nums[i+n])
            j+=2
        return ar

def shuffle(nums: list[int], n: int):
        ar=[]
        for i in range(n):
            ar.append(nums[i])
            ar.append(nums[i+n])
        return ar
    
print(shuffle([2,5,1,3,4,7],3))

