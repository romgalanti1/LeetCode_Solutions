def swap(lst,i,j):
        temp=lst[i]
        lst[i]=lst[j]
        lst[j]=temp
class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        j=n-1
        k=0
        i=0
        while (i<j):
            if nums[j]==val:
                j-=1
                continue
            if nums[i]==val:
                swap(nums,i,j)
                j-=1
                i+=1
            else:
                i+=1
                continue
        for i in range(n):
            if nums[i]!=val:
                k+=1
        return k