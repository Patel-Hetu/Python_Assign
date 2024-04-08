"""
This the solution associated to q1.
Points associated: 0

Given the radius of a circle, compute the area of that circle.
Assume pi = 3.14159
Round to two decimal places the computed area and return the result.
"""

import unittest
# --------------------------------------------------------------
# Area of a circle
# --------------------------------------------------------------
def area(radius):
    pi = 3.14159
    area = pi*(radius**2)
    return round(area*100)/100

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(area(2),12.57)
    def test1(self):
        self.assertEqual(area(3),28.27)
    def test2(self):
        self.assertEqual(area(4),50.27)
    def test3(self):
        self.assertEqual(area(10),314.16)


if __name__=='__main__':
    unittest.main(exit=True)