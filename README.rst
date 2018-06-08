==========================================================================
cbmcodecs - Python encodings for handling PETSCII and C64 Screencode text.
==========================================================================

Introduction
============

The cbmcodecs package provides a number of encodings for handling text from
Commodore 8-bit systems. Much of the credit for this package must go to
Linus Walleij of Triad, as these codecs were built from his PETSCII to Unicode
mappings which can be found at http://www.df.lth.se/~triad/krad/recode/petscii.html
The screencodes codec was created by hand later and borrows from them.


Usage
=====

Currently there are four codecs defined for variations of the PETSCII encoding:

petscii-c64en-lc
    The English version of the Commodore 64 mixed-case character set

petscii-c64en-uc
    The English version of the Commodore 64 upper-case/graphics character set

petscii-vic20en-lc
    The English version of the VIC-20 mixed-case character set

petscii-vic20en-uc
    The English version of the VIC-20 upper-case/graphics character set


There are two codecs defined to handle the Screencode (POKE) encoding:

screencode-c64-lc
    Mixed-case mapping to screencodes (POKE) used by the Commodore 64 and Vic20

screencode-c64-uc
    Upper-case/graphics mapping to screencodes (POKE) used by the Commodore 64 and Vic20


Simply import the cbmcodecs package and you will then be able to use them as
with any of the encodings from the standard library::

    import cbmcodecs


    with open('file.seq', encoding='petscii-c64en-lc') as f:
        for line in f:
            print(line)


Python Version Note
===================

Currently only Python 3 is supported (tested on 3.5+). May or may not work on older versions.


License
=======

As with the original PETSCII to Unicode mapping files, the cbmcodecs package
is Licensed under the GNU GPL Version 2, see the ``LICENSE.txt`` file for the
full text.


Unicode symbols used
====================
Aside from the regular alphanumerics and symbols, the unicode mapping uses the
following unicode block drawing and other symbols to mimic a bunch of PETSCII characters:

£ π ✓ ← ↑ ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ ╭ ╮ ╯ ╰
╱ ╲ ╳ ▁ ▂ ▃ ▄ ▌ ▍ ▎ ▏ ▒ ▔ ▕ ▖ ▗ ▘ ▚ ▝
○ ● ◤ ◥ ♠ ♣ ♥ ♦


Credits
=======

Linus Walleij - Original C64 and VIC-20 mappings
Dan Johnson - Translation of C64 & VIC-20 mappings to python codecs
Irmen de Jong - Screencode mappings, bug fixes and unit tests.
