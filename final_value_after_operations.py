def finalValueAfterOperations(operations: list[str]):
        x=0
        for v in operations:
            if v=="X++" or v=="++X":
                x+=1
            if v=="--X" or v=="X--":
                x-=1
        return x