class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        temp = set(list1) & set(list2)
        ans = dict()
        for i in temp:
            z = list1.index(i) + list2.index(i)
            ans[i] = z
        min_dict = min(ans.values())
        return([key for key in ans if ans[key]== min_dict])

