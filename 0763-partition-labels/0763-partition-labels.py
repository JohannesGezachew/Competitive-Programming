class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = right = 0
        answer = []
        lidx = 0

        while right < len(s):
            right = s.rindex(s[left])
            while left < right:
                left += 1
                right = max(right, s.rindex(s[left]))
            
            if left == right:
                answer.append(right - lidx + 1)
                lidx = left = right = right + 1
        
        return answer