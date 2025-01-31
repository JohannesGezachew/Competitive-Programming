class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        filtered_s = re.sub(r'[^a-z0-9]', '', s)
        return filtered_s == filtered_s[::-1]

        