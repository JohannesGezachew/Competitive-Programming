class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = len(nums1) - len(nums2) - 1 
        right = len(nums2) - 1
        current = len(nums1) - 1 

        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[current] = nums1[left]
                left -= 1
            else:
                nums1[current] = nums2[right]
                right -= 1
            current -= 1