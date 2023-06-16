def numberOfSteps(num: int):
        k=0
        while num!=0:
            if num%2==1:
                num-=1
            else:
                num//=2
            k+=1
        return k