class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
            
        shortest_str = min(strs, key=len)
        
        for i in range(len(shortest_str)):
            for string in strs:
                if string[i] != shortest_str[i]:
                    return shortest_str[:i]
        
        return shortest_str
   
