# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
Unit test stub 
"""

from __future__ import print_function

import unittest, os, sys, click


class TestOne(unittest.TestCase):

    """
    Tests  
    """

    click.secho("**TEST**", fg='red')

    def test_001(self):
        print("Nothing to test yet")



if __name__ == "__main__":
    unittest.main()