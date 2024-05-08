class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        char_sets = {}
        
        for word in words:
            char_set = frozenset(word)
            if char_set in char_sets:
                count += char_sets[char_set]
                char_sets[char_set] += 1
            else:
                char_sets[char_set] = 1
        
        return count
