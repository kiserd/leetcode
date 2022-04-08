# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
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

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # define some helper variables
        visited = set()
        # map directional vector to a right turn
        right_turn = {
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0)
        }

        # define recursive backtracking algorithm
        def backtrack(row, col, dir):
            """ blindly clean entire room using robot interface """
            # clean current cell and mark as visited
            robot.clean()
            visited.add((row, col))
            # unpack our directional vectors
            i_vec, j_vec = dir
            # explore all four candidates: straight, rt turn, rt turn, ...
            for _ in range(4):
                # only explore cells that have not been visited
                if (row + i_vec, col + j_vec) not in visited:
                    # handle case where movement is NOT blocked
                    if robot.move():
                        backtrack(row + i_vec, col + j_vec, (i_vec, j_vec))
                    # take note of barrier in visited set
                    else:
                        visited.add((row + i_vec, col + j_vec))
                # turn robot right and update our directional vector
                robot.turnRight()
                i_vec, j_vec = right_turn[(i_vec, j_vec)]
            # point robot forward and move back to where it came from
            go_back()

        def go_back():
            """ moves robot back to previous cell """
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        # kick off backtracking function
        backtrack(0, 0, (-1, 0))
