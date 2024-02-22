class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
    
        salary.remove(min(salary))
        salary.remove(max(salary))
        print(salary)
        return float(sum(salary))/(len(salary))

        