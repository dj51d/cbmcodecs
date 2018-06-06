""" Python Character Mapping Codec screencode_c64_uc generated from 'mappings/screencode_c64_uc.txt' with gencodec.py.

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
        name='screencode-c64-uc',
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
    'A'         #  0x01 -> LATIN CAPITAL LETTER A
    'B'         #  0x02 -> LATIN CAPITAL LETTER B
    'C'         #  0x03 -> LATIN CAPITAL LETTER C
    'D'         #  0x04 -> LATIN CAPITAL LETTER D
    'E'         #  0x05 -> LATIN CAPITAL LETTER E
    'F'         #  0x06 -> LATIN CAPITAL LETTER F
    'G'         #  0x07 -> LATIN CAPITAL LETTER G
    'H'         #  0x08 -> LATIN CAPITAL LETTER H
    'I'         #  0x09 -> LATIN CAPITAL LETTER I
    'J'         #  0x0A -> LATIN CAPITAL LETTER J
    'K'         #  0x0B -> LATIN CAPITAL LETTER K
    'L'         #  0x0C -> LATIN CAPITAL LETTER L
    'M'         #  0x0D -> LATIN CAPITAL LETTER M
    'N'         #  0x0E -> LATIN CAPITAL LETTER N
    'O'         #  0x0F -> LATIN CAPITAL LETTER O
    'P'         #  0x10 -> LATIN CAPITAL LETTER P
    'Q'         #  0x11 -> LATIN CAPITAL LETTER Q
    'R'         #  0x12 -> LATIN CAPITAL LETTER R
    'S'         #  0x13 -> LATIN CAPITAL LETTER S
    'T'         #  0x14 -> LATIN CAPITAL LETTER T
    'U'         #  0x15 -> LATIN CAPITAL LETTER U
    'V'         #  0x16 -> LATIN CAPITAL LETTER V
    'W'         #  0x17 -> LATIN CAPITAL LETTER W
    'X'         #  0x18 -> LATIN CAPITAL LETTER X
    'Y'         #  0x19 -> LATIN CAPITAL LETTER Y
    'Z'         #  0x1A -> LATIN CAPITAL LETTER Z
    '['         #  0x1B -> LEFT SQUARE BRACKET
    '\xa3'      #  0x1C -> POUND SIGN
    ']'         #  0x1D -> RIGHT SQUARE BRACKET
    '\u2191'    #  0x1E -> UPWARDS ARROW
    '\u2190'    #  0x1F -> LEFTWARDS ARROW
    ' '         #  0x20 -> SPACE
    '!'         #  0x21 -> EXCLAMATION MARK
    '"'         #  0x22 -> QUOTATION MARK
    '#'         #  0x23 -> NUMBER SIGN
    '$'         #  0x24 -> DOLLAR SIGN
    '%'         #  0x25 -> PERCENT SIGN
    '&'         #  0x26 -> AMPERSAND
    "'"         #  0x27 -> APOSTROPHE
    '('         #  0x28 -> LEFT PARENTHESIS
    ')'         #  0x29 -> RIGHT PARENTHESIS
    '*'         #  0x2A -> ASTERISK
    '+'         #  0x2B -> PLUS SIGN
    ','         #  0x2C -> COMMA
    '-'         #  0x2D -> HYPHEN-MINUS
    '.'         #  0x2E -> FULL STOP
    '/'         #  0x2F -> SOLIDUS
    '0'         #  0x30 -> DIGIT ZERO
    '1'         #  0x31 -> DIGIT ONE
    '2'         #  0x32 -> DIGIT TWO
    '3'         #  0x33 -> DIGIT THREE
    '4'         #  0x34 -> DIGIT FOUR
    '5'         #  0x35 -> DIGIT FIVE
    '6'         #  0x36 -> DIGIT SIX
    '7'         #  0x37 -> DIGIT SEVEN
    '8'         #  0x38 -> DIGIT EIGHT
    '9'         #  0x39 -> DIGIT NINE
    ':'         #  0x3A -> COLON
    ';'         #  0x3B -> SEMICOLON
    '<'         #  0x3C -> LESS-THAN SIGN
    '='         #  0x3D -> EQUALS SIGN
    '>'         #  0x3E -> GREATER-THAN SIGN
    '?'         #  0x3F -> QUESTION MARK
    '\u2500'    #  0x40 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\u2660'    #  0x41 -> BLACK SPADE SUIT
    '\u2502'    #  0x42 -> BOX DRAWINGS LIGHT VERTICAL
    '\u2500'    #  0x43 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\uf122'    #  0x44 -> BOX DRAWINGS LIGHT HORIZONTAL ONE QUARTER UP (CUS)
    '\uf123'    #  0x45 -> BOX DRAWINGS LIGHT HORIZONTAL TWO QUARTERS UP (CUS)
    '\uf124'    #  0x46 -> BOX DRAWINGS LIGHT HORIZONTAL ONE QUARTER DOWN (CUS)
    '\uf126'    #  0x47 -> BOX DRAWINGS LIGHT VERTICAL ONE QUARTER LEFT (CUS)
    '\uf128'    #  0x48 -> BOX DRAWINGS LIGHT VERTICAL ONE QUARTER RIGHT (CUS)
    '\u256e'    #  0x49 -> BOX DRAWINGS LIGHT ARC DOWN AND LEFT
    '\u2570'    #  0x4A -> BOX DRAWINGS LIGHT ARC UP AND RIGHT
    '\u256f'    #  0x4B -> BOX DRAWINGS LIGHT ARC UP AND LEFT
    '\uf12a'    #  0x4C -> ONE EIGHTH BLOCK UP AND RIGHT (CUS)
    '\u2572'    #  0x4D -> BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT
    '\u2571'    #  0x4E -> BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT
    '\uf12b'    #  0x4F -> ONE EIGHTH BLOCK DOWN AND RIGHT (CUS)
    '\uf12c'    #  0x50 -> ONE EIGHTH BLOCK DOWN AND LEFT (CUS)
    '\u25cf'    #  0x51 -> BLACK CIRCLE
    '\uf125'    #  0x52 -> BOX DRAWINGS LIGHT HORIZONTAL TWO QUARTERS DOWN (CUS)
    '\u2665'    #  0x53 -> BLACK HEART SUIT
    '\uf127'    #  0x54 -> BOX DRAWINGS LIGHT VERTICAL TWO QUARTERS LEFT (CUS)
    '\u256d'    #  0x55 -> BOX DRAWINGS LIGHT ARC DOWN AND RIGHT
    '\u2573'    #  0x56 -> BOX DRAWINGS LIGHT DIAGONAL CROSS
    '\u25cb'    #  0x57 -> WHITE CIRCLE
    '\u2663'    #  0x58 -> BLACK CLUB SUIT
    '\uf129'    #  0x59 -> BOX DRAWINGS LIGHT VERTICAL TWO QUARTERS RIGHT (CUS)
    '\u2666'    #  0x5A -> BLACK DIAMOND SUIT
    '\u253c'    #  0x5B -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    '\uf12e'    #  0x5C -> LEFT HALF BLOCK MEDIUM SHADE (CUS)
    '\u2502'    #  0x5D -> BOX DRAWINGS LIGHT VERTICAL
    '\u03c0'    #  0x5E -> GREEK SMALL LETTER PI
    '\u25e5'    #  0x5F -> BLACK UPPER RIGHT TRIANGLE
    '\xa0'      #  0x60 -> NO-BREAK SPACE
    '\u258c'    #  0x61 -> LEFT HALF BLOCK
    '\u2584'    #  0x62 -> LOWER HALF BLOCK
    '\u2594'    #  0x63 -> UPPER ONE EIGHTH BLOCK
    '\u2581'    #  0x64 -> LOWER ONE EIGHTH BLOCK
    '\u258f'    #  0x65 -> LEFT ONE EIGHTH BLOCK
    '\u2592'    #  0x66 -> MEDIUM SHADE
    '\u2595'    #  0x67 -> RIGHT ONE EIGHTH BLOCK
    '\uf12f'    #  0x68 -> LOWER HALF BLOCK MEDIUM SHADE (CUS)
    '\u25e4'    #  0x69 -> BLACK UPPER LEFT TRIANGLE
    '\uf130'    #  0x6A -> RIGHT ONE QUARTER BLOCK (CUS)
    '\u251c'    #  0x6B -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    '\u2597'    #  0x6C -> QUADRANT LOWER RIGHT
    '\u2514'    #  0x6D -> BOX DRAWINGS LIGHT UP AND RIGHT
    '\u2510'    #  0x6E -> BOX DRAWINGS LIGHT DOWN AND LEFT
    '\u2582'    #  0x6F -> LOWER ONE QUARTER BLOCK
    '\u250c'    #  0x70 -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    '\u2534'    #  0x71 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    '\u252c'    #  0x72 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    '\u2524'    #  0x73 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    '\u258e'    #  0x74 -> LEFT ONE QUARTER BLOCK
    '\u258d'    #  0x75 -> LEFT THREE EIGTHS BLOCK
    '\uf131'    #  0x76 -> RIGHT THREE EIGHTHS BLOCK (CUS)
    '\uf132'    #  0x77 -> UPPER ONE QUARTER BLOCK (CUS)
    '\uf133'    #  0x78 -> UPPER THREE EIGHTS BLOCK (CUS)
    '\u2583'    #  0x79 -> LOWER THREE EIGHTHS BLOCK
    '\uf12d'    #  0x7A -> ONE EIGHTH BLOCK UP AND LEFT (CUS)
    '\u2596'    #  0x7B -> QUADRANT LOWER LEFT
    '\u259d'    #  0x7C -> QUADRANT UPPER RIGHT
    '\u2518'    #  0x7D -> BOX DRAWINGS LIGHT UP AND LEFT
    '\u2598'    #  0x7E -> QUADRANT UPPER LEFT
    '\u259a'    #  0x7F -> QUADRANT UPPER LEFT AND LOWER RIGHT
    '\ufffe'    #  0x80 -> UNDEFINED
    '\ufffe'    #  0x81 -> UNDEFINED
    '\ufffe'    #  0x82 -> UNDEFINED
    '\ufffe'    #  0x83 -> UNDEFINED
    '\ufffe'    #  0x84 -> UNDEFINED
    '\ufffe'    #  0x85 -> UNDEFINED
    '\ufffe'    #  0x86 -> UNDEFINED
    '\ufffe'    #  0x87 -> UNDEFINED
    '\ufffe'    #  0x88 -> UNDEFINED
    '\ufffe'    #  0x89 -> UNDEFINED
    '\ufffe'    #  0x8A -> UNDEFINED
    '\ufffe'    #  0x8B -> UNDEFINED
    '\ufffe'    #  0x8C -> UNDEFINED
    '\ufffe'    #  0x8D -> UNDEFINED
    '\ufffe'    #  0x8E -> UNDEFINED
    '\ufffe'    #  0x8F -> UNDEFINED
    '\ufffe'    #  0x90 -> UNDEFINED
    '\ufffe'    #  0x91 -> UNDEFINED
    '\ufffe'    #  0x92 -> UNDEFINED
    '\ufffe'    #  0x93 -> UNDEFINED
    '\ufffe'    #  0x94 -> UNDEFINED
    '\ufffe'    #  0x95 -> UNDEFINED
    '\ufffe'    #  0x96 -> UNDEFINED
    '\ufffe'    #  0x97 -> UNDEFINED
    '\ufffe'    #  0x98 -> UNDEFINED
    '\ufffe'    #  0x99 -> UNDEFINED
    '\ufffe'    #  0x9A -> UNDEFINED
    '\ufffe'    #  0x9B -> UNDEFINED
    '\ufffe'    #  0x9C -> UNDEFINED
    '\ufffe'    #  0x9D -> UNDEFINED
    '\ufffe'    #  0x9E -> UNDEFINED
    '\ufffe'    #  0x9F -> UNDEFINED
    '\ufffe'    #  0xA0 -> UNDEFINED
    '\ufffe'    #  0xA1 -> UNDEFINED
    '\ufffe'    #  0xA2 -> UNDEFINED
    '\ufffe'    #  0xA3 -> UNDEFINED
    '\ufffe'    #  0xA4 -> UNDEFINED
    '\ufffe'    #  0xA5 -> UNDEFINED
    '\ufffe'    #  0xA6 -> UNDEFINED
    '\ufffe'    #  0xA7 -> UNDEFINED
    '\ufffe'    #  0xA8 -> UNDEFINED
    '\ufffe'    #  0xA9 -> UNDEFINED
    '\ufffe'    #  0xAA -> UNDEFINED
    '\ufffe'    #  0xAB -> UNDEFINED
    '\ufffe'    #  0xAC -> UNDEFINED
    '\ufffe'    #  0xAD -> UNDEFINED
    '\ufffe'    #  0xAE -> UNDEFINED
    '\ufffe'    #  0xAF -> UNDEFINED
    '\ufffe'    #  0xB0 -> UNDEFINED
    '\ufffe'    #  0xB1 -> UNDEFINED
    '\ufffe'    #  0xB2 -> UNDEFINED
    '\ufffe'    #  0xB3 -> UNDEFINED
    '\ufffe'    #  0xB4 -> UNDEFINED
    '\ufffe'    #  0xB5 -> UNDEFINED
    '\ufffe'    #  0xB6 -> UNDEFINED
    '\ufffe'    #  0xB7 -> UNDEFINED
    '\ufffe'    #  0xB8 -> UNDEFINED
    '\ufffe'    #  0xB9 -> UNDEFINED
    '\ufffe'    #  0xBA -> UNDEFINED
    '\ufffe'    #  0xBB -> UNDEFINED
    '\ufffe'    #  0xBC -> UNDEFINED
    '\ufffe'    #  0xBD -> UNDEFINED
    '\ufffe'    #  0xBE -> UNDEFINED
    '\ufffe'    #  0xBF -> UNDEFINED
    '\ufffe'    #  0xC0 -> UNDEFINED
    '\ufffe'    #  0xC1 -> UNDEFINED
    '\ufffe'    #  0xC2 -> UNDEFINED
    '\ufffe'    #  0xC3 -> UNDEFINED
    '\ufffe'    #  0xC4 -> UNDEFINED
    '\ufffe'    #  0xC5 -> UNDEFINED
    '\ufffe'    #  0xC6 -> UNDEFINED
    '\ufffe'    #  0xC7 -> UNDEFINED
    '\ufffe'    #  0xC8 -> UNDEFINED
    '\ufffe'    #  0xC9 -> UNDEFINED
    '\ufffe'    #  0xCA -> UNDEFINED
    '\ufffe'    #  0xCB -> UNDEFINED
    '\ufffe'    #  0xCC -> UNDEFINED
    '\ufffe'    #  0xCD -> UNDEFINED
    '\ufffe'    #  0xCE -> UNDEFINED
    '\ufffe'    #  0xCF -> UNDEFINED
    '\ufffe'    #  0xD0 -> UNDEFINED
    '\ufffe'    #  0xD1 -> UNDEFINED
    '\ufffe'    #  0xD2 -> UNDEFINED
    '\ufffe'    #  0xD3 -> UNDEFINED
    '\ufffe'    #  0xD4 -> UNDEFINED
    '\ufffe'    #  0xD5 -> UNDEFINED
    '\ufffe'    #  0xD6 -> UNDEFINED
    '\ufffe'    #  0xD7 -> UNDEFINED
    '\ufffe'    #  0xD8 -> UNDEFINED
    '\ufffe'    #  0xD9 -> UNDEFINED
    '\ufffe'    #  0xDA -> UNDEFINED
    '\ufffe'    #  0xDB -> UNDEFINED
    '\ufffe'    #  0xDC -> UNDEFINED
    '\ufffe'    #  0xDD -> UNDEFINED
    '\ufffe'    #  0xDE -> UNDEFINED
    '\ufffe'    #  0xDF -> UNDEFINED
    '\ufffe'    #  0xE0 -> UNDEFINED
    '\ufffe'    #  0xE1 -> UNDEFINED
    '\ufffe'    #  0xE2 -> UNDEFINED
    '\ufffe'    #  0xE3 -> UNDEFINED
    '\ufffe'    #  0xE4 -> UNDEFINED
    '\ufffe'    #  0xE5 -> UNDEFINED
    '\ufffe'    #  0xE6 -> UNDEFINED
    '\ufffe'    #  0xE7 -> UNDEFINED
    '\ufffe'    #  0xE8 -> UNDEFINED
    '\ufffe'    #  0xE9 -> UNDEFINED
    '\ufffe'    #  0xEA -> UNDEFINED
    '\ufffe'    #  0xEB -> UNDEFINED
    '\ufffe'    #  0xEC -> UNDEFINED
    '\ufffe'    #  0xED -> UNDEFINED
    '\ufffe'    #  0xEE -> UNDEFINED
    '\ufffe'    #  0xEF -> UNDEFINED
    '\ufffe'    #  0xF0 -> UNDEFINED
    '\ufffe'    #  0xF1 -> UNDEFINED
    '\ufffe'    #  0xF2 -> UNDEFINED
    '\ufffe'    #  0xF3 -> UNDEFINED
    '\ufffe'    #  0xF4 -> UNDEFINED
    '\ufffe'    #  0xF5 -> UNDEFINED
    '\ufffe'    #  0xF6 -> UNDEFINED
    '\ufffe'    #  0xF7 -> UNDEFINED
    '\ufffe'    #  0xF8 -> UNDEFINED
    '\ufffe'    #  0xF9 -> UNDEFINED
    '\ufffe'    #  0xFA -> UNDEFINED
    '\ufffe'    #  0xFB -> UNDEFINED
    '\ufffe'    #  0xFC -> UNDEFINED
    '\ufffe'    #  0xFD -> UNDEFINED
    '\ufffe'    #  0xFE -> UNDEFINED
    '\ufffe'    #  0xFF -> UNDEFINED
)

### Encoding table
encoding_table = codecs.charmap_build(decoding_table)

