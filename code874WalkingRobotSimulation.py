"""
874 Walking Robot Simulation

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)

Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
"""
class Solution(object):
    # brutal force solution
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """ 
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))   # up, right, down, left
        obstacleSet = set(map(tuple, obstacles))

        res, d, x, y = 0, 0, 0, 0
        for cmd in commands:
            if cmd == -2:
                d = (d + 3)%4
            elif cmd == -1:
                d = (d + 1)%4
            else:
                for k in range(cmd):
                    if (x + dirs[d][0], y + dirs[d][1]) not in obstacleSet:
                        x += dirs[d][0]
                        y += dirs[d][1]
                        res = max(res, x*x + y*y)
                    else:
                        break
            
        return res

commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
print(Solution().robotSim(commands, obstacles))