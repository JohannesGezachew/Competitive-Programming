class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:


        ans = []
            

        for i in range(len(transactions)):

            x =  transactions[i].split(",")
            # print(ans)

            if int(x[2]) > 1000:
                ans.append(transactions[i])
                continue
                
            for j in range(len(transactions)):
                y = transactions[j].split(",")
                print(y)
                if abs(int(y[1]) -  int(x[1])) <= 60:
                    if x[0] == y[0] and x[3] != y[3]:
                        ans.append(transactions[i])
                        break

        return (ans)

