class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        x = len(s)
        y = len(p)
        inde = []
        count = Counter(p)
        slide_window = s[:y]

        for i in range(x - y + 1):
            slide_count = Counter(s[i:i+y])
            if slide_count == count:
                inde.append(i)

        return(inde)

