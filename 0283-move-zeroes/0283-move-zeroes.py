class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        left=0
        right=left
        while right<n:
            if nums[right]!=0:
                  nums[left]=nums[right]
                  left+=1
            right+=1
        for i in range(left,n):
              nums[i]=0
        return nums