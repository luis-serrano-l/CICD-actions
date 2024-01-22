import unittest
from multiplica import multiplicar
class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 100), -100)
        self.assertEqual(multiplicar(-12, -12), 144)
        self.assertEqual(multiplicar(-12, 2), -24)

if __name__ == '__main__':
    unittest.main()