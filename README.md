# PySciGraph

Python command line utility for accessing [Springer Nature SciGraph](https://scigraph.springernature.com).

> SciGraph is a large Linked Open Data repository containing info about 12 million+ research publications, plus grants, conferences, organizations, classifications etc..

The code is hosted on Pypi:

- [https://pypi.org/project/pyscigraph/](https://pypi.org/project/pyscigraph/)

### Example

```
# check if an object is on SciGraph via its URI
$ pyscigraph --uri http://www.grid.ac/institutes/grid.443610.4

# check if a publication is on SciGraph via its DOI
$ pyscigraph --doi 10.1038/171737a0

# retrieve all metadata via an RDF serialization
$ pyscigraph --doi 10.1038/171737a0 --rdf jsonld

```

### Install

```
pip install pyscigraph
```


### Status

Prototype. 