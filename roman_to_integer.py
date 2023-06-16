def romanToInt(s: str):##not done
    val=0
    arr=[]
    i=0
    for a in s:
        arr.append(a)
    while i<len(arr) and arr[i]!="I":
        if arr[i]=="V":
            val+=5
        elif arr[i]=="X":
            val+=10
        elif arr[i]=="L":
            val+=50
        elif arr[i]=="C":
            val+=100
        elif arr[i]=="D":
            val+=500
        else:
            val+=1000
        i+=1
    while i<len(arr):
        if arr[i]=="I":
            val+=1
        else:
            if arr[i]=="V":
                val+=3
            elif arr[i]=="X":
                val+=8
            elif arr[i]=="L":
                val+=39
            elif arr[i]=="C":
                val+=89
            elif arr[i]=="D":
                val+=399
            else:
                val+=899
        i+=1
    
    return val
   
print(romanToInt("XIX"))