class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = Counter(nums)
        result = [i for i in nums if x[i] > len(nums) / 3]
        return set(result)
        