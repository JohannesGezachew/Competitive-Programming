class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = sorted(nums)
        left = 0
        sol = []
        for i in range(len(nums)):
            while x[left] < nums[i]:
                left +=1
            sol.append(left)
            left = 0
        return(sol)