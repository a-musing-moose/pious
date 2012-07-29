===========
Pious Pipes
===========

Pipes are similar to data sources in that they act as iterators. The different
is that they take a datasource (or another pipe) as an input.  Pipes therefore
are the building blocks of your transformation pipeline.

Pious provides a goodly collection of pipe with which to build your pipelines
providing filters, field transformers along with more complex pipes like
fork which takes a pipeline and splits it into 2 or multiple parallel pipes.

Existing Pipes
==============

Pipe
    The base pipe class that all others extend. This should be the basis of
    your own pipe implementations

Ensure
    Ensure that the dict passing through has certain keys and that if they are
    not present then we set a default value

Filter
    Skips items that match certain criteria

Fork
    Splits the pipe into 2 parallel pipes - i.e. the output of the bound
    iterator is fed into the input of 2 pipelines.


