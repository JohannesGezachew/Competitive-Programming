class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if modified:
                    return False
                if i == 1 or nums[i] >= nums[i - 2]:

                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                modified = True
        return True
