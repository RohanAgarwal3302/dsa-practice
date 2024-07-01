# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# height = [1,8,6,2,5,4,8,3,7]
# ans: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# complete

def maxArea(height: list[int]):
    i,j=0,len(height)-1
    area=0
    while i!=j:
        if height[i]<height[j]:
            if i>0:
                if height[i]<height[i-1]:
                    i+=1
                    continue          
            a=height[i]*(j-i)
            i+=1
        else:
            if j<len(height)-1:
                if height[j]<height[j+1]:
                    j-=1
                    continue
            a=height[j]*(j-i)
            j-=1
        if a>area:
            area=a
    return area

print(maxArea([1,8,6,2,5,4,8,3,7]))