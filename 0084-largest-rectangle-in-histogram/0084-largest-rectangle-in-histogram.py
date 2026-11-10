class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        """
        each rectangle can either be one single height, vertical
        or can be horizontal which would be width * height
        can calculate width by the total number of heights looked at * the height of the minimum

        at every bar i, what is the maximum area i can get if the height is the shortest
        R[i] is the index of the first shorter height to the right
        L[i] is the index of the first shorter height to the left
        width would be R[i] - L[i] - 1
        height would be heights[i]
        area would be width * height
        build Right_heights and left_heights with monotonic stack
        """
        
        n = len(heights)
        max_area = 0
        right_heights = [n] * n
        left_heights = [-1] * n
        stack = []

        # build left_heights
        # monotonic increasing stack
        for i, height in enumerate(heights):
            while stack and stack[-1][1] >= height:
                stack.pop()

            if stack:
                left_heights[i] = stack[-1][0]
            
            stack.append((i,height))

        # build right_heights
        stack = []
        for j in range(n-1,-1,-1):
            height = heights[j]
            while stack and stack[-1][1] >= height:
                stack.pop()
            
           
            if stack:
                right_heights[j] = stack[-1][0]
            
            stack.append((j,height))

        i = 0
        # calculate heights for each height
        for i in range(n):
            right_index = right_heights[i]
            left_index = left_heights[i]
            width = right_index - left_index - 1
            area = width * heights[i]

            max_area = max(max_area,area)
        
        return max_area

                
