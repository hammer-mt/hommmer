import pathlib
from setuptools import setup, find_packages
HERE = pathlib.Path(__file__).parent
VERSION = '0.0.0.1'
PACKAGE_NAME = 'hommmer'
AUTHOR = 'mike taylor'
AUTHOR_EMAIL = 'mike@saxifrage.xyz'
URL = 'https://github.com/hammer-mt/hommmer'
LICENSE = 'MIT'
DESCRIPTION = 'A simple Marketing Mix Modeling library in Python'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = [
    'numpy',
    'pandas',
    'matplotlib',
    'statsmodels'
]
setup(name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages()
    )
