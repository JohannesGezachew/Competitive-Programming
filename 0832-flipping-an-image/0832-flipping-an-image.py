class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def swap(x):
            if x ==0:
                return 1
            else:
                return 0
        answer = []
        for i in image:
            temp = []
            temp = i[::-1]
            res = map(swap,temp)
            answer.append(res)
        return answer
