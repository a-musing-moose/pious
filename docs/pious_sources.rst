==================
Pious Data Sources
==================

At the base of all Pious transform pipelines are data sources, which as the
name would imply are sources of the raw data you wish to transform.

Pious provides a number of data source primatives along with the provisions to
build upon those primatives to fit your own requires.

Data Source Primitives
======================

Source
    The base class for all data sources. This is the class from which you
    should extend you own custom data sources.

CSVFile
    A Character separated values file. You can specify the separator, escape character etc.

XMLFile
    The build blocks of a SAX based XML file parser

FlatXMLFile
    This extends the XMLFile primitive to provide a simple flat xml importer.
    By flat XML I mean one that bascially imitates a CSV, it doesn't use
    attributes, just flat un-nested elements.

DbIterator
    Iterators the results of an SQL query


