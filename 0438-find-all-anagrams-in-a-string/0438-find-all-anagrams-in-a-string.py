class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_s = len(s)
        length_p = len(p)
        
        if length_p > length_s:
            return []
        
        anagram_indices = []

        count_p = Counter(p)
        
        count_window = Counter(s[:length_p-1])

        for i in range(length_p-1, length_s):
            count_window[s[i]] += 1

            if count_window == count_p:
                anagram_indices.append(i - length_p + 1)

            count_window[s[i - length_p + 1]] -= 1

            if count_window[s[i - length_p + 1]] == 0:
                del count_window[s[i - length_p + 1]]
        
        return anagram_indices