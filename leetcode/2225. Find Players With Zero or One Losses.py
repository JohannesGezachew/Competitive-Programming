class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        players_lost_count = dict()
        player_won = set()
        player_lost = set()

        count = 0
        for i in range(len(matches)):
            player_won.add(matches[i][0])
            player_lost.add(matches[i][1])
            if matches[i][1] in players_lost_count:
                players_lost_count[matches[i][1]] += 1
            else:
                players_lost_count[matches[i][1]] = 1

        result = [
            sorted(list(player_won - player_lost)),
            sorted(list(k for k, v in players_lost_count.items() if v == 1)),
        ]
        return result
