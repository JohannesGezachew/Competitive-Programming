class Solution:
    def minimizedStringLength(self, s: str) -> int:
        mini_string_len = len(s)
        a =Counter(s)
        keys = [i for i in a.values()]
        for key in keys:
            if key >= 2:
                mini_string_len -= key -1
        return(mini_string_len)