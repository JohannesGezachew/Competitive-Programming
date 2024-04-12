class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = 0
        right = (sorted(nums).index(pivot))
       
        
        ans = [0]*len(nums)
        for i in range(Counter(nums).get(pivot)):
            ans[right] = pivot
            right += 1
        for num in nums:
            if num < pivot:
                ans[left] = num
                left += 1
            elif num > pivot:
                ans[right] = num
                right += 1
        return(ans)
