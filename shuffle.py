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
        for i in range(0,n):
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

