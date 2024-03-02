class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        re=[]
        for i in range(len(operations)):
            if operations[i] == "+":
                re.append(re[-1] + re[-2])
            elif operations[i] == "D":
                re.append(re[-1] * 2)
            elif operations[i] == "C":
                if len(operations) > 1:
                    re.pop()
            else:
                re.append(int(operations[i]))
        
        return(sum(re))
            
            