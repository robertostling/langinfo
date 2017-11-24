#!/bin/sh

wget "https://cdstar.shh.mpg.de/bitstreams/EAEA0-983F-6966-3616-0/glottolog_languoid.csv.zip"
wget "https://cdstar.shh.mpg.de/bitstreams/EAEA0-983F-6966-3616-0/tree_glottolog_newick.txt"
#wget http://glottolog.org/static/trees/tree-glottolog-newick.txt
#wget http://glottolog.org/static/download/glottolog-languoid.csv.zip
unzip glottolog_languoid.csv.zip
rm glottolog_languoid.csv.zip
wget "http://glottolog.org/resourcemap.json?rsc=language" -O resourcemap.json

