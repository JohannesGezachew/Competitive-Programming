class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                    prev_day = stack.pop()
                    result[prev_day] = i - prev_day
            stack.append(i)
        return result 

