#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
simple test queries [for DEVELOPMENT  / not part of official tests]
"""

import click 

from .. import *
from ..classmodule import MyClass
from ..funcmodule import my_function


@click.command()
@click.argument('test_number')
def quicktest_cli(test_number=1):

    test_number = int(test_number)

    if test_number == 1:
        my_function('hello world')

        my_object = MyClass('Thomas')
        my_object.say_name()



 
if __name__ == '__main__':
    quicktest()