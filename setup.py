import os
import re

from setuptools import setup

VERSION_RE = re.compile(".*__version__ = '(.*?)'", re.MULTILINE)
v_file = os.path.join(os.path.dirname(__file__), 'cbmcodecs', '__init__.py')
with open(v_file) as f:
    version = VERSION_RE.search(f.read()).group(1)

setup(
    name='cbmcodecs',
    description='Python codecs for PETSCII encodings',
    long_description=open('README.rst').read(),
    author='Dan Johnson',
    author_email='dj51d@warbirdsurvivors.com',
    packages=['cbmcodecs'],
    license='GPLv2',
    url='https://github.com/dj51d/cbmcodecs',
    version=version,
    install_requires=[],
    test_suite="tests",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
