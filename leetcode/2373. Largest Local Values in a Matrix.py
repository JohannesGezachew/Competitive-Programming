class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = []
        for i in range(len(grid)):
            curr = []
            for j in range(len(grid) - 2):
                curr.append(max(grid[i][j:j+3]))
            rows.append(curr)
        
        cols = [[0 for _ in range(len(rows))] for _ in range(len(rows[0]))]

        for i in range(len(rows)):
            for j in range(len(rows[0])):
                cols[j][i] = rows[i][j]
        
        answer = []

        for i in range(len(cols)):
            curr = []
            for j in range(len(cols[0]) - 2):
                curr.append(max(cols[i][j:j+3]))
            
            answer.append(curr)

        final_answer = [[0 for _ in range(len(answer))] for _ in range(len(answer))]
        for i in range(len(answer)):
            for j in range(len(answer[0])):
                final_answer[j][i] = answer[i][j]

        return final_answer
                
