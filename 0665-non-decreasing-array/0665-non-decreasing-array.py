class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count  = 0
        if len(nums) < 2:
            return True
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                count += 1
            else:
                print(nums[i])
                print(nums.pop(i))
                if nums == sorted(nums):
                    return True
                else:return False

        print(count)
        print(len(nums))
        if count == (len(nums)-1):
            return True
        else:
            return False