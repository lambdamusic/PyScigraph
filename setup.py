from setuptools import setup, find_packages

setup(
    name = 'scigraphcli',
    version = '0.1.0',
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
        scigraphcli = scigraphcli.main:main_cli
        quicktest_scigraphcli = scigraphcli.tests.quicktest:quicktest_cli
    ''',
)