"""CBM "encodings" Package

Encodings for PETSCII generated with gencodec.py from the Unicode mappings
defined by Linus Walleij, see
http://www.df.lth.se/~triad/krad/recode/petscii.html

The following encodings are defined by this package:

petscii-c64en-lc - Mixed-case mapping used by the Commodore 64
petscii-c64en-uc - Upper-case/graphics mapping used by the Commodore 64
petscii-vic20en-lc - Mixed-case mapping used by the Commodore VIC-20
petscii-vic20en-uc - Upper-case/graphics mapping used by the VIC-20

"""
import codecs

from . import petscii_c64en_lc
from . import petscii_c64en_uc
from . import petscii_vic20en_lc
from . import petscii_vic20en_uc

__version__ = '0.1.1'
__all__ = []

petscii_codecs = {
    'petscii-c64en-lc': petscii_c64en_lc.getregentry(),
    'petscii-c64en-uc': petscii_c64en_uc.getregentry(),
    'petscii-vic20en-lc': petscii_vic20en_lc.getregentry(),
    'petscii-vic20en-uc': petscii_vic20en_uc.getregentry(),
}


def search_fn(encoding):
    return petscii_codecs.get(encoding, None)


codecs.register(search_fn)
