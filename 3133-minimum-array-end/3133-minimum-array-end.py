class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        i_x = 1
        increment = 1

        while increment <= n - 1:
            if (i_x & x) == 0:
                if increment & (n - 1):
                       res =  res | i_x
                increment = increment << 1
            i_x = i_x << 1

        return res