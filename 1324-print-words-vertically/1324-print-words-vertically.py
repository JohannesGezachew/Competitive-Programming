class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        x = s.split()
        z = []

        for j in range(len(max(x, key=lambda x: len(x)))):
            y = ""
            for i in range(len(x)):
                if j < len(x[i]):
                    y += x[i][j]
                else:
                    y += " "
            z.append(y.rstrip())
        return z

