# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
Misc utils
"""

from colorama import Fore, Style
import click



def printDebug(text, mystyle="", err=True, **kwargs):
    """Wrapper around click.secho() for printing in colors with various defaults.

    :kwargs = you can do printDebug("s", bold=True)

    2018-12-06: by default print to standard error stderr (err=True)
    https://click.palletsprojects.com/en/5.x/api/#click.echo
    This means that the output is ok with `less` and when piped to other commands (or files)

    Styling output:
    <http://click.pocoo.org/5/api/#click.style>
    Styles a text with ANSI styles and returns the new string. By default the styling is self contained which means that at the end of the string a reset code is issued. This can be prevented by passing reset=False.

    This works also with inner click styles eg

    ```python
    uri, title = "http://example.com", "My ontology"
    printDebug(click.style("[%d]" % 1, fg='blue') +
               click.style(uri + " ==> ", fg='black') +
               click.style(title, fg='red'))
    ```

    Or even with Colorama

    ```
    from colorama import Fore, Style

    printDebug(Fore.BLUE + Style.BRIGHT + "[%d]" % 1 + 
            Style.RESET_ALL + uri + " ==> " + Fore.RED + title + 
            Style.RESET_ALL)
    ```


    Examples:

    click.echo(click.style('Hello World!', fg='green'))
    click.echo(click.style('ATTENTION!', blink=True))
    click.echo(click.style('Some things', reverse=True, fg='cyan'))
    Supported color names:

    black (might be a gray)
    red
    green
    yellow (might be an orange)
    blue
    magenta
    cyan
    white (might be light gray)
    reset (reset the color code only)
    New in version 2.0.

    Parameters:
    text – the string to style with ansi codes.
    fg – if provided this will become the foreground color.
    bg – if provided this will become the background color.
    bold – if provided this will enable or disable bold mode.
    dim – if provided this will enable or disable dim mode. This is badly supported.
    underline – if provided this will enable or disable underline.
    blink – if provided this will enable or disable blinking.
    reverse – if provided this will enable or disable inverse rendering (foreground becomes background and the other way round).
    reset – by default a reset-all code is added at the end of the string which means that styles do not carry over. This can be disabled to compose styles.

    """

    if mystyle == "comment":
        click.secho(text, dim=True, err=err)
    elif mystyle == "important":
        click.secho(text, bold=True, err=err)
    elif mystyle == "normal":
        click.secho(text, reset=True, err=err)
    elif mystyle == "red" or mystyle == "error":
        click.secho(text, fg='red', err=err)
    elif mystyle == "green":
        click.secho(text, fg='green', err=err)
    else:
        click.secho(text, err=err, **kwargs)




def printInfo(text, mystyle="", **kwargs):
    """Wrapper around printDebug for printing ALWAYS to stdout
    This means that the output can be grepped etc..
    NOTE this output will be picked up by pipes etc..

    Fixes https://github.com/lambdamusic/Ontospy/issues/76
    """
    printDebug(text, mystyle, False, **kwargs)

