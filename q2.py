import unittest

"""
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] 
represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of 
one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll 
(i.e., put one inside the other).

Note: Suppose the envelops will always have a smaller height than width:        
        ____________
       |           |
       |           |
       |___________|
 
Example 1:
Input: envelopes = [[5,10],[6,10],[6,13],[2,4]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,4] => [5,10] => [6,13]).

Example 2:
Input: envelopes = [[1,2],[1,2],[1,2]]
Output: 1
"""

def rDoll(envelopes):
    
    leng = len(envelopes)
    
    if leng == 0:
        return 0
    
    for measurement in range(leng-1):
        for i in range(leng-1):
            if envelopes[i][0] * envelopes[i][1] > envelopes[i+1][0] * envelopes[i+1][1]:
                envelopes[i], envelopes[i+1] = envelopes[i+1], envelopes[i]
    
    current = envelopes[0]
    output = 1
    
    for next_measure in range(1,leng):
        if current[0] < envelopes[next_measure][0] and current[1] < envelopes[next_measure][1]:
            current = envelopes[next_measure]
            output += 1
    return output

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(rDoll([[5,10],[6,10],[6,13],[2,4]]),3)
    def test1(self):
        self.assertEqual(rDoll([[1,2],[1,2],[1,2]]),1)
    def test2(self):
        self.assertEqual(rDoll([[8,14],[6,14],[2,4],[55,106],[4,6]]),4)
    def test3(self):
        self.assertEqual(rDoll([]),0)
    def test4(self):
        self.assertEqual(rDoll([[7,15],[8,16]]),2)


if __name__=='__main__':
    unittest.main(exit=True)