import requests
import rdflib
import rdflib_jsonld
import click


# curl -H 'Accept: application/ld+json' 'http://scigraph.springernature.com/things/articles/94a3b24581fa0638d91b2b339cd61f22'

# curl -H 'Accept: application/ld+json' -L 'https://scigraph.springernature.com/api/redirect?doi=10.1038/171737a0'


def get_doi(doi):
    """
    Follows a redirect

    http://docs.python-requests.org/en/master/user/quickstart/
    """
    base = 'https://scigraph.springernature.com/api/redirect'
    # headers = {'Accept': 'application/ld+json'}
    headers = {'Accept': 'application/rdf+xml'}
    payload = {'doi': doi}
    click.secho("... requesting rdf", fg="green")
    r = requests.get(base, headers=headers, params=payload)
    # print(r.url)
    url = r.url
    if url.startswith("https://"):
        # https ok for retrieval, but rdf payload always uses http uris
        url = url.replace("https://", "http://")
    return (url, r.text)
    


def rdf_parse_type(uri, jsonld_data):
    """parse jsonld as RDF and extract the type info for main URI"""
    click.secho("... init graph", fg="green")
    graph = rdflib.Graph()
    # print jsonld_data
    # graph.parse(data=jsonld_data, format='json-ld')
    graph.parse(data=jsonld_data, format='xml')
    query = """
        select * where {
            <%s> a ?type .
        }
    """ % rdflib.term.URIRef(uri)
    click.secho("... querying type...", fg="green")
    # print query
    # print graph.serialize(format="turtle")
    qres = graph.query(query)
    for row in qres:
        print row['type']




