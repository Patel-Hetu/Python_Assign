import unittest

# --------------------------------------------------------------
# kanye west string matching
# --------------------------------------------------------------
def kanye_counter(str):
    '''
    Everyone knows each kanye gets a west.
    Given a string return True if there are exactly as many kanyes in the string as there are wests.
    Also, everyone knows that yeezy is another name for kanye so we will allow yeezy to count as kanye as well.

    '''
    string = str.lower()
    kanye_count = string.count("kanye") + string.count("yeezy")
    west_count = string.count("west")
    
    return kanye_count == west_count
    
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(kanye_counter('xxx'), True)

    def test1(self):
        self.assertEqual(kanye_counter('kanyewest'), True)

    def test2(self):
        self.assertEqual(kanye_counter('yeezywest'), True)

    def test3(self):
        self.assertEqual(kanye_counter('KaNyEwEsT'), True)

    def test4(self):
        self.assertEqual(kanye_counter('YeezyKanyeWest'), False)

if __name__ == '__main__':
    unittest.main(exit=True)