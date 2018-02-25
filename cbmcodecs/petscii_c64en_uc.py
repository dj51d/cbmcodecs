""" Python Character Mapping Codec petscii_c64en_uc generated from 'mappings/petscii_c64en_uc.txt' with gencodec.py.

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
        name='petscii-c64en-uc',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Table

decoding_table = (
    '\ufffe'    #  0x00 -> UNDEFINED
    '\ufffe'    #  0x01 -> UNDEFINED
    '\ufffe'    #  0x02 -> UNDEFINED
    '\ufffe'    #  0x03 -> UNDEFINED
    '\ufffe'    #  0x04 -> UNDEFINED
    '\uf100'    #  0x05 -> WHITE COLOR SWITCH (CUS)
    '\ufffe'    #  0x06 -> UNDEFINED
    '\ufffe'    #  0x07 -> UNDEFINED
    '\uf118'    #  0x08 -> DISABLE CHARACTER SET SWITCHING (CUS)
    '\uf119'    #  0x09 -> ENABLE CHARACTER SET SWITCHING (CUS)
    '\ufffe'    #  0x0A -> UNDEFINED
    '\ufffe'    #  0x0B -> UNDEFINED
    '\ufffe'    #  0x0C -> UNDEFINED
    '\r'        #  0x0D -> CARRIAGE RETURN
    '\x0e'      #  0x0E -> SHIFT OUT
    '\ufffe'    #  0x0F -> UNDEFINED
    '\ufffe'    #  0x10 -> UNDEFINED
    '\uf11c'    #  0x11 -> CURSOR DOWN (CUS)
    '\uf11a'    #  0x12 -> REVERSE VIDEO ON (CUS)
    '\uf120'    #  0x13 -> HOME (CUS)
    '\x7f'      #  0x14 -> DELETE
    '\ufffe'    #  0x15 -> UNDEFINED
    '\ufffe'    #  0x16 -> UNDEFINED
    '\ufffe'    #  0x17 -> UNDEFINED
    '\ufffe'    #  0x18 -> UNDEFINED
    '\ufffe'    #  0x19 -> UNDEFINED
    '\ufffe'    #  0x1A -> UNDEFINED
    '\ufffe'    #  0x1B -> UNDEFINED
    '\uf101'    #  0x1C -> RED COLOR SWITCH (CUS)
    '\uf11d'    #  0x1D -> CURSOR RIGHT (CUS)
    '\uf102'    #  0x1E -> GREEN COLOR SWITCH (CUS)
    '\uf103'    #  0x1F -> BLUE COLOR SWITCH (CUS)
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
    '@'         #  0x40 -> COMMERCIAL AT
    'A'         #  0x41 -> LATIN CAPITAL LETTER A
    'B'         #  0x42 -> LATIN CAPITAL LETTER B
    'C'         #  0x43 -> LATIN CAPITAL LETTER C
    'D'         #  0x44 -> LATIN CAPITAL LETTER D
    'E'         #  0x45 -> LATIN CAPITAL LETTER E
    'F'         #  0x46 -> LATIN CAPITAL LETTER F
    'G'         #  0x47 -> LATIN CAPITAL LETTER G
    'H'         #  0x48 -> LATIN CAPITAL LETTER H
    'I'         #  0x49 -> LATIN CAPITAL LETTER I
    'J'         #  0x4A -> LATIN CAPITAL LETTER J
    'K'         #  0x4B -> LATIN CAPITAL LETTER K
    'L'         #  0x4C -> LATIN CAPITAL LETTER L
    'M'         #  0x4D -> LATIN CAPITAL LETTER M
    'N'         #  0x4E -> LATIN CAPITAL LETTER N
    'O'         #  0x4F -> LATIN CAPITAL LETTER O
    'P'         #  0x50 -> LATIN CAPITAL LETTER P
    'Q'         #  0x51 -> LATIN CAPITAL LETTER Q
    'R'         #  0x52 -> LATIN CAPITAL LETTER R
    'S'         #  0x53 -> LATIN CAPITAL LETTER S
    'T'         #  0x54 -> LATIN CAPITAL LETTER T
    'U'         #  0x55 -> LATIN CAPITAL LETTER U
    'V'         #  0x56 -> LATIN CAPITAL LETTER V
    'W'         #  0x57 -> LATIN CAPITAL LETTER W
    'X'         #  0x58 -> LATIN CAPITAL LETTER X
    'Y'         #  0x59 -> LATIN CAPITAL LETTER Y
    'Z'         #  0x5A -> LATIN CAPITAL LETTER Z
    '['         #  0x5B -> LEFT SQUARE BRACKET
    '\xa3'      #  0x5C -> POUND SIGN
    ']'         #  0x5D -> RIGHT SQUARE BRACKET
    '\u2191'    #  0x5E -> UPWARDS ARROW
    '\u2190'    #  0x5F -> LEFTWARDS ARROW
    '\u2500'    #  0x60 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\u2660'    #  0x61 -> BLACK SPADE SUIT
    '\u2502'    #  0x62 -> BOX DRAWINGS LIGHT VERTICAL
    '\u2500'    #  0x63 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\uf122'    #  0x64 -> BOX DRAWINGS LIGHT HORIZONTAL ONE QUARTER UP (CUS)
    '\uf123'    #  0x65 -> BOX DRAWINGS LIGHT HORIZONTAL TWO QUARTERS UP (CUS)
    '\uf124'    #  0x66 -> BOX DRAWINGS LIGHT HORIZONTAL ONE QUARTER DOWN (CUS)
    '\uf126'    #  0x67 -> BOX DRAWINGS LIGHT VERTICAL ONE QUARTER LEFT (CUS)
    '\uf128'    #  0x68 -> BOX DRAWINGS LIGHT VERTICAL ONE QUARTER RIGHT (CUS)
    '\u256e'    #  0x69 -> BOX DRAWINGS LIGHT ARC DOWN AND LEFT
    '\u2570'    #  0x6A -> BOX DRAWINGS LIGHT ARC UP AND RIGHT
    '\u256f'    #  0x6B -> BOX DRAWINGS LIGHT ARC UP AND LEFT
    '\uf12a'    #  0x6C -> ONE EIGHTH BLOCK UP AND RIGHT (CUS)
    '\u2572'    #  0x6D -> BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT
    '\u2571'    #  0x6E -> BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT
    '\uf12b'    #  0x6F -> ONE EIGHTH BLOCK DOWN AND RIGHT (CUS)
    '\uf12c'    #  0x70 -> ONE EIGHTH BLOCK DOWN AND LEFT (CUS)
    '\u25cf'    #  0x71 -> BLACK CIRCLE
    '\uf125'    #  0x72 -> BOX DRAWINGS LIGHT HORIZONTAL TWO QUARTERS DOWN (CUS)
    '\u2665'    #  0x73 -> BLACK HEART SUIT
    '\uf127'    #  0x74 -> BOX DRAWINGS LIGHT VERTICAL TWO QUARTERS LEFT (CUS)
    '\u256d'    #  0x75 -> BOX DRAWINGS LIGHT ARC DOWN AND RIGHT
    '\u2573'    #  0x76 -> BOX DRAWINGS LIGHT DIAGONAL CROSS
    '\u25cb'    #  0x77 -> WHITE CIRCLE
    '\u2663'    #  0x78 -> BLACK CLUB SUIT
    '\uf129'    #  0x79 -> BOX DRAWINGS LIGHT VERTICAL TWO QUARTERS RIGHT (CUS)
    '\u2666'    #  0x7A -> BLACK DIAMOND SUIT
    '\u253c'    #  0x7B -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    '\uf12e'    #  0x7C -> LEFT HALF BLOCK MEDIUM SHADE (CUS)
    '\u2502'    #  0x7D -> BOX DRAWINGS LIGHT VERTICAL
    '\u03c0'    #  0x7E -> GREEK SMALL LETTER PI
    '\u25e5'    #  0x7F -> BLACK UPPER RIGHT TRIANGLE
    '\ufffe'    #  0x80 -> UNDEFINED
    '\uf104'    #  0x81 -> ORANGE COLOR SWITCH (CUS)
    '\ufffe'    #  0x82 -> UNDEFINED
    '\ufffe'    #  0x83 -> UNDEFINED
    '\ufffe'    #  0x84 -> UNDEFINED
    '\uf110'    #  0x85 -> FUNCTION KEY 1 (CUS)
    '\uf112'    #  0x86 -> FUNCTION KEY 3 (CUS)
    '\uf114'    #  0x87 -> FUNCTION KEY 5 (CUS)
    '\uf116'    #  0x88 -> FUNCTION KEY 7 (CUS)
    '\uf111'    #  0x89 -> FUNCTION KEY 2 (CUS)
    '\uf113'    #  0x8A -> FUNCTION KEY 4 (CUS)
    '\uf115'    #  0x8B -> FUNCTION KEY 6 (CUS)
    '\uf117'    #  0x8C -> FUNCTION KEY 8 (CUS)
    '\n'        #  0x8D -> LINE FEED
    '\x0f'      #  0x8E -> SHIFT IN
    '\ufffe'    #  0x8F -> UNDEFINED
    '\uf105'    #  0x90 -> BLACK COLOR SWITCH (CUS)
    '\uf11e'    #  0x91 -> CURSOR UP (CUS)
    '\uf11b'    #  0x92 -> REVERSE VIDEO OFF (CUS)
    '\x0c'      #  0x93 -> FORM FEED
    '\uf121'    #  0x94 -> INSERT (CUS)
    '\uf106'    #  0x95 -> BROWN COLOR SWITCH (CUS)
    '\uf107'    #  0x96 -> LIGHT RED COLOR SWITCH (CUS)
    '\uf108'    #  0x97 -> GRAY 1 COLOR SWITCH (CUS)
    '\uf109'    #  0x98 -> GRAY 2 COLOR SWITCH (CUS)
    '\uf10a'    #  0x99 -> LIGHT GREEN COLOR SWITCH (CUS)
    '\uf10b'    #  0x9A -> LIGHT BLUE COLOR SWITCH (CUS)
    '\uf10c'    #  0x9B -> GRAY 3 COLOR SWITCH (CUS)
    '\uf10d'    #  0x9C -> PURPLE COLOR SWITCH (CUS)
    '\uf11d'    #  0x9D -> CURSOR LEFT (CUS)
    '\uf10e'    #  0x9E -> YELLOW COLOR SWITCH (CUS)
    '\uf10f'    #  0x9F -> CYAN COLOR SWITCH (CUS)
    '\xa0'      #  0xA0 -> NO-BREAK SPACE
    '\u258c'    #  0xA1 -> LEFT HALF BLOCK
    '\u2584'    #  0xA2 -> LOWER HALF BLOCK
    '\u2594'    #  0xA3 -> UPPER ONE EIGHTH BLOCK
    '\u2581'    #  0xA4 -> LOWER ONE EIGHTH BLOCK
    '\u258f'    #  0xA5 -> LEFT ONE EIGHTH BLOCK
    '\u2592'    #  0xA6 -> MEDIUM SHADE
    '\u2595'    #  0xA7 -> RIGHT ONE EIGHTH BLOCK
    '\uf12f'    #  0xA8 -> LOWER HALF BLOCK MEDIUM SHADE (CUS)
    '\u25e4'    #  0xA9 -> BLACK UPPER LEFT TRIANGLE
    '\uf130'    #  0xAA -> RIGHT ONE QUARTER BLOCK (CUS)
    '\u251c'    #  0xAB -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    '\u2597'    #  0xAC -> QUADRANT LOWER RIGHT
    '\u2514'    #  0xAD -> BOX DRAWINGS LIGHT UP AND RIGHT
    '\u2510'    #  0xAE -> BOX DRAWINGS LIGHT DOWN AND LEFT
    '\u2582'    #  0xAF -> LOWER ONE QUARTER BLOCK
    '\u250c'    #  0xB0 -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    '\u2534'    #  0xB1 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    '\u252c'    #  0xB2 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    '\u2524'    #  0xB3 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    '\u258e'    #  0xB4 -> LEFT ONE QUARTER BLOCK
    '\u258d'    #  0xB5 -> LEFT THREE EIGTHS BLOCK
    '\uf131'    #  0xB6 -> RIGHT THREE EIGHTHS BLOCK (CUS)
    '\uf132'    #  0xB7 -> UPPER ONE QUARTER BLOCK (CUS)
    '\uf133'    #  0xB8 -> UPPER THREE EIGHTS BLOCK (CUS)
    '\u2583'    #  0xB9 -> LOWER THREE EIGHTHS BLOCK
    '\uf12d'    #  0xBA -> ONE EIGHTH BLOCK UP AND LEFT (CUS)
    '\u2596'    #  0xBB -> QUADRANT LOWER LEFT
    '\u259d'    #  0xBC -> QUADRANT UPPER RIGHT
    '\u2518'    #  0xBD -> BOX DRAWINGS LIGHT UP AND LEFT
    '\u2598'    #  0xBE -> QUADRANT UPPER LEFT
    '\u259a'    #  0xBF -> QUADRANT UPPER LEFT AND LOWER RIGHT
    '\u2500'    #  0xC0 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\u2660'    #  0xC1 -> BLACK SPADE SUIT
    '\u2502'    #  0xC2 -> BOX DRAWINGS LIGHT VERTICAL
    '\u2500'    #  0xC3 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\uf122'    #  0xC4 -> BOX DRAWINGS LIGHT HORIZONTAL ONE QUARTER UP (CUS)
    '\uf123'    #  0xC5 -> BOX DRAWINGS LIGHT HORIZONTAL TWO QUARTERS UP (CUS)
    '\uf124'    #  0xC6 -> BOX DRAWINGS LIGHT HORIZONTAL ONE QUARTER DOWN (CUS)
    '\uf126'    #  0xC7 -> BOX DRAWINGS LIGHT VERTICAL ONE QUARTER LEFT (CUS)
    '\uf128'    #  0xC8 -> BOX DRAWINGS LIGHT VERTICAL ONE QUARTER RIGHT (CUS)
    '\u256e'    #  0xC9 -> BOX DRAWINGS LIGHT ARC DOWN AND LEFT
    '\u2570'    #  0xCA -> BOX DRAWINGS LIGHT ARC UP AND RIGHT
    '\u256f'    #  0xCB -> BOX DRAWINGS LIGHT ARC UP AND LEFT
    '\uf12a'    #  0xCC -> ONE EIGHTH BLOCK UP AND RIGHT (CUS)
    '\u2572'    #  0xCD -> BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT
    '\u2571'    #  0xCE -> BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT
    '\uf12b'    #  0xCF -> ONE EIGHTH BLOCK DOWN AND RIGHT (CUS)
    '\uf12c'    #  0xD0 -> ONE EIGHTH BLOCK DOWN AND LEFT (CUS)
    '\u25cf'    #  0xD1 -> BLACK CIRCLE
    '\uf125'    #  0xD2 -> BOX DRAWINGS LIGHT HORIZONTAL TWO QUARTERS DOWN (CUS)
    '\u2665'    #  0xD3 -> BLACK HEART SUIT
    '\uf127'    #  0xD4 -> BOX DRAWINGS LIGHT VERTICAL TWO QUARTERS LEFT (CUS)
    '\u256d'    #  0xD5 -> BOX DRAWINGS LIGHT ARC DOWN AND LEFT
    '\u2573'    #  0xD6 -> BOX DRAWINGS LIGHT DIAGONAL CROSS
    '\u25cb'    #  0xD7 -> WHITE CIRCLE
    '\u2663'    #  0xD8 -> BLACK CLUB SUIT
    '\uf129'    #  0xD9 -> BOX DRAWINGS LIGHT VERTICAL TWO QUARTERS RIGHT (CUS)
    '\u2666'    #  0xDA -> BLACK DIAMOND SUIT
    '\u253c'    #  0xDB -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    '\uf12e'    #  0xDC -> LEFT HALF BLOCK MEDIUM SHADE (CUS)
    '\u2502'    #  0xDD -> BOX DRAWINGS LIGHT VERTICAL
    '\u03c0'    #  0xDE -> GREEK SMALL LETTER PI
    '\u25e5'    #  0xDF -> BLACK UPPER RIGHT TRIANGLE
    '\xa0'      #  0xE0 -> NO-BREAK SPACE
    '\u258c'    #  0xE1 -> LEFT HALF BLOCK
    '\u2584'    #  0xE2 -> LOWER HALF BLOCK
    '\u2594'    #  0xE3 -> UPPER ONE EIGHTH BLOCK
    '\u2581'    #  0xE4 -> LOWER ONE EIGHTH BLOCK
    '\u258f'    #  0xE5 -> LEFT ONE EIGHTH BLOCK
    '\u2592'    #  0xE6 -> MEDIUM SHADE
    '\u2595'    #  0xE7 -> RIGHT ONE EIGHTH BLOCK
    '\uf12f'    #  0xE8 -> LOWER HALF BLOCK MEDIUM SHADE (CUS)
    '\u25e4'    #  0xE9 -> BLACK UPPER LEFT TRIANGLE
    '\uf130'    #  0xEA -> RIGHT ONE QUARTER BLOCK (CUS)
    '\u251c'    #  0xEB -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    '\u2597'    #  0xEC -> QUADRANT LOWER RIGHT
    '\u2514'    #  0xED -> BOX DRAWINGS LIGHT UP AND RIGHT
    '\u2510'    #  0xEE -> BOX DRAWINGS LIGHT DOWN AND LEFT
    '\u2582'    #  0xEF -> LOWER ONE QUARTER BLOCK
    '\u250c'    #  0xF0 -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    '\u2534'    #  0xF1 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    '\u252c'    #  0xF2 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    '\u2524'    #  0xF3 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    '\u258e'    #  0xF4 -> LEFT ONE QUARTER BLOCK
    '\u258d'    #  0xF5 -> LEFT THREE EIGTHS BLOCK
    '\uf131'    #  0xF6 -> RIGHT THREE EIGHTHS BLOCK (CUS)
    '\uf132'    #  0xF7 -> UPPER ONE QUARTER BLOCK (CUS)
    '\uf133'    #  0xF8 -> UPPER THREE EIGHTS BLOCK (CUS)
    '\u2583'    #  0xF9 -> LOWER THREE EIGHTHS BLOCK
    '\uf12d'    #  0xFA -> ONE EIGHTH BLOCK UP AND LEFT (CUS)
    '\u2596'    #  0xFB -> QUADRANT LOWER LEFT
    '\u259d'    #  0xFC -> QUADRANT UPPER RIGHT
    '\u2518'    #  0xFD -> BOX DRAWINGS LIGHT UP AND LEFT
    '\u2598'    #  0xFE -> QUADRANT UPPER LEFT
    '\u03c0'    #  0xFF -> GREEK SMALL LETTER PI
)

### Encoding table
encoding_table = codecs.charmap_build(decoding_table)

