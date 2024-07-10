class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        union = set()
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                union.add(j)
        if left in union and right in union:
            for a in range(left,right+1):
               if a not in union:
                return False
            else:
                return True
        else:
            return False
        



        

        
        