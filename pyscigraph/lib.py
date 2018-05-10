import requests
import rdflib
import rdflib_jsonld
import click
import ontospy

# Examples

# curl -H 'Accept: application/ld+json' 'http://scigraph.springernature.com/things/articles/94a3b24581fa0638d91b2b339cd61f22'

# curl -H 'Accept: application/ld+json' -L 'https://scigraph.springernature.com/api/redirect?doi=10.1038/171737a0'



def pull_redirect_URL(val, kind, verbose):
    base = 'https://scigraph.springernature.com/api/redirect'
    headers = {'Accept': 'application/rdf+xml'}
    if kind == "doi":
        payload = {'doi': val}
    elif kind == "issn":
        payload = {'issn': val} 
    elif kind == "isbn":
        payload = {'isbn': val}     
    else:
        click.secho("Value no valid", fg="red")
        return False                     
    response = _get_url_contents(base, headers, payload, verbose)
    return response 


def pull_lod_URI(uri, verbose):
    if not uri.startswith("http"):
        click.secho("Not a valid URI", fg="red")
        return False
    headers = {'Accept': 'application/rdf+xml'}                   
    response = _get_url_contents(uri, headers, {}, verbose)
    return response




def _get_url_contents(base_url, headers, payload, verbose):
    if verbose: click.secho("... requesting rdf", fg="green")
    r = requests.get(base_url, headers=headers, params=payload)
    if r.status_code == 404:
        return False
    else:
        if r.url.startswith("https://"):
            # https ok for retrieval, but rdf payload always uses http uris
            r.url = r.url.replace("https://", "http://")
        if verbose: click.secho("Found " + r.url, fg="green")
        return r




def reify_rdf_object(entity_uri, rdf_text, verbose):
    """Parse RDF for an entity using ontospy"""    
    x = ontospy.Ontospy()
    if verbose: click.secho("... loading graph", fg="green")
    x.load_rdf(text=rdf_text)
    click.secho("Parsing %d triples.." % x.triplesCount())
    if verbose: click.secho("... building entity...", fg="green")
    entity = x.build_entity_from_uri(entity_uri)
    return entity



def print_report(url, entity):
    click.echo(click.style('URI: ', fg='green') + click.style(' ' + url, reset=True))
    click.echo(click.style('Title: ', fg='green') + click.style(' ' + entity.bestLabel(), reset=True))
    _types = " ".join([x for x in entity.rdftype_qname])
    click.echo(click.style('Types: ', fg='green') + click.style(' ' + _types, reset=True))




