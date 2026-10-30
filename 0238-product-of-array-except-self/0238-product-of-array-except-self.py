class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # first approach - prefix prroduct array, divide each i but cant divide
        # second approach for each i find the product for each other index O(n^2)
        # insight - for each i the product of the arrya is the product of all left nums and all right nums
        # iterate left to right- for each i output[i] will be the product of nums[:i]
        # iterate again right to left and multiply output[i] by the product of all right ones
        # keep running_product from right to left with O(1) space
        # i - [1,2,3,4]
        # o - [1,1,2,6]
        
        n = len(nums)
        output = [1 for _ in range(n)]
        for i in range(1,n):
            output[i] = output[i-1] * nums[i-1]
        
        running_product = 1
        for j in range(n-2,-1,-1):
            running_product *= nums[j + 1]
            output[j] *= running_product
        
        return output
        