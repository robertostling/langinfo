#!/bin/sh

# Glottolog 4.5
wget "https://cdstar.eva.mpg.de/bitstreams/EAEA0-F8BB-0AB6-96FA-0/glottolog_languoid.csv.zip"
wget "https://cdstar.eva.mpg.de/bitstreams/EAEA0-F8BB-0AB6-96FA-0/languages_and_dialects_geo.csv"
# NOTE: this is not tied to a particular version, but parsing the newick file
# was tricky
wget "http://glottolog.org/resourcemap.json?rsc=language" -O resourcemap.json
#wget "https://cdstar.eva.mpg.de/bitstreams/EAEA0-F8BB-0AB6-96FA-0/tree_glottolog_newick.txt"
unzip glottolog_languoid.csv.zip
# This extracts languoid.csv
rm glottolog_languoid.csv.zip

#wget "https://cdstar.shh.mpg.de/bitstreams/EAEA0-983F-6966-3616-0/glottolog_languoid.csv.zip"
#wget "https://cdstar.shh.mpg.de/bitstreams/EAEA0-983F-6966-3616-0/tree_glottolog_newick.txt"
##wget http://glottolog.org/static/trees/tree-glottolog-newick.txt
##wget http://glottolog.org/static/download/glottolog-languoid.csv.zip
#unzip glottolog_languoid.csv.zip
#rm glottolog_languoid.csv.zip

