class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        res=[]
        i=0
        j=0
        while(i<m and j<n):
            if(nums1[i]>=nums2[j]):
                res.append(nums2[j])
                j+=1
            else:
                res.append(nums1[i])
                i+=1
        if (i==m):
            while(j<n):
                res.append(nums2[j])
                j+=1
        else:
            while(i<m):
                res.append(nums1[i])
                i+=1
        for t in range(len(res)):
            nums1[t]=res[t]
            