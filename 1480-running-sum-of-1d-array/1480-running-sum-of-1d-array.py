class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        pre = 0
        for num in nums:
            pre += num
            ans.append(pre)
        return ans