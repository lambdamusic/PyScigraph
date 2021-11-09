import requests
import rdflib
import click

from .utils import *


# Examples

# curl -H 'Accept: application/ld+json' 'https://scigraph.springernature.com/pub.10.1007/978-1-62703-715-0_2'



class SciGraphClient(object):
    """
    Simple class for accessing SciGraph entities
    """
    url = 'https://scigraph.springernature.com/'
    _default_headers = {'Accept': 'application/ld+json'}

    def __init__(self, *args, **kwargs):
        allowed_keys = ['verbose']
        self.__dict__.update((k, False) for k in allowed_keys)
        self.__dict__.update(
            (k, v) for k, v in kwargs.items() if k in allowed_keys)

        self.uri = None
        self.data = None # the raw data coming back from SciGraph
        self.rdfgraph = rdflib.ConjunctiveGraph()

    @property
    def triples_count(self):
        """
        Simply dereference a scigraph URI
        """
        return len(self.rdfgraph)

    def get_entity_from_uri(self, uri, rdf_format):
        """
        Simply dereference a scigraph URI
        """
        data = self._do_request(uri, rdf_format)
        if data:
            self.uri = uri
            self.data = data.text
            self._build_rdf_object(rdf_format)
            return self.data
        else:
            return None


    def get_entity_from_doi(self, doi, rdf_format):
        """
        Simply dereference a scigraph URI based on a DOI
        """
        uri  = self.url + "pub." + doi
        data = self._do_request(uri, rdf_format)
        if data:
            self.uri = uri
            self.data = data.text
            return self.data
        else:
            return None


    def _do_request(self, uri, rdf_format):
        """
        Request data from back end service 
        """
        
        if not rdf_format or rdf_format == "json-ld" or rdf_format == "jsonld":
            headers = {'Accept': 'application/ld+json'}
        elif rdf_format == "nt":
            headers = {'Accept': 'application/n-triples'}
        elif rdf_format == "turtle":
            headers = {'Accept': 'text/turtle'}
        elif rdf_format == "xml":
            headers = {'Accept': 'application/rdf+xml'}

        if self.verbose: printDebug(f">> Requesting format '{rdf_format}' from URI: {uri}", dim=True)

        response = requests.get(uri, headers=headers)

        if response.status_code == 404:
            return False
        else:
            if response.url.startswith("https://"):
                # https ok for retrieval, but rdf payload always uses http uris
                response.url = response.url.replace("https://", "http://")
            if self.verbose: printDebug(f">> Found: {response.url}\n----------------", dim=True)
            return response


    def _build_rdf_object(self, rdf_format):
        """Use rdflib to create a graph using the scigraph data returned
        """
        if rdf_format == "jsonld":
            rdf_format = "json-ld" # fix for rdflib
        if self.data:
            self.rdfgraph.parse(data=self.data, format=rdf_format)

