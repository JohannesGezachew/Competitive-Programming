class Solution:
    def removeStars(self, s: str) -> str:
        componets = list(s)
        stack = []
        for item in componets:
            if item == "*":
                stack.pop()
            else:
                stack.append(item)
        return "".join(stack)