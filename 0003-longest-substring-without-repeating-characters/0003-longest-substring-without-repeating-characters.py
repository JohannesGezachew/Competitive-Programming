class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        ch = set()
        max_str = 0
        
        while right < len(s):
            if s[right] not in ch:
                ch.add(s[right])
                right += 1
                max_str = max(max_str, right - left)
            else:
                ch.remove(s[left])
                left += 1
        
        return max_str
