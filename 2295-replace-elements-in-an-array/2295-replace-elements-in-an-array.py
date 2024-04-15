class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dnum = {num: i for i, num in enumerate(nums)}
 

        for target, new_value in operations:
            if target in dnum:
                nums[dnum[target]] = new_value
                dnum[new_value] =dnum[target]
 
        
        return nums