def kidsWithCandies(self, candies: list[int], extraCandies: int):
    ans=[]
    for c in candies:
        if c+extraCandies>=max(candies):
            ans.append(True)
        else:
            ans.append(False)
    return ans

