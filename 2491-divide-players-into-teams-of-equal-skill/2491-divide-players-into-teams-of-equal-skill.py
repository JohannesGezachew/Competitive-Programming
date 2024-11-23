class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left = 0
        right = len(skill) -1
        skill.sort()
        total = skill[left] + skill[right]
        ans = 0
        while left < right:
            if skill[left] + skill[right] == total:
                ans +=  (skill[left] * skill[right])
            else:
                return -1
            left += 1
            right -= 1
        return ans

