""" Python Character Mapping Codec screencode_c64_lc generated from 'mappings/screencode_c64_lc.txt' with gencodec.py.

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]

class StreamWriter(Codec, codecs.StreamWriter):
    pass

class StreamReader(Codec, codecs.StreamReader):
    pass

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name='screencode-c64-lc',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Table

decoding_table = (
    '@'         #  0x00 -> COMMERCIAL AT
    'a'         #  0x01 -> LATIN SMALL LETTER A
    'b'         #  0x02 -> LATIN SMALL LETTER B
    'c'         #  0x03 -> LATIN SMALL LETTER C
    'd'         #  0x04 -> LATIN SMALL LETTER D
    'e'         #  0x05 -> LATIN SMALL LETTER E
    'f'         #  0x06 -> LATIN SMALL LETTER F
    'g'         #  0x07 -> LATIN SMALL LETTER G
    'h'         #  0x08 -> LATIN SMALL LETTER H
    'i'         #  0x09 -> LATIN SMALL LETTER I
    'j'         #  0x0A -> LATIN SMALL LETTER J
    'k'         #  0x0B -> LATIN SMALL LETTER K
    'l'         #  0x0C -> LATIN SMALL LETTER L
    'm'         #  0x0D -> LATIN SMALL LETTER M
    'n'         #  0x0E -> LATIN SMALL LETTER N
    'o'         #  0x0F -> LATIN SMALL LETTER O
    'p'         #  0x10 -> LATIN SMALL LETTER P
    'q'         #  0x11 -> LATIN SMALL LETTER Q
    'r'         #  0x12 -> LATIN SMALL LETTER R
    's'         #  0x13 -> LATIN SMALL LETTER S
    't'         #  0x14 -> LATIN SMALL LETTER T
    'u'         #  0x15 -> LATIN SMALL LETTER U
    'v'         #  0x16 -> LATIN SMALL LETTER V
    'w'         #  0x17 -> LATIN SMALL LETTER W
    'x'         #  0x18 -> LATIN SMALL LETTER X
    'y'         #  0x19 -> LATIN SMALL LETTER Y
    'z'         #  0x1A -> LATIN SMALL LETTER Z
    '['         #  0x1B -> LEFT SQUARE BRACKET
    '\xa3'      #  0x1C -> POUND SIGN
    ']'         #  0x1D -> RIGHT SQUARE BRACKET
    '\u2191'    #  0x1E -> UPWARDS ARROW
    '\u2190'    #  0x1F -> LEFTWARDS ARROW
    '@'         #  0x20 -> COMMERCIAL AT
    '@'         #  0x21 -> COMMERCIAL AT
    '@'         #  0x22 -> COMMERCIAL AT
    '@'         #  0x23 -> COMMERCIAL AT
    '@'         #  0x24 -> COMMERCIAL AT
    '@'         #  0x25 -> COMMERCIAL AT
    '@'         #  0x26 -> COMMERCIAL AT
    '@'         #  0x27 -> COMMERCIAL AT
    '@'         #  0x28 -> COMMERCIAL AT
    '@'         #  0x29 -> COMMERCIAL AT
    '@'         #  0x2A -> COMMERCIAL AT
    '@'         #  0x2B -> COMMERCIAL AT
    '@'         #  0x2C -> COMMERCIAL AT
    '@'         #  0x2D -> COMMERCIAL AT
    '@'         #  0x2E -> COMMERCIAL AT
    '@'         #  0x2F -> COMMERCIAL AT
    '@'         #  0x30 -> COMMERCIAL AT
    '@'         #  0x31 -> COMMERCIAL AT
    '@'         #  0x32 -> COMMERCIAL AT
    '@'         #  0x33 -> COMMERCIAL AT
    '@'         #  0x34 -> COMMERCIAL AT
    '@'         #  0x35 -> COMMERCIAL AT
    '@'         #  0x36 -> COMMERCIAL AT
    '@'         #  0x37 -> COMMERCIAL AT
    '@'         #  0x38 -> COMMERCIAL AT
    '@'         #  0x39 -> COMMERCIAL AT
    '@'         #  0x3A -> COMMERCIAL AT
    '@'         #  0x3B -> COMMERCIAL AT
    '@'         #  0x3C -> COMMERCIAL AT
    '@'         #  0x3D -> COMMERCIAL AT
    '@'         #  0x3E -> COMMERCIAL AT
    '@'         #  0x3F -> COMMERCIAL AT
    '@'         #  0x40 -> COMMERCIAL AT
    '@'         #  0x41 -> COMMERCIAL AT
    '@'         #  0x42 -> COMMERCIAL AT
    '@'         #  0x43 -> COMMERCIAL AT
    '@'         #  0x44 -> COMMERCIAL AT
    '@'         #  0x45 -> COMMERCIAL AT
    '@'         #  0x46 -> COMMERCIAL AT
    '@'         #  0x47 -> COMMERCIAL AT
    '@'         #  0x48 -> COMMERCIAL AT
    '@'         #  0x49 -> COMMERCIAL AT
    '@'         #  0x4A -> COMMERCIAL AT
    '@'         #  0x4B -> COMMERCIAL AT
    '@'         #  0x4C -> COMMERCIAL AT
    '@'         #  0x4D -> COMMERCIAL AT
    '@'         #  0x4E -> COMMERCIAL AT
    '@'         #  0x4F -> COMMERCIAL AT
    '@'         #  0x50 -> COMMERCIAL AT
    '@'         #  0x51 -> COMMERCIAL AT
    '@'         #  0x52 -> COMMERCIAL AT
    '@'         #  0x53 -> COMMERCIAL AT
    '@'         #  0x54 -> COMMERCIAL AT
    '@'         #  0x55 -> COMMERCIAL AT
    '@'         #  0x56 -> COMMERCIAL AT
    '@'         #  0x57 -> COMMERCIAL AT
    '@'         #  0x58 -> COMMERCIAL AT
    '@'         #  0x59 -> COMMERCIAL AT
    '@'         #  0x5A -> COMMERCIAL AT
    '@'         #  0x5B -> COMMERCIAL AT
    '@'         #  0x5C -> COMMERCIAL AT
    '@'         #  0x5D -> COMMERCIAL AT
    '@'         #  0x5E -> COMMERCIAL AT
    '@'         #  0x5F -> COMMERCIAL AT
    '@'         #  0x60 -> COMMERCIAL AT
    '@'         #  0x61 -> COMMERCIAL AT
    '@'         #  0x62 -> COMMERCIAL AT
    '@'         #  0x63 -> COMMERCIAL AT
    '@'         #  0x64 -> COMMERCIAL AT
    '@'         #  0x65 -> COMMERCIAL AT
    '@'         #  0x66 -> COMMERCIAL AT
    '@'         #  0x67 -> COMMERCIAL AT
    '@'         #  0x68 -> COMMERCIAL AT
    '@'         #  0x69 -> COMMERCIAL AT
    '@'         #  0x6A -> COMMERCIAL AT
    '@'         #  0x6B -> COMMERCIAL AT
    '@'         #  0x6C -> COMMERCIAL AT
    '@'         #  0x6D -> COMMERCIAL AT
    '@'         #  0x6E -> COMMERCIAL AT
    '@'         #  0x6F -> COMMERCIAL AT
    '@'         #  0x70 -> COMMERCIAL AT
    '@'         #  0x71 -> COMMERCIAL AT
    '@'         #  0x72 -> COMMERCIAL AT
    '@'         #  0x73 -> COMMERCIAL AT
    '@'         #  0x74 -> COMMERCIAL AT
    '@'         #  0x75 -> COMMERCIAL AT
    '@'         #  0x76 -> COMMERCIAL AT
    '@'         #  0x77 -> COMMERCIAL AT
    '@'         #  0x78 -> COMMERCIAL AT
    '@'         #  0x79 -> COMMERCIAL AT
    '@'         #  0x7A -> COMMERCIAL AT
    '@'         #  0x7B -> COMMERCIAL AT
    '@'         #  0x7C -> COMMERCIAL AT
    '@'         #  0x7D -> COMMERCIAL AT
    '@'         #  0x7E -> COMMERCIAL AT
    '@'         #  0x7F -> COMMERCIAL AT
    '@'         #  0x80 -> COMMERCIAL AT
    '@'         #  0x81 -> COMMERCIAL AT
    '@'         #  0x82 -> COMMERCIAL AT
    '@'         #  0x83 -> COMMERCIAL AT
    '@'         #  0x84 -> COMMERCIAL AT
    '@'         #  0x85 -> COMMERCIAL AT
    '@'         #  0x86 -> COMMERCIAL AT
    '@'         #  0x87 -> COMMERCIAL AT
    '@'         #  0x88 -> COMMERCIAL AT
    '@'         #  0x89 -> COMMERCIAL AT
    '@'         #  0x8A -> COMMERCIAL AT
    '@'         #  0x8B -> COMMERCIAL AT
    '@'         #  0x8C -> COMMERCIAL AT
    '@'         #  0x8D -> COMMERCIAL AT
    '@'         #  0x8E -> COMMERCIAL AT
    '@'         #  0x8F -> COMMERCIAL AT
    '@'         #  0x90 -> COMMERCIAL AT
    '@'         #  0x91 -> COMMERCIAL AT
    '@'         #  0x92 -> COMMERCIAL AT
    '@'         #  0x93 -> COMMERCIAL AT
    '@'         #  0x94 -> COMMERCIAL AT
    '@'         #  0x95 -> COMMERCIAL AT
    '@'         #  0x96 -> COMMERCIAL AT
    '@'         #  0x97 -> COMMERCIAL AT
    '@'         #  0x98 -> COMMERCIAL AT
    '@'         #  0x99 -> COMMERCIAL AT
    '@'         #  0x9A -> COMMERCIAL AT
    '@'         #  0x9B -> COMMERCIAL AT
    '@'         #  0x9C -> COMMERCIAL AT
    '@'         #  0x9D -> COMMERCIAL AT
    '@'         #  0x9E -> COMMERCIAL AT
    '@'         #  0x9F -> COMMERCIAL AT
    '@'         #  0xA0 -> COMMERCIAL AT
    '@'         #  0xA1 -> COMMERCIAL AT
    '@'         #  0xA2 -> COMMERCIAL AT
    '@'         #  0xA3 -> COMMERCIAL AT
    '@'         #  0xA4 -> COMMERCIAL AT
    '@'         #  0xA5 -> COMMERCIAL AT
    '@'         #  0xA6 -> COMMERCIAL AT
    '@'         #  0xA7 -> COMMERCIAL AT
    '@'         #  0xA8 -> COMMERCIAL AT
    '@'         #  0xA9 -> COMMERCIAL AT
    '@'         #  0xAA -> COMMERCIAL AT
    '@'         #  0xAB -> COMMERCIAL AT
    '@'         #  0xAC -> COMMERCIAL AT
    '@'         #  0xAD -> COMMERCIAL AT
    '@'         #  0xAE -> COMMERCIAL AT
    '@'         #  0xAF -> COMMERCIAL AT
    '@'         #  0xB0 -> COMMERCIAL AT
    '@'         #  0xB1 -> COMMERCIAL AT
    '@'         #  0xB2 -> COMMERCIAL AT
    '@'         #  0xB3 -> COMMERCIAL AT
    '@'         #  0xB4 -> COMMERCIAL AT
    '@'         #  0xB5 -> COMMERCIAL AT
    '@'         #  0xB6 -> COMMERCIAL AT
    '@'         #  0xB7 -> COMMERCIAL AT
    '@'         #  0xB8 -> COMMERCIAL AT
    '@'         #  0xB9 -> COMMERCIAL AT
    '@'         #  0xBA -> COMMERCIAL AT
    '@'         #  0xBB -> COMMERCIAL AT
    '@'         #  0xBC -> COMMERCIAL AT
    '@'         #  0xBD -> COMMERCIAL AT
    '@'         #  0xBE -> COMMERCIAL AT
    '@'         #  0xBF -> COMMERCIAL AT
    '@'         #  0xC0 -> COMMERCIAL AT
    '@'         #  0xC1 -> COMMERCIAL AT
    '@'         #  0xC2 -> COMMERCIAL AT
    '@'         #  0xC3 -> COMMERCIAL AT
    '@'         #  0xC4 -> COMMERCIAL AT
    '@'         #  0xC5 -> COMMERCIAL AT
    '@'         #  0xC6 -> COMMERCIAL AT
    '@'         #  0xC7 -> COMMERCIAL AT
    '@'         #  0xC8 -> COMMERCIAL AT
    '@'         #  0xC9 -> COMMERCIAL AT
    '@'         #  0xCA -> COMMERCIAL AT
    '@'         #  0xCB -> COMMERCIAL AT
    '@'         #  0xCC -> COMMERCIAL AT
    '@'         #  0xCD -> COMMERCIAL AT
    '@'         #  0xCE -> COMMERCIAL AT
    '@'         #  0xCF -> COMMERCIAL AT
    '@'         #  0xD0 -> COMMERCIAL AT
    '@'         #  0xD1 -> COMMERCIAL AT
    '@'         #  0xD2 -> COMMERCIAL AT
    '@'         #  0xD3 -> COMMERCIAL AT
    '@'         #  0xD4 -> COMMERCIAL AT
    '@'         #  0xD5 -> COMMERCIAL AT
    '@'         #  0xD6 -> COMMERCIAL AT
    '@'         #  0xD7 -> COMMERCIAL AT
    '@'         #  0xD8 -> COMMERCIAL AT
    '@'         #  0xD9 -> COMMERCIAL AT
    '@'         #  0xDA -> COMMERCIAL AT
    '@'         #  0xDB -> COMMERCIAL AT
    '@'         #  0xDC -> COMMERCIAL AT
    '@'         #  0xDD -> COMMERCIAL AT
    '@'         #  0xDE -> COMMERCIAL AT
    '@'         #  0xDF -> COMMERCIAL AT
    '@'         #  0xE0 -> COMMERCIAL AT
    '@'         #  0xE1 -> COMMERCIAL AT
    '@'         #  0xE2 -> COMMERCIAL AT
    '@'         #  0xE3 -> COMMERCIAL AT
    '@'         #  0xE4 -> COMMERCIAL AT
    '@'         #  0xE5 -> COMMERCIAL AT
    '@'         #  0xE6 -> COMMERCIAL AT
    '@'         #  0xE7 -> COMMERCIAL AT
    '@'         #  0xE8 -> COMMERCIAL AT
    '@'         #  0xE9 -> COMMERCIAL AT
    '@'         #  0xEA -> COMMERCIAL AT
    '@'         #  0xEB -> COMMERCIAL AT
    '@'         #  0xEC -> COMMERCIAL AT
    '@'         #  0xED -> COMMERCIAL AT
    '@'         #  0xEE -> COMMERCIAL AT
    '@'         #  0xEF -> COMMERCIAL AT
    '@'         #  0xF0 -> COMMERCIAL AT
    '@'         #  0xF1 -> COMMERCIAL AT
    '@'         #  0xF2 -> COMMERCIAL AT
    '@'         #  0xF3 -> COMMERCIAL AT
    '@'         #  0xF4 -> COMMERCIAL AT
    '@'         #  0xF5 -> COMMERCIAL AT
    '@'         #  0xF6 -> COMMERCIAL AT
    '@'         #  0xF7 -> COMMERCIAL AT
    '@'         #  0xF8 -> COMMERCIAL AT
    '@'         #  0xF9 -> COMMERCIAL AT
    '@'         #  0xFA -> COMMERCIAL AT
    '@'         #  0xFB -> COMMERCIAL AT
    '@'         #  0xFC -> COMMERCIAL AT
    '@'         #  0xFD -> COMMERCIAL AT
    '@'         #  0xFE -> COMMERCIAL AT
    '@'         #  0xFF -> COMMERCIAL AT
)

### Encoding table
encoding_table = codecs.charmap_build(decoding_table)

