"""CBM "encodings" Package

Encodings for PETSCII generated with gencodec.py from the Unicode mappings
defined by Linus Walleij, see
http://www.df.lth.se/~triad/krad/recode/petscii.html

The screencode mappings were written by hand by Irmen de Jong.

The following encodings are defined by this package:

petscii-c64en-lc - Mixed-case mapping used by the Commodore 64
petscii-c64en-uc - Upper-case/graphics mapping used by the Commodore 64
petscii-vic20en-lc - Mixed-case mapping used by the Commodore VIC-20
petscii-vic20en-uc - Upper-case/graphics mapping used by the VIC-20
screencode-c64-lc - Mixed-case mapping to screencodes (POKE) used by the Commodore 64 and Vic20
screencode-c64-uc - Upper-case/graphics mapping to screencodes (POKE) used by the Commodore 64 and Vic20
"""
import codecs

from . import petscii_c64en_lc
from . import petscii_c64en_uc
from . import petscii_vic20en_lc
from . import petscii_vic20en_uc
from . import screencode_c64_lc
from . import screencode_c64_uc

__version__ = '0.2.1'
__all__ = []

petscii_codecs = {
    'petscii-c64en-lc': petscii_c64en_lc.getregentry(),
    'petscii-c64en-uc': petscii_c64en_uc.getregentry(),
    'petscii-vic20en-lc': petscii_vic20en_lc.getregentry(),
    'petscii-vic20en-uc': petscii_vic20en_uc.getregentry(),
    'screencode-c64-lc': screencode_c64_lc.getregentry(),
    'screencode-c64-uc': screencode_c64_uc.getregentry()
}


def search_fn(encoding):
    return petscii_codecs.get(encoding, None)


codecs.register(search_fn)
