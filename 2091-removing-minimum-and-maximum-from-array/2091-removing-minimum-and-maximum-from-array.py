class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return 1
        max_ind=0
        min_ind=0
        minimum=nums[0]
        maximum=nums[0]
        for i in range(len(nums)):
            if nums[i]<minimum:
                minimum=nums[i]
                min_ind=i
            if nums[i]>maximum:
                maximum=nums[i]
                max_ind=i
        i=min(min_ind,max_ind)
        j=max(min_ind,max_ind)
        option1= j+1
        option2= n-i
        option3= i+1 + n-j
        return min(option1,option2,option3)