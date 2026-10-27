# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set([(0,0)])
        
        def goback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(i,j,d):
            visited.add((i,j))
            robot.clean()
            for k in range(4):
                cur_d = (d + k) % 4
                di,dj = dirs[cur_d]
                ni,nj = i + di,j + dj
                if (ni,nj) not in visited and robot.move():
                    dfs(ni, nj, cur_d)
                    goback()
                robot.turnRight()
                
        dfs(0,0,0)
        