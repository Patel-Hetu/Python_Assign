"""
Complete the function solveMaze(). 
This function takes exactly two arguments: 
    one is a 2D array containing a maze, 
    another is the ending point. 
Your starting point will always be (0,0).
The format of the end point will be a tuple as follows: (x, y).
Your goal is to solve the maze and output True if it can be solved, 
if no solution exists return False. 

A wall in the maze is represented by a 1, while a moveable square is represented by a 0. 
You can only move one square at a time.
You can only move left, right, up down.

Example:
Inputs: maze = [[0, 1, 1], [0, 0, 1], [1, 0, 1]]
        end = (2, 1)
        
i.e.:
        [[0, 1, 1], 
         [0, 0, 1], 
         [1, 0, 1]]
        
Output: True, because, starting from (0,0), we can go
down to (1,0), right to (1,1) and down to (2,1)
        
"""
import unittest
        
def solveMaze(maze, end):
    if maze[0][0] != 0:
        return False
    else:
        start_point = (0,0) 
        previous = (0,0)
        
        for i in range(9):
            moved = getAdjcentList(maze, start_point)
            movedlist = []
            for j in moved:
                if maze[j[0]][j[1]] == 0 and j != previous:
                    movedlist.append(j)
            len_of_movedlist = len(movedlist) 
            if len_of_movedlist == 1:
                previous = start_point
                start_point = movedlist[0]
            elif end in movedlist or start_point == end:
                return True
    return False

def getAdjcentList(maze, point):
    """
    Helper function used to return a list of tuples containing all VALID adjacent moves to point in maze.
    """
    res = []
    # check if right is valid
    if point[1] + 1 < len(maze[point[0]]):
        res.append((point[0], point[1]+1))
    # check if left is valid
    if point[1] - 1 >= 0:
        res.append((point[0], point[1]-1))
    # check if down is valid
    if point[0] + 1 < len(maze):
        res.append((point[0] + 1, point[1]))
    # check if we can go up
    if point[0] - 1 >= 0:
        res.append((point[0] - 1, point[1]))
    return res

class TestMazeMethod(unittest.TestCase):

    def testSolver(self):
        # basic maze to solve.
        miniMaze = [[0, 1, 1], [0, 0, 1], [1, 0, 1]]
        end = (2, 1)
        self.assertTrue(solveMaze(miniMaze, end))

    def testSolver2(self):
        # one line maze with no solution
        maze = [[0, 0, 1]]
        end = (0,2)
        self.assertFalse(solveMaze(maze, end))
    
    def testSolver3(self):
        # invalid starting point
        miniMaze = [[1, 1, 1], [0, 0, 1], [1, 0, 1]]
        end = (2, 1)
        self.assertFalse(solveMaze(miniMaze, end))
    
    def testSolver4(self):
        # ending point different than 2,1
        miniMaze = [[0, 0, 1], [1, 0, 0], [1, 0, 1]]
        end = (1, 2)
        self.assertTrue(solveMaze(miniMaze, end))
    
    def testSolver5(self):
        # end point is closed.
        miniMaze = [[0, 0, 1], [1, 0, 1], [1, 0, 1]]
        end = (1, 2)
        self.assertFalse(solveMaze(miniMaze, end))
            
if __name__ == '__main__':
    unittest.main()