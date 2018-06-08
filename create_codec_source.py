#! /usr/bin/env python

# automate the codec source code generation process
import os
import glob

try:
    import gencodec
except ImportError:
    print("This script requires the 'gencodec.py' script from the Python Tools directory to be on the import path somewhere.")
    raise SystemExit


outputdir = "cbmcodecs"
os.makedirs(outputdir, exist_ok=True)
gencodec.convertdir("mappings", outputdir+"/")

# remove unneeded things
for mappingfile in glob.glob(outputdir+"/*.mapping"):
    os.remove(mappingfile)
os.remove(outputdir+"/pet_unicode.py")
