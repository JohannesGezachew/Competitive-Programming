class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        left = right = count = 0
        players.sort()
        trainers.sort()
        while left <len(players) and right < len(trainers):
            if players[left] <= trainers[right]:
                count += 1
                left += 1
                right += 1
            elif players[left] > trainers[right]:
                right += 1
        return count       