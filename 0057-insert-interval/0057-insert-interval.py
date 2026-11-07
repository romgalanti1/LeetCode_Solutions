class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        # need to return output array
        output = []
        # new interval can grow, by merging
        newStart = newInterval[0]
        newEnd = newInterval[1]
        added = False
        # when should i merge?
        # if two intervals share a number take the min of the start and the max of the end
        # when do two intervals share a number?
        # [  ]       [   ]            [    ]
        #    [   ]     [   ]      [   ]
        # append all intervals that dont touch newInterval
        # merge all intervals that do touch newInterval
        # append the rest
        for start, end in intervals:
            if end < newStart: # append all intervals before merged
                output.append([start,end])
            elif start > newEnd and not added: # first time meeting interval not in merged, append the merged
                output.append([newStart,newEnd])
                added = True
                output.append([start,end])
            elif start > newEnd: # append all the rest after appending merged
                output.append([start,end])
            else: # merge
                newStart = min(start,newStart)
                newEnd = max(end,newEnd)
        if not added:
            output.append([newStart,newEnd])
            
        return output
