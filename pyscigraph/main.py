#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import click

from .lib import *
from .VERSION import *


CMD_LINE_EXAMPLES = """
Springer Nature SciGraph http://scigraph.springernature.com is a large linked data repository of scholarly related metadata. Using this library one can quickly obtain information ('dereference') for objects stored in this database. 

E.g.:

$ pyscigraph --doi 10.1038/171737a0 

$ pyscigraph --uri http://scigraph.springernature.com/pub.10.1038/171737a0

$ pyscigraph --doi 10.1038/171737a0 --rdf turtle
"""


@click.command()
@click.argument('args', nargs=-1)
@click.option('--doi', help='Retrieve a SciGraph publication via its DOI')
@click.option('--uri', help='Retrieve a SciGraph object via its URI')
@click.option('--rdf', help="Serialize RDF: options are 'jsonld' (default), 'xml', 'turtle', 'nt'")
@click.option('--examples', is_flag=True, help='More examples')
@click.option('--verbose', is_flag=True, help='Verbose logs')
@click.pass_context
def main_cli(ctx, args=None, doi=None, uri=None, rdf=None,  examples=False, verbose=False):
    """PySciGraph: simple client for Springer Nature SciGraph.
(eg: pyscigraph --doi 10.1038/171737a0)    
    """

    if examples:
        click.secho(CMD_LINE_EXAMPLES, fg="green")
        return

    if not (doi or uri) and not args:
        click.secho("Release: " + VERSION, bold=True)
        click.echo(ctx.get_help())
        return

    valid_rdf_opts = ['jsonld', 'xml', 'turtle', 'nt']
    if rdf and rdf not in valid_rdf_opts:
        click.secho("RDF options: " + str(valid_rdf_opts), fg="green")
        return

    s = SciGraphClient(verbose=verbose)

    if doi:
        res = s.get_entity_from_doi(doi, rdf)
    elif uri:
        res = s.get_entity_from_uri(uri, rdf)

    if res:
        print(res)
    else:
        click.secho("Not found", fg="green")


if __name__ == '__main__':
    main_cli()
