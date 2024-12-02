class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        prefix_counts = Counter()
        prefix_counts[0] = 1 
        result = 0
        
        for num in nums:
            if num % 2 != 0:
                odd_count += 1

            result += prefix_counts[odd_count - k]
            prefix_counts[odd_count] += 1
        
        return result