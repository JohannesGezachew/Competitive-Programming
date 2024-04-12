class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1
        neg = []
        pos = []
        ans =[]
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        for i  in range(len(nums)//2):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans




                