class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        cycle = time // (n- 1)
        extra = time%(n - 1)

        if cycle % 2 == 0:
            return extra + 1
        else:
            return n - extra
        