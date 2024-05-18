class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        value = set(nums1) & set(nums2)
        return min(value) if value else -1