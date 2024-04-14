from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        left = 0
        right = spaces[0]
        count = 0

        for i in range(len(s)):
            if i == right:

                ans += " " + s[i]
                count += 1 
                right = spaces[count] if count < len(spaces) else float('inf')  
            else:
                ans += s[i]
 

        return ans
