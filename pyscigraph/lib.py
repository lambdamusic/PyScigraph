import requests
import rdflib
import rdflib_jsonld
import click
import ontospy
from ontospy.core.utils import firstEnglishStringInList

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


    def _do_request(self, uri, rdf_format=""):
        """
        Request data from back end service 
        """
        if not rdf_format or rdf_format == "json-ld" or rdf_format == "jsonld":
            headers = self._default_headers
        elif rdf_format == "nt":
            headers = {'Accept': 'application/n-triples'}
        elif rdf_format == "turtle":
            headers = {'Accept': 'text/turtle'}
        elif rdf_format == "xml":
            headers = {'Accept': 'application/rdf+xml'}

        if self.verbose: click.secho(f"... requesting rdf {uri}", fg="green")

        r = requests.get(uri, headers=headers)

        if r.status_code == 404:
            return False
        else:
            if r.url.startswith("https://"):
                # https ok for retrieval, but rdf payload always uses http uris
                r.url = r.url.replace("https://", "http://")
            if self.verbose: click.secho("Found " + r.url, fg="green")
            return r

    def get_entity_from_uri(self, uri, rdf="json-ld"):
        """
        Simply dereference a scigraph URI
        """
        data = self._do_request(uri, rdf)
        if data:
            rdf_url, rdf_text = data.url, data.text
            return rdf_text
        else:
            return None


    def get_entity_from_doi(self, doi, rdf="json-ld"):
        """
        Simply dereference a scigraph URI based on a DOI
        """
        uri  = self.url + "pub." + doi
        data = self._do_request(uri, rdf)
        if data:
            rdf_url, rdf_text = data.url, data.text
            return rdf_text
        else:
            return None


    # BUG
    # method with ontospy parsing which fails with JSON-LD
    # 
    # def get_entity_from_uri(self, uri):
    #     """
    #     Simply dereference a scigraph URI
    #     """
    #     data = self._do_request({'uri' : uri})
    #     if data:
    #         rdf_url, rdf_text = data.url, data.text
    #         x = ontospy.Ontospy()
    #         if self.verbose: click.secho("... loading graph", fg="green")
    #         x.load_rdf(data=rdf_text, rdf_format="json-ld", verbose=True)
    #         click.secho("Parsing %d triples.." % x.triplesCount(), fg="green")
    #         if self.verbose: click.secho("... building entity...", fg="green")
    #         # build SG Entity
    #         self.entity = x.build_entity_from_uri(rdf_url, SciGraphRdfEntity)
    #         return self.entity
    #     else:
    #         return None

    # def print_report(self):
    #     if self.entity and self.response:
    #         # extract values
    #         label = self.entity.bestLabel() or "N/A"
    #         title = self.entity.title or "N/A"
    #         doi = self.entity.doi or "N/A"
    #         types = " ".join([x for x in self.entity.rdftype_qname])
    #         rdf_url, rdf_text = self.response.url, self.response.text
    #         # print
    #         click.echo(
    #             click.style('URI: ', fg='green') +
    #             click.style(' ' + rdf_url, reset=True))
    #         click.echo(
    #             click.style('DOI: ', fg='green') +
    #             click.style(' ' + doi, reset=True))
    #         click.echo(
    #             click.style('Label: ', fg='green') +
    #             click.style(' ' + label, reset=True))
    #         click.echo(
    #             click.style('Title: ', fg='green') +
    #             click.style(' ' + title, reset=True))
    #         click.echo(
    #             click.style('Types: ', fg='green') +
    #             click.style(' ' + types, reset=True))


# def sgonto(local_name=""):
#     """
#     Util for creating SG ontology URIs eg http://scigraph.springernature.com/ontologies/core/Conference
#     """
#     return "http://scigraph.springernature.com/ontologies/core/" + local_name


# class SciGraphRdfEntity(ontospy.RDF_Entity):
#     def __init__(self, uri, rdftype=None, namespaces=None, ext_model=False):
#         super(SciGraphRdfEntity, self).__init__(uri, rdftype, namespaces,
#                                                 ext_model)

#     def __repr__(self):
#         return "<SciGraphRdfEntity *%s*>" % (self.uri)

#     @property
#     def title(self):
#         return firstEnglishStringInList(
#             self.getValuesForProperty(sgonto("title")))

#     @property
#     def doi(self):
#         return firstEnglishStringInList(
#             self.getValuesForProperty(sgonto("doi")))
