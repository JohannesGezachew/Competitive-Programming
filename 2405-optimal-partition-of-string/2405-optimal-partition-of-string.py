class Solution:
    def partitionString(self, s: str) -> int:
        unique_chars = set()
        ans = 1

        for char in s:
            if char in unique_chars:
                ans += 1
                unique_chars.clear()
            unique_chars.add(char)
        return ans