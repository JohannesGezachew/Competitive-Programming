class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        threshold = len(arr) / 4
        for num, count in counter.items():
            if count > threshold:
                return num
