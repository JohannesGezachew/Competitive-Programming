class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        out = []
        t = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                ans.append(i)

        for i in range(len(boxes)):
            for j in ans:
                t += abs(j-i)
            out.append(t)
            t = 0
        return(out)
          
