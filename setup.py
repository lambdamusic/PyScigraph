from setuptools import setup, find_packages

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



setup(
    name = 'pyscigraph',
    version = VERSIONSTRING,
    description='Python API for accessing Springer Nature SciGraph Linked Open Data.',
    packages = find_packages(),
    include_package_data=True,
    install_requires=[
        'Click==6.6',
        'Requests==2.18.3',
        'rdflib==4.2.2',
        'rdflib-jsonld==0.4.0',
        'ontospy>=1.9',
    ],
    entry_points='''
        [console_scripts]
        scigraphcli = pyscigraph.main:main_cli
        quicktest_scigraphcli = pyscigraph.tests.quicktest:quicktest_cli
    ''',
)