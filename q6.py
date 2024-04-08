import unittest

def squared_string(msg):
    """
    Write a function squared_string(msg) that returns True if msg is a 
    squared_string else returns False. A perfect string is a string that contains
    even number of occurring characters. For example "ADeBEDaEEB" is a squared string as 
    there are 2 (A,D,B) and 4 (E), while "aat" is not a squared string 
    since ther is only one t
    
    Note: squared strings are case-insensitive
    """
    counts_num = {}
    for char in msg:
        counts_num[char] = counts_num.get(char,0)
        counts_num[char] += 1
    for count in counts_num.values():
        if count % 2 != 0:
            return False
    return True
        
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(squared_string(''), True)
    def test2(self):
        self.assertEqual(squared_string("aa"), True)
    def test3(self):
        self.assertEqual(squared_string('g'), False)
    def test4(self):
        self.assertEqual(squared_string('aat'), False)
    def test5(self):
        self.assertEqual(squared_string('TT'), True)
 
             
if __name__ == '__main__':
    unittest.main(exit=True)
