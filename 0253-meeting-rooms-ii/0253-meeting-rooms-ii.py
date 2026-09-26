class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        starts = [a[0] for a in intervals]
        ends = [a[1] for a in intervals]
        starts.sort()
        ends.sort()
        s_p = 0
        e_p = 0
        most = 0
        curr = 0
        n = len(intervals)
        while e_p < n:
            most = max(most, curr)
            if s_p < n and starts[s_p] < ends[e_p] :
                curr += 1
                s_p += 1
            else:
                curr -= 1
                e_p += 1
        return most