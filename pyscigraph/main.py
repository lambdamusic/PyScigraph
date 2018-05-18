#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import click

from .lib import *




CMD_LINE_EXAMPLES = """EXAMPLES:
$ pyscigraph --doi 10.1038/171737a0 

$ pyscigraph --issn 2365-631X

$ pyscigraph --isbn 978-90-481-9751-4
"""




@click.command()
@click.argument('args', nargs=-1)
@click.option('--doi', help='Search a DOI')
@click.option('--issn', help='Search a ISSN')
@click.option('--isbn', help='Search a ISBN')
@click.option('--uri', help='Get a SciGraph URI (default)')
@click.option('--rdf', help='Return RDF: ttl, xml, n3, jsonld')
@click.option('--examples', is_flag=True, help='Show some examples')
@click.option('--verbose', is_flag=True, help='Verbose logs')
@click.pass_context
def main_cli(ctx, args=None, doi=None, issn=None, isbn=None, uri=None, rdf=None,  examples=False, verbose=False):
    """PySciGraph: client for Springer Nature SciGraph APIs.
(see: http://scigraph.springernature.com)    
    """

    if examples:
        click.secho(CMD_LINE_EXAMPLES, fg="green")
        return

    if not (doi or issn or isbn or uri) and not args:
        # print dir(search_cli)
        click.echo(ctx.get_help())
        return
 
    valid_rdf_opts = ['ttl', 'xml', 'n3', 'jsonld']
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
            print s.entity.rdf_source()
        else:
            s.print_report()
    else:
        click.secho("Not found", fg="green")


if __name__ == '__main__':
    main_cli()