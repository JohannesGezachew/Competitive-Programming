class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        if n < 8:
            y = 0
            for i in range(n+1):
                y += i
            
            return(y)
        else:
            left = 1
            count = 1
            m = 7
            for i in range(n):
                if left == m:
                    ans += left
                    count += 1
                    m += 1
                    left = count
                    continue
                else:
                    ans += left
                    left += 1
        return ans
