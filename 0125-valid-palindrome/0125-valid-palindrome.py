class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered_s = re.sub(r'[^a-z0-9]', '', s)
        return filtered_s == filtered_s[::-1]