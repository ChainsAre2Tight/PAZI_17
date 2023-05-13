import unittest
from backpack_alg.packing import pack, create_public_key, encrypt, decrypt


class MyTestCase(unittest.TestCase):
    def test_packing_True_example(self):
        key = [2, 3, 6, 13, 27, 52, 105, 210]
        self.assertEqual(
            (
                True,
                '10100101',
                270
            ),
            pack(
                s_max=270,
                sequence=key
            )
        )

    def test_packing_False(self):
        key = [2, 3, 6, 13, 27, 53, 105, 210]
        self.assertEqual(
            (
                False, None, None
            ),
            pack(
                s_max=270,
                sequence=key
            )
        )


class TestPublicKey(unittest.TestCase):
    def test_public_key_creation_example(self):
        key = [2, 3, 6, 13, 27, 52, 105, 210]
        p_key = create_public_key(private_key=key, a=31, n=420)
        self.assertEqual([62, 93, 186, 403, 417, 352, 315, 210], p_key)


class TestEncode(unittest.TestCase):
    def test_encode_example(self):
        key = [62, 93, 186, 403, 417, 352, 315, 210]
        message = [
            '11010000',
            '11000010',
            '11000000',
            '11000001',
            '11001110',
            '11000000',
            '11001100',
        ]
        result = encrypt(message, key)
        intended_result = [558, 470, 155, 365, 1239, 155, 924]
        self.assertEqual(intended_result, result)


class TestDecode(unittest.TestCase):
    def test_decode_example(self):
        d = [2, 3, 6, 13, 27, 52, 105, 210]
        n = 420
        a = 31
        anti_a = 271
        intended_result = [558, 470, 155, 365, 1239, 155, 924]
        msg = [
            '11010000',
            '11000010',
            '11000000',
            '11000001',
            '11001110',
            '11000000',
            '11001100',
        ]
        result = decrypt(message=msg, public_key=d)
        self.assertEqual(intended_result, result)


if __name__ == '__main__':
    unittest.main()
