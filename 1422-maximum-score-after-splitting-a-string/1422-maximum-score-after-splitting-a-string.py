class Solution:
    def maxScore(self, s: str) -> int:
        leftZeros = 0
        rightOnes = s.count("1")
        maxSum = 0

        for i in range(len(s)-1):
            if s[i] == "0":
                leftZeros += 1
            if s[i] == "1":
                rightOnes -= 1
            maxSum = max(maxSum, rightOnes + leftZeros)
        return maxSum 