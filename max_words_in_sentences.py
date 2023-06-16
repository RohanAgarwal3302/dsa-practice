def mostWordsFound(sentences:list[str]):
    import re
    m=0
    for s in sentences:
        res = re.findall(r'\w+', s)
        m=max(m,len(res))
    return m

def mostWordsFound(sentences:list[str]):
    m=0
    for s in sentences:
        m=max(m,len(s.split()))
    return m
    
print(mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"]))