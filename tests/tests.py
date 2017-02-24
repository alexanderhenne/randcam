import unittest
import hashlib
import binascii
import randcam

byteArray = bytearray("randcam is a good project", "utf-8")


class RandomTest(unittest.TestCase):

    def test_random(self):
        m = hashlib.sha256()
        m.update(byteArray)
        digest = m.digest()

        self.assertEqual(binascii.hexlify(digest).decode("utf-8"),
                         "47ed7bd2cd92e9a863c13ed2cda933fb093447f18e65fd2563e580d37a9e4e60")


class ShannonTest(unittest.TestCase):
    def test_shannon(self):
        entropy = randcam.shannon_entropy(byteArray)

        self.assertEqual(entropy, 3.7034651896016464)

if __name__ == '__main__':
    unittest.main()
