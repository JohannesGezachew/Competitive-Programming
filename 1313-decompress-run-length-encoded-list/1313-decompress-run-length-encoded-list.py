class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        sol= []
        freq =[]

        x = 0
        y = 1
        for i in range(0,len(nums),2):
            temp = [nums[y]]*nums[x]

            sol.extend(temp) 
            x +=2
            y +=2
        return(sol)


