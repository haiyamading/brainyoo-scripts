brainyoo-scripts
================

Some brainyoo data python scripts

E.g. Convert

1,1-1,爱,ai4,to love; affection; to be fond of; to like,

to

爱,to love; affection; to be fond of; to like,ai4


python csv2brainyoo.py -i input\hsk\hsk_level_1.csv -o output\hsk\hsk1.csv --mapping=iiqha

The mapping iigha will instruct the parser to ignore the first two entries and map question, hint and answer accordingly.
