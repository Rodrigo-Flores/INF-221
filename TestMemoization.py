import unittest
from memoization import memoization

class TestMemoization(unittest.TestCase):

    def test_1(self):
        self.assertEqual(memoization([3,4,6,8,7]), 1, "Debe ser 1")

    def test_2(self):
        self.assertEqual(memoization([4,2,1,3]), 2, "Debe ser 2")

    def test_3(self):
        self.assertEqual(memoization([2,1,9,8]), 2, "Debe ser 2")
    
    def test_4(self):
        self.assertEqual(memoization([6, 1, 2, 3, 4, 5]), 1, "Debe ser 1")

    def test_5(self):
        self.assertEqual(memoization([1,8,9,2]), 1, "Debe ser 1")

    def test_6(self):
        self.assertEqual(memoization([5, 2, 4, 3, 1]), 3, "Debe ser 3")

    def test_7(self):
        self.assertEqual(memoization([2, 1, 3, 4]), 1, "Debe ser 1")

    def test_8(self):
        self.assertEqual(memoization([3,4,6,1,5,8,7]), 3, "Debe ser 3")

    def test_9(self):
        self.assertEqual(memoization([50,3,10,7,40,80]), 2, "Debe ser 2")
    
    def test_10(self):
        self.assertEqual(memoization( [10,22,9,33,21,50,41,60]), 3, "Debe ser 3")
    
    def test_11(self):
        self.assertEqual(memoization([50,3,10,7,40,80]), 2, "Debe ser 2")

    def test_12(self):
        self.assertEqual(memoization([9,8,2,1]), 3, "Debe ser 3")

if __name__ == '__main__':
    unittest.main()
