import cbmcodecs
import unittest


class TestC64Codecs(unittest.TestCase):
    def test_lowercase(self):
        codec = "petscii-c64en-lc"
        self.assertEqual(b"HELLO \xd7\xcf\xd2\xcc\xc4 123 @!\x5c", "hello WORLD 123 @!£".encode(codec))
        self.assertEqual(b"\x12", "\uf11a".encode(codec))  # reversevid
        self.assertEqual(b"\xfa", "✓".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "π".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "♥".encode(codec)

    def test_uppercase(self):
        codec = "petscii-c64en-uc"
        self.assertEqual(b"HELLO 123 @!\x5c", "HELLO 123 @!£".encode(codec))
        self.assertEqual(b"\x12", "\uf11a".encode(codec))  # reversevid
        self.assertEqual(b"\xd3", "♥".encode(codec))
        self.assertEqual(b"\xff", "π".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "✓".encode(codec)

    def test_screencodes_lowercase(self):
        codec = "screencode-c64-lc"
        self.assertEqual(b"", "hello WORLD 123 @!£".encode(codec))
        self.assertEqual(b"", "♥".encode(codec))
        self.assertEqual(b"", "✓".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "♥".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "π".encode(codec)

    def test_screencodes_uppercase(self):
        codec = "screencode-c64-uc"
        self.assertEqual(b"", "WORLD 123 @!£".encode(codec))
        self.assertEqual(b"\x5e", "♥".encode(codec))
        self.assertEqual(b"\x5e", "π".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "✓".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "hello".encode(codec)


class TestVic20Codecs(unittest.TestCase):
    def test_lowercase(self):
        codec = "petscii-vic20en-lc"
        self.assertEqual(b"HELLO \xd7\xcf\xd2\xcc\xc4 123 @!\x5c", "hello WORLD 123 @!£".encode(codec))
        self.assertEqual(b"\xfa", "✓".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "π".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "♥".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "\uf11a".encode(codec)  # reversevid not supported on vic20

    def test_uppercase(self):
        codec = "petscii-vic20en-uc"
        self.assertEqual(b"HELLO 123 @!\x5c", "HELLO 123 @!£".encode(codec))
        self.assertEqual(b"\xd3", "♥".encode(codec))
        self.assertEqual(b"\xff", "π".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "✓".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "\uf11a".encode(codec)  # reversevid not supported on vic20
