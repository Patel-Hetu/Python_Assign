import unittest

def pyramid_builder(blocks):
    '''
    given a certain number of blocks how many layers of a pyriamid can mr. frog build?

    a pyramid is built as follows...
    * -> 1 layer, 1 block

    *
   *** -> 2 layers, 4 blocks

   *
  ***
 ***** -> 3 layers, 9 blocks

    '''
    num = 1
    n = 0
    
    while num > 0:
        n = (num*(num+1))/2
        if n > blocks:
            return num-1
            exit()
        elif n == blocks:
            return num
            exit()
        else:
            pass
        num+=1
        

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(pyramid_builder(1), 1)

    def test1(self):
        self.assertEqual(pyramid_builder(3), 2)

    def test2(self):
        self.assertEqual(pyramid_builder(6), 3)

    def test3(self):
        self.assertEqual(pyramid_builder(7), 3)

    def test4(self):
        self.assertEqual(pyramid_builder(10), 4)


if __name__ == '__main__':
    unittest.main(exit=True)
