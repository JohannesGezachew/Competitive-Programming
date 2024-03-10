class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in storage:
                return [storage[complement], i]
            if nums[i] in storage:
                continue
            storage[nums[i]] = i
           
        
        