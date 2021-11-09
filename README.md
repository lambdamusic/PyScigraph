# PySciGraph

Python command line utility for accessing [Springer Nature SciGraph](https://scigraph.springernature.com).

> SN SciGraph is a Linked Open Data repository containing info about 14 million+ research publications from Springer Nature, plus related researchers, grants, patents, organizations, etc..

The code is hosted on Pypi:

- [https://pypi.org/project/pyscigraph/](https://pypi.org/project/pyscigraph/)

[![Downloads](https://pepy.tech/badge/pyscigraph)](https://pepy.tech/project/pyscigraph)

### Example

```bash
# Get JSONLD for a SN publication from its DOI
$ pyscigraph --doi 10.1038/171737a0 

# Get JSONLD for a SN publication from its full URI
$ pyscigraph --uri http://scigraph.springernature.com/pub.10.1038/171737a0

# Serialise RDF to Turtle format (default= JSONLD)
$ pyscigraph --doi 10.1038/171737a0 --rdf turtle

# Get JSONLD for other entity types
$ pyscigraph --uri http://scigraph.springernature.com/clinicaltrial.NCT05060562
$ pyscigraph --uri http://scigraph.springernature.com/grant.2691278
$ pyscigraph --uri http://scigraph.springernature.com/patent.US-10355159-B2
$ pyscigraph --uri http://scigraph.springernature.com/journal.1136213
$ pyscigraph --uri http://www.grid.ac/institutes/grid.511171.2
$ pyscigraph --uri http://scigraph.springernature.com/person.01311060163.26

```

### Install

```
pip install pyscigraph
```


### Status

Prototype. 