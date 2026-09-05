class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        max_arr=[0]*n
        min_arr=[0]*n
        curr_min=float('inf')
        curr_max=float('-inf')
        for i in range(n):
            max_arr[i]=max(curr_max,nums[i])
            min_arr[n-i-1]=min(curr_min,nums[n-i-1])
            if(max_arr[i]!=curr_max):
                curr_max=nums[i]
            if(min_arr[n-i-1]!=curr_min):
                curr_min=nums[n-i-1]
        for i in range(n):
            if max_arr[i]-min_arr[i]<=k:
                return i
        return -1