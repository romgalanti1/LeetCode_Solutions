class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n=len(nums)
        numsum=0
        max_avg=0
        avg=0
        for i in range(k):
            numsum+=nums[i]
        avg=numsum/k
        max_avg=avg
        if k<n:
            for i in range(k,n):
                numsum+=nums[i]-nums[i-k]
                avg=numsum/k
                if avg>max_avg:
                    max_avg=avg
        return max_avg