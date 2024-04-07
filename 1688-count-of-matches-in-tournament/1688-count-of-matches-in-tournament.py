class Solution:
    def numberOfMatches(self, n: int) -> int:
        count =0
        x = n
        for i in range(n):
            if x % 2==0:
                count += x/2
                x = x/2
            else:
                count +=(x-1) /2
                x = (x-1) /2 +1
        return(int(count))