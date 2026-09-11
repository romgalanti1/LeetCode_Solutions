class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        n=len(digits)
        d=dict()
        even_digits=len(set([x for x in digits if x%2==0]))
        counts=Counter(digits)
        res=0
        for j in range(100,1000,2):
            currnum=str(j)
            curr_counts=Counter([int(digit) for digit in currnum])
            valid=True
            for t in range(3):
                if curr_counts[int(currnum[t])]>counts[int(currnum[t])]:
                    valid=False
            if valid:
                res+=1
        return res
            