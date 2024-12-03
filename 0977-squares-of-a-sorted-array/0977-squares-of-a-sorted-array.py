class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [pow(nums[0],2)]

        left = right = None
        for i in range(1,len(nums)):
            if abs(nums[i - 1]) < abs(nums[i]):
                left = i - 1
                right = i 
                break
        res = []

    
        if left == right == None:
            for i in range(len(nums)):
                res.append(nums[i] ** 2)
            
            return res if nums[0] >= 0 else res[::-1]

        while left >= 0 and right < len(nums):
            x = pow(nums[left],2)
            y  = pow(nums[right],2)
            if x > y:
                res.append(y)
                right += 1
            else:
                res.append(x)
                left -= 1


        for i in range(left, -1, -1):
            res.append(pow(nums[i],2))


        for j in range(right, len(nums)):
            res.append(pow(nums[j],2))
            
        return res

