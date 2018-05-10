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
 

    # steps:
    # get url and rdf content 
    # instantiate entity
    # get useful fields from entity and print out


    if doi:
        response = pull_redirect_URL(doi, "doi", verbose)
    if issn:
        response = pull_redirect_URL(issn, "issn", verbose)
    if isbn:
        response = pull_redirect_URL(isbn, "isbn", verbose)

    if uri:
        reponse = pull_lod_URI(uri, verbose)

    for arg in args:
        #multiple args ignored, only last one kept
        # print('passed argument :: {}'.format(arg))
        response  = pull_lod_URI(arg, verbose)

    if response:
        entity = reify_rdf_object(response.url, response.text, verbose)
        print_report(response.url, entity)
    else:
        click.secho("Not found", fg="green")


if __name__ == '__main__':
    main_cli()