class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left = 0
        right = len(skill) - 1
        skill.sort()
        chemistry = skill[0] + skill[-1]
        
        res = 0

        while left < right:
            if skill[left] + skill[right] == chemistry:
                res += skill[left] * skill[right]
            else:
                return -1
            left += 1
            right -= 1
        return res