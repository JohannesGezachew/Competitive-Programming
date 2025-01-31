class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = []
        x = num / 3
        if num % 3 == 0:
            ans.append(x-1)
            ans.append(x)
            ans.append(x+1)
        return ans


     
        
        