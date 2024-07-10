class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        corrected =[""]*len(s)
        for i in s:
            index = int(i[-1])-1
            value = i[:-1]
            corrected[index]= value
        return " ".join(corrected)