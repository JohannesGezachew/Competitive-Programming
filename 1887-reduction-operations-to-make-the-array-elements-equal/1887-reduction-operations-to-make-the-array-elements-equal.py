class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()

        temp =list(set(nums))
        t = min(temp)
        c = Counter(nums)
        holder = 0

        for i in temp:
            if i == t:
                continue
            holder +=c[i]
        if holder ==0:
            return 0
        return holder+1