import unittest
from fuerza_bruta_recursiva import fb
# from programacion_dinamica import fb

class TestFB(unittest.TestCase):
    def test_fb_0(self):
        self.assertEqual(fb([4,4,2,1,3]), 2)
    
    def test_fb_1(self):
        self.assertEqual(fb([6,6,1,2,3,4,5]), 1)
    
    def test_fb_2(self):
        self.assertEqual(fb([4,1,8,9,2]), 1)
    
    # def test_factorial_negative(self):
    #     with self.assertRaises(ValueError):
    #         pass
    
    # def test_factorial_float(self):
    #     with self.assertRaises(TypeError):
    #         pass

if __name__ == '__main__':
    unittest.main()
