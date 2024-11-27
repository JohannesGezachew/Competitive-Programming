class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter_p = Counter(p)
        window_length = len(p)
        current = Counter(s[:window_length])
        result = []
        
        for i in range(len(s) - window_length + 1):
            if i > 0:

                current[s[i - 1]] -= 1
                if current[s[i - 1]] == 0:
                    del current[s[i - 1]]
                current[s[i + window_length - 1]] += 1
            
            if current == counter_p:
                result.append(i)
        
        return result