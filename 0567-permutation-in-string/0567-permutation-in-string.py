class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs1 = Counter(s1)
        cs2 = Counter( s2[0:len(s1)])
        left = 0
        for right in range(len(s1),len(s2)):
            if cs1 == cs2:
                return True

            cs2[s2[right]] += 1
            cs2[s2[ left]] -= 1
            left += 1
            if cs2[s2[left]] == 0:
                del cs2[s2[right-left]]

        return cs1 == cs2
