class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack =[]

        for i in range(len(s)):
            print(stack)
            if s[i] == "(":
                stack.append(s[i])
            
            else:
                if stack[-1] == "(":
                    val = 1
                    stack.pop()
                    while stack and stack[-1] != "(":
                        val += stack.pop()
                    stack.append(val)
                else:
                    val = 2 * stack.pop()
                    stack.pop()
                    while stack and stack[-1] != "(":
                        val += stack.pop()
                    stack.append(val)
                    
        return stack.pop()