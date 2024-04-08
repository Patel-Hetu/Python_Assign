import unittest

"""
remove_duplicates_recursion is a recursive function that takes 2 inputs:
1. dupList: list where elements may be duplicates
2. uniqList: empty list. 

Create the function remove_duplicates_recursion, 
which should produce a list called uniqList containing 
only the unique elements of the input list dupList, 
thereby eliminating any duplicates,
while preserving the order of the elements as they initially appear. 
For instance, if dupList is [1,2,3,3], then uniqList should be [1,2,3]. 
Finally, the function should return uniqList.

No points if recursion is not used.
"""

def remove_duplicates_recursion (dupList, uniqList):
    
    final_unique_list = []
    leng = len(dupList)
    
    if leng == 0:
        return []
    else:
        if dupList[0] not in uniqList:
            final_unique_list = [dupList[0]]
            uniqList += final_unique_list
        return final_unique_list + remove_duplicates_recursion(dupList[1:], uniqList)

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(remove_duplicates_recursion([1,2,2,2,3,4],[]),[1,2,3,4])
    def test1(self):
        self.assertEqual(remove_duplicates_recursion(['hello', 'world', 'hello', 'world', 'hi'],[]),['hello', 'world', 'hi'])
    def test2(self):
        self.assertEqual(remove_duplicates_recursion(["water","weather","water"],[]),["water","weather"])
    def test3(self):
        self.assertEqual(remove_duplicates_recursion(["A","b","a","A"],[]),['A', 'b', 'a'])
    def test4(self):
        self.assertEqual(remove_duplicates_recursion([9,5,4,1,1,4],[]),[9,5,4,1])

if __name__=='__main__':
    unittest.main(exit=True)
    

