# SynonymFinder
Ranks worda from a word set based on the similarity of the selected word in one or multiple word files.

used to find Synonym of a word

Set file:
format:
Water
river
cake
pond

kill
stab
kiss
murder

empty lines indicate the end and atart of a new set. e.g Water and river are apwrate sets
The first word in a set is used as the selected word. The following worda are ranked based on their similarity with the selected word
A set needs to be created once on first run.
if program is run agqin after a save set file does not have to be read again.
but you may add one to add new or modify exsiting sets

Common word file:
Format:
the
on
a
is 

Common file is optional - words in the common file will be ignored in the similarity calculation
