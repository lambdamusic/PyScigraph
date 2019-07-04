# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
Unit test stub 
"""

from __future__ import print_function

import unittest, os, sys, click

from .. import *


class TestOne(unittest.TestCase):

    """
    Tests  
    """

    click.secho("**TESTS**", fg='red')
    client = SciGraphClient(verbose=True)

    def test_001(self):
        click.secho("TEST 001: query using redirect API.", fg='green')

        click.secho("Querying URI...", fg="red")
        print(self.client.get_entity_from_uri("http://www.grid.ac/institutes/grid.443610.4"))


        click.secho("Querying DOI...", fg="red")
        print(self.client.get_entity_from_doi("10.1038/171737a0"))


        click.secho("Completed test succesfully", fg='green')


if __name__ == "__main__":
    unittest.main()