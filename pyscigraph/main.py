#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import click

from .lib import *
from .VERSION import *


CMD_LINE_EXAMPLES = """
Springer Nature SciGraph http://scigraph.springernature.com is a large linked data repository for the scholarly domain. Using this library one can quickly obtain information ('dereference') for objects stored in this database. 

E.g.:

$ pyscigraph --doi 10.1038/171737a0 

$ pyscigraph --issn 2365-631X

$ pyscigraph --isbn 978-90-481-9751-4

More features will be coming soon.
"""


@click.command()
@click.argument('args', nargs=-1)
@click.option('--doi', help='Retrieve a SciGraph publication via its DOI')
@click.option('--issn', help='Retrieve a SciGraph publication via its ISSN')
@click.option('--isbn', help='Retrieve a SciGraph publication via its ISBN')
@click.option('--uri', help='Retrieve a SciGraph object via its URI')
@click.option('--rdf', help="Serialize RDF: options are 'xml', 'n3', 'turtle', 'nt'")
@click.option('--examples', is_flag=True, help='More examples')
@click.option('--verbose', is_flag=True, help='Verbose logs')
@click.pass_context
def main_cli(ctx, args=None, doi=None, issn=None, isbn=None, uri=None, rdf=None,  examples=False, verbose=False):
    """PySciGraph: simple client for Springer Nature SciGraph.
(eg: pyscigraph --doi 10.1038/171737a0)    
    """

    if examples:
        click.secho(CMD_LINE_EXAMPLES, fg="green")
        return

    if not (doi or issn or isbn or uri) and not args:
        # print dir(search_cli)
        click.secho("Release: " + VERSION, bold=True)
        click.echo(ctx.get_help())
        return

    # valid_rdf_opts = ['ttl', 'xml', 'n3', 'jsonld']
    valid_rdf_opts = ['xml', 'n3', 'turtle', 'nt']
    if rdf and rdf not in valid_rdf_opts:
        click.secho("RDF options: " + str(valid_rdf_opts), fg="green")
        return

    s = SciGraphClient(verbose=verbose)

    if doi:
        s.get_entity_from_id(doi=doi)
    elif issn:
        s.get_entity_from_id(issn=issn)
    elif isbn:
        s.get_entity_from_id(isbn=isbn)
    elif uri:
        s.get_entity_from_id(uri=uri)

    if s.entity:
        if rdf:
            # TODO different serializatiions
            print(s.entity.rdf_source(format=rdf))
        else:
            s.print_report()
    else:
        click.secho("Not found", fg="green")


if __name__ == '__main__':
    main_cli()
