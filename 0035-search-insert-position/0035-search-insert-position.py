class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int   [1,3,5,6]
                           l  h
        """
        lo, hi = 0, len(nums) - 1

        while lo <= hi :
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


        