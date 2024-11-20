class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merged_word = []
        left, right = 0, 0

        while left < len(word1) and right < len(word2):
            if word1[left:] > word2[right:]:
                merged_word.append(word1[left])
                left += 1
            else:
                merged_word.append(word2[right])
                right += 1

        if left < len(word1):
            merged_word.extend(word1[left:])
        if right < len(word2):
            merged_word.extend(word2[right:])

        return "".join(merged_word)
