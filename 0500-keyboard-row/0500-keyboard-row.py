class Solution:
    def findWords(self, words: List[str]) -> List[str]:
            a1 = set("qwertyuiop")
            a2 = set("asdfghjkl")
            a3 = set("zxcvbnm")
            sol = []
            for word in words:
                a = set(word.lower())
                if a <= a1 or a <= a2 or a <= a3:
                    sol.append(word)
            return sol
