class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        z = s.split()
        return (len(z[-1]))
