import unittest
from fuerza_bruta import fuerza_bruta

class TestFuerzaBruta(unittest.TestCase):

    def test_1(self):
        self.assertEqual(fuerza_bruta([3,4,6,8,7]), 1, "Debe ser 1")

    def test_2(self):
        self.assertEqual(fuerza_bruta([4,2,1,3]), 2, "Debe ser 2")

    def test_3(self):
        self.assertEqual(fuerza_bruta([2,1,9,8]), 2, "Debe ser 2")
    
    def test_4(self):
        self.assertEqual(fuerza_bruta([6, 1, 2, 3, 4, 5]), 1, "Debe ser 1")

    def test_5(self):
        self.assertEqual(fuerza_bruta([1,8,9,2]), 1, "Debe ser 1")

    def test_6(self):
        self.assertEqual(fuerza_bruta([5, 2, 4, 3, 1]), 3, "Debe ser 3")

    def test_7(self):
        self.assertEqual(fuerza_bruta([2, 1, 3, 4]), 1, "Debe ser 1")

    def test_8(self):
        self.assertEqual(fuerza_bruta([3,4,6,1,5,8,7]), 3, "Debe ser 3")

    def test_9(self):
        self.assertEqual(fuerza_bruta([50,3,10,7,40,80]), 2, "Debe ser 2")
    
    def test_10(self):
        self.assertEqual(fuerza_bruta( [10,22,9,33,21,50,41,60]), 3, "Debe ser 3")
    
    def test_11(self):
        self.assertEqual(fuerza_bruta([50,3,10,7,40,80]), 2, "Debe ser 2")

    def test_12(self):
        self.assertEqual(fuerza_bruta([9,8,2,1]), 3, "Debe ser 3")

if __name__ == '__main__':
    unittest.main()

    # Ejemplo de uso
#arr = [5,3,4,6,8,7] # 1 ✔
#arr = [4,4,2,1,3] # 2   ✔
#arr = [6, 6, 1, 2, 3, 4, 5]  # 1 ✔
#arr = [4,1,8,9,2] # 1  ✔
#arr = [5, 5, 2, 4, 3, 1] # 3  ✔
#arr = [4, 2, 1, 3, 4] # 1   ✔
#arr = [7,3,4,6,1,5,8,7] #3 tira 2  ✖
#arr = [6,50,3,10,7,40,80] # 2  ✔
#arr = [8,10,22,9,33,21,50,41,60] #3   ✔
#arr = [4,1,8,9,2] #1 ✔
#arr = [4,9,8,2,1] #3  ✔
arr = [4,2,1,9,8] #2 ✔