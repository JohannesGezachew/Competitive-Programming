class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans = numBottles
        emptyBottles = numBottles
        
        while emptyBottles >= numExchange:
            newBottles = emptyBottles // numExchange
            ans += newBottles
            emptyBottles = newBottles + (emptyBottles % numExchange) 
        
        return ans