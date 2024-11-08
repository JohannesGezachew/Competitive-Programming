class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = [0] * 26
        max_count = 0
        start = 0
        max_length = 0

        for end in range(len(s)):

            count[ord(s[end]) - ord('A')] += 1

            max_count = max(max_count, count[ord(s[end]) - ord('A')])

            if (end - start + 1) - max_count > k:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
