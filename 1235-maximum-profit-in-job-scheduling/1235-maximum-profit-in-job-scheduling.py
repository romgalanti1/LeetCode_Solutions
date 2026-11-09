class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        """
        dp[i] = maximum profit taking elements from suffix starting at i
        """
        def findnextjob(end):
            """
             find next job that starts earliest after my current job that im taking ends
             because jobs are sorted by start, can binary search to find the *FIRST* index i such that
             start[i] >= end[j] where index j is the current job that im taking
            """
            endTime = jobs_by_start[end][1]
            lo = end 
            hi = n
            while lo < hi:
                mid = (lo + hi) // 2
                if jobs_by_start[mid][0] >= endTime: # can be this job or can be smaller
                    hi = mid
                else:
                    lo = mid + 1
            return lo
                

        n = len(startTime)

        jobs_by_start = sorted([(startTime[i],endTime[i],profit[i]) for i in range(n)])
        dp = [0] * (n + 1)

        for i in range(n-1,-1,-1):
            s, e, p = jobs_by_start[i]
            
            next_job = findnextjob(i)
            dp[i] = max(dp[i + 1],p + dp[next_job])

        return dp[0]
            

