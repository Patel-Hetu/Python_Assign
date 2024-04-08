import unittest

"""
Suppose that there are 2000 houses in your city, 
and each house is assigned a number based on 
a coordinate system that is defined as follows:
	y
	^
	|
	|  16
	|  11 17
	|  7  12 18
	|  4  8  13 19 
	|  2  5  9  14 20
	|  1  3  6  10 15 21
(0,0) ------------------> x

For instance:
the house identified by the number 1 is located at coordinates (1,1), 
and the house identified by the number 9 is located at coordinates (3,2).
Write a function coordinate(x,y) that returns the corresponding house number.
"""

def coordinate(x,y):
    x_coor = 1
    y_coor = 1
    IDnum = 1
    
    for house in range(1, 2001):
        if x_coor == x and y_coor == y:
            return IDnum
        
        x_coor1 = x_coor
        y_coor1 = y_coor
        
        while x_coor != y_coor1 and y_coor != x_coor1:
            x_coor1 += 1
            y_coor1 -= 1
            IDnum += 1
            if x_coor1 == x and y_coor1 == y:
                return IDnum
            
        y_coor += 1
        IDnum += 1
    

class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(coordinate(3,2),9)
    def test1(self):
        self.assertEqual(coordinate(1,3),4)
    def test2(self):
        self.assertEqual(coordinate(4,3),19)
    def test3(self):
        self.assertEqual(coordinate(9,6),100)
    def test4(self):
        self.assertEqual(coordinate(2,6),23)
        
if __name__=='__main__':
    unittest.main(exit=True)