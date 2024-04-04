class Solution:
    def largestGoodInteger(self, num: str) -> str:
        sol = []
        x = ["000","111","222","333","444","555","666","777","888","999"]
        for i in range(len(x)):
            if x[i] in num:
                sol.append(x[i])
        z = list(map(int, sol))
        if not z:
            return("")
        elif max(z) == 0:
            return("000")
        else:
            return(str(max(z)))


            

        
                