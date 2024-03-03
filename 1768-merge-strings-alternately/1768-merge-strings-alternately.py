class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = list()
        length = 0
        if len(word1) <= len(word2):
            length = len(word2)
        else:
            length = len(word1)
        for i in range (length):
            if i< len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
        return("".join(merged))