class Solution:
    def reverseVowels(self, s: str) -> str:
        temp = []
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s_list = list(s)

        for i in range(len(s)):
            if s[i] in vowels:
                temp.append(s[i])
        
        temp.reverse()
        
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s_list[i] = temp[j]
                j += 1

        return ''.join(s_list)
