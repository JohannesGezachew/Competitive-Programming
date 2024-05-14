class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort(reverse=True)
        print(piles)
        left= 1
        s = 0
        while left < len(piles):
            s += piles[left]
            left += 2
            piles.pop()
        return(s)


