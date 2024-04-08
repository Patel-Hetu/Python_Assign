import unittest

"""
Credit: problem from Ilkka’s GitHub https://github.com/ikokkari/PythonProblems

Define an element of a list of items to be a dominator 
if every element to its right (not just the one element that is  
immediately to its right) is strictly smaller than that element. 

Note how according to this definition, the last item of the list 
is automatically a dominator, regardless of its value. 

This function should return the count of how many elements in items are dominators. 

Example:
the dominators of the list [42, 7, 12, 9, 13, 5] would be 42, 13 and 5. 
In turn, your function should return 3.

Important: your code must be efficient. I will call your function on complex inputs,
and will use a function to timeout any solution that is too computationally expensive.
Hint: find a solution that goes through the elements of the list 'items' only once.

Exam
[42, 7, 12, 9, 2, 5] 4
[] 0
[-2, 5, -1, -3] 2
[-10, -20, -30, -42] 4
[42, 42, 42, 42] 1
range(10**7) 1
range(10**7, 0, -1) 10000000

"""

def count_dominators(items):
    num_of_dominator = 0
    max_num = None
    
    for element in reversed(items):
        if max_num is None or element > max_num:
            max_num = element
            num_of_dominator += 1
    return num_of_dominator

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(count_dominators([42, 7, 12, 9, 2, 5]),4)
    def test1(self):
        self.assertEqual(count_dominators([42, 7, 12, 9, 13, 5]),3)
    def test2(self):
        self.assertEqual(count_dominators([]),0)
    def test3(self):
        self.assertEqual(count_dominators(range(10**7)),1)        
    def test4(self):
        self.assertEqual(count_dominators([42, 42, 42, 42]),1)

if __name__=='__main__':
    unittest.main(exit=True)
    