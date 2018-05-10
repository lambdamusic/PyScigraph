#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
simple test queries [for DEVELOPMENT  / not part of official tests]
"""

import click 

from .. import *
from ..lib import *

@click.command()
@click.argument('test_number')
def quicktest_cli(test_number=1):

    test_number = int(test_number)

    if test_number == 1:
        click.secho("Querying DOI...", fg="red")
        scigraph_redirect("10.1038/171737a0", "doi", True)
        click.secho("Querying ISSN...", fg="red")
        scigraph_redirect("2365-631X", "issn", True)
        click.secho("Querying ISBN...", fg="red")
        scigraph_redirect("978-90-481-9751-4", "isbn", True)

 
if __name__ == '__main__':
    quicktest_cli()