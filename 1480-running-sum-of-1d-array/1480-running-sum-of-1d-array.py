class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        pre = 0
        for i in nums:
            pre += i
            ans.append(pre)
        return ans