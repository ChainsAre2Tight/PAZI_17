import unittest
from RSA.algorithms import Eucledes_algorithm, phi, extended_gcd


class TestEucledesAlgorithm(unittest.TestCase):
    def test_1071_462_21(self):
        self.assertEqual(21, Eucledes_algorithm(1071, 462))

    def test_1111_1112_1(self):
        self.assertEqual(1, Eucledes_algorithm(1111, 1112))

    def test_1234_5678_2(self):
        self.assertEqual(2, Eucledes_algorithm(1234, 5678))

    def test_6699_10857_231(self):
        self.assertEqual(231, Eucledes_algorithm(6699, 10857))

    def test_891_9093_3(self):
        self.assertEqual(3, Eucledes_algorithm(891, 9093))

    def test_2017_3011_1(self):
        self.assertEqual(1, Eucledes_algorithm(2017, 3011))


class TestExtendedGCD(unittest.TestCase):
    def test_1071_462_21(self):
        self.assertEqual(21, extended_gcd(1071, 462)[0])

    def test_1111_1112_1(self):
        self.assertEqual(1, extended_gcd(1111, 1112)[0])

    def test_1234_5678_2(self):
        self.assertEqual(2, extended_gcd(1234, 5678)[0])

    def test_6699_10857_231(self):
        self.assertEqual(231, extended_gcd(6699, 10857)[0])

    def test_891_9093_3(self):
        self.assertEqual(3, extended_gcd(891, 9093)[0])

    def test_2017_3011_1(self):
        self.assertEqual(1, extended_gcd(2017, 3011)[0])

    def test_Bezu_991_981(self):
        self.assertEqual((99, -98), extended_gcd(991, 981)[1])


class TestEulerFunction(unittest.TestCase):
    def test_1(self):
        self.assertEqual(20, phi(33))

    def test_2(self):
        self.assertEqual(40, phi(100))


if __name__ == '__main__':
    unittest.main()
