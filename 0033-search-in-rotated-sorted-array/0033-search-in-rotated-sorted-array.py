class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        r = n - 1
        l = 0

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[r] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
        