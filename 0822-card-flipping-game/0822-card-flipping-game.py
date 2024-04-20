class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {f for f, b in zip(fronts, backs) if f == b}
        res = float('inf')
        for f, b in zip(fronts, backs):
            if f!= b:
                if f not in same:
                    res = min(res, f)
                if b not in same:
                    res = min(res, b)
        return res if res!= float('inf') else 0