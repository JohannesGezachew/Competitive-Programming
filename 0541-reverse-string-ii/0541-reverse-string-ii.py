class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        modifed = ""
        is_true = True
        for i in range(0, len(s), k):
            if is_true:
                modifed += s[i:i+k][::-1]
                is_true = False
            else:
                modifed += s[i:i+k]
                is_true = True
        return modifed