class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        faranit = celsius * (1.8) + 32
        kelven = celsius + 273.15
        ans = [kelven,faranit]
        return ans
        

        