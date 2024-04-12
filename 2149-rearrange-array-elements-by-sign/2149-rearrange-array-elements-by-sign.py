class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
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




                