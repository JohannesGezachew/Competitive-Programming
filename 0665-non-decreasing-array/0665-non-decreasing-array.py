class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count  = 0
        if len(nums) < 2:
            return True
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                count += 1
            else:

                temp = list(nums)
                x = nums.pop(i)
                if nums == sorted(nums):
                    return True
                else:
                    temp.pop(i+1)
                    print(temp)
                    if temp == sorted(temp):
                        return True
                    else:
                        return False


        if count == (len(nums)-1):
            return True
        else:
            return False