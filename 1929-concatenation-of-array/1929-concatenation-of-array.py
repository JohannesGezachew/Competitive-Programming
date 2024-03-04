class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num_copy = nums
        num_copy.extend(nums)
        return num_copy