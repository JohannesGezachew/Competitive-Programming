class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        z = []
        for i in range (len(s)):
            if s[i] == "(":
                z.append(s[i])
            elif s[i] ==")" and z and z[-1] == "(":
                z.pop()
            elif s[i] == "[":
                z.append(s[i])
            elif s[i] =="]"and z and z[-1] == "[":
                z.pop()
            elif s[i] == "{":
                z.append(s[i])
            elif s[i] =="}" and z and z[-1] == "{":
                z.pop() 
            else:
                return(False)
             
        if z:
            return(False)
        else:
            return(True)





        