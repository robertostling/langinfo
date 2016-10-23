#!/bin/sh

wget http://glottolog.org/static/trees/tree-glottolog-newick.txt
wget http://glottolog.org/static/download/glottolog-languoid.csv.zip
unzip glottolog-languoid.csv.zip
rm glottolog-languoid.csv.zip
wget "http://glottolog.org/resourcemap.json?rsc=language" -O resourcemap.json

