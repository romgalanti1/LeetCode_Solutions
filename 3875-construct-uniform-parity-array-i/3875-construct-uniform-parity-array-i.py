class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        odd_count=(1 for x in nums1 if x % 2 != 0)
        can_be_even = odd_count != 1
        can_be_odd = odd_count == len(nums1) or (odd_count>=1)
        return can_be_even or can_be_odd        