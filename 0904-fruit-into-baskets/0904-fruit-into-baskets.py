class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        num = float("-inf")
        bas = Counter()
        for right in range(len(fruits)):
            bas[fruits[right]] += 1

            while len(bas) > 2:
                bas[fruits[left]] -= 1 
                if bas[fruits[left]] == 0:
                    bas.pop(fruits[left])
                left += 1
            num = max(num, right- left+1)

        return len(fruits) if num == "-inf" else num 