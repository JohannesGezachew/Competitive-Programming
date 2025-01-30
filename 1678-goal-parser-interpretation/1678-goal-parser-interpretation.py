class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        x = 0
        ans = []
        while x < len(command):
            if command[x] == "G":
                ans.append("G")
                x += 1
            elif command[x:x + 2] == "()":
                ans.append("o")
                x += 2
            else :
                ans.append("al")
                x += 4

        return "".join(ans)


        