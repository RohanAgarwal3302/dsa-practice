def maximumWealth(accounts: list[list[int]]):
        v=[]
        for i in range(len(accounts)):
            w=0
            for val in accounts[i]:
                w=w+val
            v.append(w)
        return max(v)

print(maximumWealth([[1,2,3],[3,2,1]]))