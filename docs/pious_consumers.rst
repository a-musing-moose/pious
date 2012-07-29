==============
Pious Consumer
==============

Consumers are the termination points of pipelines. They consume the final
output of the pipeline. For example they may write to a file in various formats
or insert/replace into a database table or tables.

Existing Consumers
==================

Consumer
    The base class for all Pious consumers. This is the class from which your
    own custom consumers should derive.

DbTable
    Inserts/Replaces values into a table.  Also has options for truncating
    the table prior to the insert etc.

CsvFile
    Writes the data to a CSV file with optional headers and configurable
    configurable separators and escape characters
