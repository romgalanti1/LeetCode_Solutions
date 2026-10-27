class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        row = "#" * (n-1) + "."
        grid = [row for _ in range(m)]
        first_row = "." * n
        grid[0] = first_row
        
        return grid