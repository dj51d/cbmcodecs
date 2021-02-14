import cbmcodecs
import unittest


class TestC64Codecs(unittest.TestCase):
    def test_lowercase(self):
        codec = "petscii_c64en_lc"
        self.assertEqual(b"HELLO \xd7\xcf\xd2\xcc\xc4 123 @!\x5c", "hello WORLD 123 @!£".encode(codec))
        self.assertEqual(b"\x12", "\uf11a".encode(codec))  # reversevid
        self.assertEqual(b"\xfa", "✓".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "π".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "♥".encode(codec)

    def test_uppercase(self):
        codec = "petscii_c64en_uc"
        self.assertEqual(b"HELLO 123 @!\x5c", "HELLO 123 @!£".encode(codec))
        self.assertEqual(b"\x12", "\uf11a".encode(codec))  # reversevid
        self.assertEqual(b"\xd3", "♥".encode(codec))
        self.assertEqual(b"\xff", "π".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "✓".encode(codec)

    def test_screencodes_lowercase(self):
        codec = "screencode_c64_lc"
        self.assertEqual(b"\x08\x05\x0c\x0c\x0f\x20\x57\x4f\x52\x4c\x44\x20\x31\x32\x33\x20\x00\x21\x1c",
                         "hello WORLD 123 @!£".encode(codec))
        self.assertEqual(b"\x7a", "✓".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "♥".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "π".encode(codec)

    def test_screencodes_uppercase(self):
        codec = "screencode_c64_uc"
        self.assertEqual(b"\x17\x0f\x12\x0c\x04\x20\x31\x32\x33\x20\x00\x21\x1c", "WORLD 123 @!£".encode(codec))
        self.assertEqual(b"\x53", "♥".encode(codec))
        self.assertEqual(b"\x5e", "π".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "✓".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "hello".encode(codec)


class TestVic20Codecs(unittest.TestCase):
    def test_lowercase(self):
        codec = "petscii_vic20en_lc"
        self.assertEqual(b"HELLO \xd7\xcf\xd2\xcc\xc4 123 @!\x5c", "hello WORLD 123 @!£".encode(codec))
        self.assertEqual(b"\xfa", "✓".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "π".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "♥".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "\uf11a".encode(codec)  # reversevid not supported on vic20

    def test_uppercase(self):
        codec = "petscii_vic20en_uc"
        self.assertEqual(b"HELLO 123 @!\x5c", "HELLO 123 @!£".encode(codec))
        self.assertEqual(b"\xd3", "♥".encode(codec))
        self.assertEqual(b"\xff", "π".encode(codec))
        with self.assertRaises(UnicodeEncodeError):
            "✓".encode(codec)
        with self.assertRaises(UnicodeEncodeError):
            "\uf11a".encode(codec)  # reversevid not supported on vic20
