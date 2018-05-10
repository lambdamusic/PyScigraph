import requests
import rdflib
import rdflib_jsonld
import click
import ontospy

# Examples

# curl -H 'Accept: application/ld+json' 'http://scigraph.springernature.com/things/articles/94a3b24581fa0638d91b2b339cd61f22'

# curl -H 'Accept: application/ld+json' -L 'https://scigraph.springernature.com/api/redirect?doi=10.1038/171737a0'



def scigraph_redirect(val, kind, verbose):
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
    response = get_url_contents(base, headers, payload, verbose)
    if response:
        return parse_rdf(response.url, response.text, verbose)
    else:
        click.secho("Not found", fg="green")
        return False

def scigraph_URI(uri, verbose):
    if not uri.startswith("http"):
        click.secho("Not a valid URI", fg="red")
        return False
    headers = {'Accept': 'application/rdf+xml'}                   
    response = get_url_contents(uri, headers, {}, verbose)
    if response:
        return parse_rdf(response.url, response.text, verbose)
    else:
        click.secho("Not found", fg="green")
        return False



def get_url_contents(base_url, headers, payload, verbose):
    if verbose: click.secho("... requesting rdf", fg="green")
    r = requests.get(base_url, headers=headers, params=payload)
    if r.status_code == 404:
        return False
    else:
        if r.url.startswith("https://"):
            # https ok for retrieval, but rdf payload always uses http uris
            r.url = r.url.replace("https://", "http://")
        if True: click.secho(r.url, fg="green")
        return r


def parse_rdf(entity_uri, rdf_text, verbose):
    """Parse RDF for an entity using ontospy"""    
    x = ontospy.Ontospy()
    if verbose: click.secho("... loading graph", fg="green")
    x.load_rdf(text=rdf_text)
    if verbose: click.secho("... building entity...", fg="green")
    entity = x.build_entity_from_uri(entity_uri)
    if verbose: click.secho("... querying label...", fg="green")
    print(entity.bestLabel())
    if verbose: click.secho("... querying type...", fg="green")
    print(entity.rdftype)
    return entity




