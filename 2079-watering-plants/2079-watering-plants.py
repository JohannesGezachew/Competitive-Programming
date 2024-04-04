class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        can = capacity
        l = 0
        r = 0
        is_true = True
        while is_true:
            if plants[l] <= can:
                can -= plants[l]
                l += 1
                r += 1
            else:
                r += 2*l
                can = capacity
            if l>= len(plants):
                is_true = False
        return(r)    
