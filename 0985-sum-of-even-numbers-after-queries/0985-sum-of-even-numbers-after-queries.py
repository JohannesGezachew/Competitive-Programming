class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        temp = []
        s = sum(num for num in nums if num % 2 == 0)
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                s -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                s += nums[idx]
            temp.append(s)
        return temp
