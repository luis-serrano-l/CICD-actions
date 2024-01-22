import unittest
from divide import dividir
class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(3, 2), 1.5)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(22, 2), 11)

if __name__ == '__main__':
    unittest.main()