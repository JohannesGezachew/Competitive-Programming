class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        temp = []
        s = 0
        for i in range(len(queries)):
            nums[queries[i][1]] += queries[i][0]
            for num in nums:
                if num%2 ==0:
                    s += num
            temp.append(s)
            s = 0
        return(temp)
            
