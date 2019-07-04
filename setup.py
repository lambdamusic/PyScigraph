from setuptools import setup, find_packages
from os import path
# To use a consistent encoding
from codecs import open

here = path.abspath(path.dirname(__file__))

# trick to manage package versions in one place only
# http://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
import re
VERSIONFILE="pyscigraph/VERSION.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    VERSIONSTRING = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = 'pyscigraph',
    version = VERSIONSTRING,
    description='Python API for accessing Springer Nature SciGraph Linked Open Data.',
    long_description=long_description, 
    long_description_content_type='text/markdown',
    url='https://github.com/lambdamusic/pyscigraph', 
    packages = find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Requests',
        'rdflib',
        'rdflib-jsonld',
        'ontospy',
    ],
    entry_points='''
        [console_scripts]
        pyscigraph = pyscigraph.main:main_cli
    ''',
)