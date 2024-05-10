class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l = len(matrix[0])
        r = 0
        sol = []
        for j in range(l):
            a =[]
            for i in matrix:
                a.append(i[r])
            sol.append(a)
            r +=1
        return(sol)