class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cs = Counter()
        left = 0
        right = 0
        maxs = 0
        maxf = 0
        while right < len(s):
            cs[s[right]] += 1
            maxf = max(maxf, cs[s[right]])

            while (right - left + 1) - maxf > k:
                cs[s[left]] -= 1
                left += 1
            maxs = max(right- left + 1, maxs)
            right += 1
        return maxs