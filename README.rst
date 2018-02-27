=======================================================
cbmcodecs - Python encodings for handling PETSCII text.
=======================================================

Introduction
============

The cbmcodecs package provides a number of encodings for handling text from
Commodore 8-bit systems. Much of the credit for this package must go to
Linus Walleij of Triad, as these codecs were built from his PETSCII to Unicode
mappings which can be found at www.df.lth.se/~triad/krad/recode/petscii.html


Usage
=====

Currently there are 4 codecs defined for variations of the PETSCII encoding:

petscii-c64en-lc
    The English version of the Commodore 64 mixed-case character set

petscii-c64en-uc
    The English version of the Commodore 64 upper-case/graphics character set

petscii-vic20en-lc
    The English version of the VIC-20 mixed-case character set

petscii-vic20en-uc
    The English version of the VIC-20 upper-case/graphics character set

Simply import the cbmcodecs package and you will then be able to use them as
with any of the encodings from the standard library::

    import cbmcodecs


    with open('file.seq', encoding='petscii-c64en-lc') as f:
        for line in f:
            print(line)

Python Version Note
===================

Currently only Python 3 is supported (tested on 3.3.3). Support for Python 2.7
may be added in the future, but supporting Python 2 isn't very high on my
priority list.


License
=======

As with the original PETSCII to Unicode mapping files, the cbmcodecs package
is Licensed under the GNU GPL Version 2, see the ``LICENSE.txt`` file for the
full text.
