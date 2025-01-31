class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = [list(str(nums[i])) for i in range(len(nums))]
        ans = []

        for item in temp:
            for i in item:
                ans.append(int(i))

        return (ans)
