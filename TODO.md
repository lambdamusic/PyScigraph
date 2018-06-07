# TODOs

- better rendering of results from cmd line

- catch error with wrong URL

- add usage to README

* return other RDF formats (sync names with ontospy) @done
* allow to instantiate Ontospy ORM with SG structures @done
* add to Pypi @done
* raw rdf return (turtle by default) @done
* refactor into class model @done

### Ideal interaction

$ scigraph --uri XXXXX
XX triples
URI: ..
Title: ...
Types: ...
Triples: xxx

$ scigraph --doi XXXXX
XX triples
URI: ..
Title: ...
Authors: xxx
Year: xxxx
Journal: xxxx

$ scigraph --issn XXXXX --rdf jsonld
XX triples
URI: ..
Title: ...
JournalBrand: xxxx

$ scigraph --isbn XXXXX --rdf jsonld
XX triples
URI: ..
Title: ...
Authors: xxx
Year: xxxx
Book Series: xxxx
