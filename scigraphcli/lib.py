import requests
import rdflib
import rdflib_jsonld
import click
import ontospy

# curl -H 'Accept: application/ld+json' 'http://scigraph.springernature.com/things/articles/94a3b24581fa0638d91b2b339cd61f22'

# curl -H 'Accept: application/ld+json' -L 'https://scigraph.springernature.com/api/redirect?doi=10.1038/171737a0'


def new_pull_data_with_ontospy(doi):
    base = 'https://scigraph.springernature.com/api/redirect'
    headers = {'Accept': 'application/rdf+xml'}
    payload = {'doi': doi}
    click.secho("... requesting rdf", fg="green")
    r = requests.get(base, headers=headers, params=payload)
    url = r.url
    print(url)
    if url.startswith("https://"):
        # https ok for retrieval, but rdf payload always uses http uris
        url = url.replace("https://", "http://")
    
    x = ontospy.Ontospy()
    click.secho("... loading graph", fg="green")
    x.load_rdf(text=r.text)
    click.secho("... building entity...", fg="green")
    doi_article = x.build_entity_from_uri(url)
    click.secho("... querying label...", fg="green")
    print(doi_article.bestLabel())
    click.secho("... querying type...", fg="green")
    print(doi_article.rdftype)



def pull_data_from_scigraph(doi):
    "Wrapper function"
    uri, rdf = get_doi(doi)
    rdf_parse_type(uri, rdf)


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
    print(r.url)
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
    click.secho("... loading rdf", fg="green")
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




