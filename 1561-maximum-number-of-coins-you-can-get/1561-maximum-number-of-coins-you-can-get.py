class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        total_coins = 0
        n = len(piles)
        piles.sort()

        for i in range(n // 3, n, 2):
            total_coins += piles[i]
        
        return total_coins
