class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        l = 0
        count = 0

        while left < len(people):
            if count + people[left] <= limit:
                count += people[left]
                left += 1
            else:
                l += 1
                count = 0
        return l +1