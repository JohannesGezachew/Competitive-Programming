class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        horizontal_length = 0
        for i in range(len(points)-1):
            temp = points[i+1][0] - points[i][0]
            horizontal_length = max(horizontal_length,temp)
        return horizontal_length
