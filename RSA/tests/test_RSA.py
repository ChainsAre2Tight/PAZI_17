import unittest
from RSA.main import generate_keys, encrypt_integer, decrypt_integer


class TestGenerateKeys(unittest.TestCase):

    def test_not_coprime(self):
        with self.assertRaises(ValueError):
            generate_keys(20, 40)

    def test_E_is_not_prime(self):
        with self.assertRaises(AttributeError):
            generate_keys(11, 13, 6)

    def test_E_is_too_big(self):
        with self.assertRaises(AttributeError):
            generate_keys(11, 13, 257)

    def test_3557_2579_3(self):
        p = 3557
        q = 2579
        e = 3
        intended_result = {
            'public_key': (3, 9173503),
            'private_key': (6111579, 9173503)
        }
        result = generate_keys(p=p, q=q, e=e)
        self.assertEqual(intended_result, result)


class TestEncryption(unittest.TestCase):
    # def test_encrypt_integer_1(self):
    #     public_key = (3, 9173503)
    #     msg = 111111
    #     result = encrypt_integer(message=msg, public_key=public_key)
    #     intended_result = 4051753
    #     self.assertEqual(intended_result, result)

    def test_encrypt_integer_2(self):
        public_key = (7, 33)
        msg = 2
        intended_result = 29
        result = encrypt_integer(message=msg, public_key=public_key)
        self.assertEqual(intended_result, result)


class TestDecryption(unittest.TestCase):
    # def test_decrypt_integer_1(self):
    #     private_key = (6111579, 9173503)
    #     msg = 4051753
    #     intended_result = 111111
    #     result = decrypt_integer(encrypted_message=msg, private_key=private_key)
    #     self.assertEqual(intended_result, result)

    def test_decrypt_integer_2(self):
        private_key = (3, 33)
        msg = 29
        intended_result = 2
        result = decrypt_integer(encrypted_message=msg, private_key=private_key)
        self.assertEqual(intended_result, result)


if __name__ == '__main__':
    unittest.main()
