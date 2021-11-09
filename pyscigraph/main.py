#!/usr/bin/python
# -*- coding: utf-8 -*-


import click

from .lib import *
from .utils import *
from .VERSION import *


CMD_LINE_EXAMPLES = """
PySciGraph examples:

>> Get JSONLD for a SN publication from its DOI
$ pyscigraph --doi 10.1038/171737a0 

>> Get JSONLD for a SN publication from its full URI
$ pyscigraph --uri http://scigraph.springernature.com/pub.10.1038/171737a0

>> Serialise RDF to Turtle format (default= JSONLD)
$ pyscigraph --doi 10.1038/171737a0 --rdf turtle

>> Get JSONLD for other entity types
$ pyscigraph --uri http://scigraph.springernature.com/clinicaltrial.NCT05060562
$ pyscigraph --uri http://scigraph.springernature.com/grant.2691278
$ pyscigraph --uri http://scigraph.springernature.com/patent.US-10355159-B2
$ pyscigraph --uri http://scigraph.springernature.com/journal.1136213
$ pyscigraph --uri http://www.grid.ac/institutes/grid.511171.2
$ pyscigraph --uri http://scigraph.springernature.com/person.01311060163.26

"""


@click.command()
@click.argument('args', nargs=-1)
@click.option('--doi', help='Retrieve a SciGraph publication via its DOI')
@click.option('--uri', help='Retrieve a SciGraph object via its URI')
@click.option('--rdf', help="Serialize RDF: options are 'jsonld' (default), 'xml', 'turtle', 'nt'", default="jsonld")
@click.option('--examples', is_flag=True, help='More examples')
@click.option('--verbose', is_flag=True, help='Verbose logs')
@click.pass_context
def main_cli(ctx, args=None, doi=None, uri=None, rdf=None,  examples=False, verbose=False):
    """PySciGraph: simple CLI for Springer Nature SciGraph http://scigraph.springernature.com

    Eg: pyscigraph --doi 10.1038/171737a0
    """
    printDebug(f"PySciGraph: {VERSION}\n----------------" , dim=True)

    if examples:
        printDebug(CMD_LINE_EXAMPLES)
        return

    if not (doi or uri) and not args:
        printDebug(ctx.get_help())
        return

    valid_rdf_opts = ['jsonld', 'xml', 'turtle', 'nt']
    if rdf and rdf not in valid_rdf_opts:
        printDebug("RDF options: " + str(valid_rdf_opts), fg="green")
        return

    s = SciGraphClient(verbose=verbose)

    if doi:
        res = s.get_entity_from_doi(doi, rdf)
    elif uri:
        res = s.get_entity_from_uri(uri, rdf)

    if res:
        printDebug("Payload:", dim=True)
        printInfo(res)
        printDebug(f"----------------\nURI: {s.uri}\nTriples: {s.triples_count}", dim=True)
    else:
        printDebug("Not found", fg="green")


if __name__ == '__main__':
    main_cli()
