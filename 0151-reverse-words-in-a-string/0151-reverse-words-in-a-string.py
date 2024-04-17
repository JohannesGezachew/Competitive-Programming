class Solution:
    def reverseWords(self, s: str) -> str:
        n = s.split()
        m = ""
        for i in range(len(n)-1,-1,-1):
            m +=(n[i])+" "
        return(m.strip())