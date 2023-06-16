def strchk(major:str,minor:str,i:int):
    index=i
    for c in minor:
        if c!=major[i]:
            i+=1
            return
        i+=1    
    return index,i

def strStr(haystack: str, needle: str):
    index=0
    i=0
    result=[]
    while i!=len(haystack):
        index=i
        for c in needle:
            if c!=haystack[i]:
                i+=1
                break
            i+=1
        
        

    if len(result)==0:
        return -1
    return result

print(strchk("sadbutsad","sad",0))

# v="str"
# print(v[0])