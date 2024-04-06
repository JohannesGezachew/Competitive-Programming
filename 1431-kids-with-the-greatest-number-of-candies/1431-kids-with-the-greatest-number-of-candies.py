class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = list(map(lambda x: x + extraCandies, candies))
        comparizer = max(candies)


        ans = [True if i >= comparizer else False for i in out]
        return(ans)
