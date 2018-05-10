#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import click

from .lib import *




CMD_LINE_EXAMPLES = """EXAMPLES:
$ scigraphcli --doi 10.1038/171737a0 

$ scigraphcli --issn 2365-631X

$ scigraphcli --isbn 978-90-481-9751-4
"""




@click.command()
@click.argument('args', nargs=-1)
@click.option('--doi', help='Search a DOI')
@click.option('--issn', help='Search a ISSN')
@click.option('--isbn', help='Search a ISBN')
@click.option('--uri', help='Get a SciGraph URI (default)')
@click.option('--examples', is_flag=True, help='Show some examples')
@click.option('--verbose', is_flag=True, help='Verbose logs')
@click.pass_context
def main_cli(ctx, args=None, doi=None, issn=None, isbn=None, uri=None, examples=False, verbose=False):
    """SciGraph CLI: get Springer Nature SciGraph data.
(see: http://scigraph.springernature.com/explorer/api/)    
    """

    if examples:
        click.secho(CMD_LINE_EXAMPLES, fg="green")
        return

    if not (doi or issn or isbn or uri) and not args:
        # print dir(search_cli)
        click.echo(ctx.get_help())
        return
 
    if doi:
        scigraph_redirect(doi, "doi", verbose)

    if issn:
        scigraph_redirect(issn, "issn", verbose)

    if isbn:
        scigraph_redirect(isbn, "isbn", verbose)

    if uri:
        scigraph_URI(uri, verbose)

    for arg in args:
        print('passed argument :: {}'.format(arg))
        # pull_data_from_scigraph(arg)
        scigraph_URI(arg, verbose)

        

if __name__ == '__main__':
    main_cli()