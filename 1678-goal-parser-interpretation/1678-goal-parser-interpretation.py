class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        x = []
        for i in range(len(command)-1):
            if command[i] =="G":
                x.append("G")
            elif command[i] =="(" and command[i+1] ==")":
                x.append("o")
            elif command[i] =="(" and command[i+1] =="a":
                x.append("al")
        if command[len(command)-1] =="G":
                x.append("G")

        return "".join(x)
                