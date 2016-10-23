# langinfo
Python library for interfacing the Glottolog database

## Installing

    python3 setup.py install --user

## Usage

The API is quite simple, please see [relatives.py](examples/relatives.py)
for an example of how to use it.

## Regenerating the database

This repository contains a pickled version of the database for convenience.
To regenerate the database, do the following:

    cd langinfo/data
    ./download.sh
    cd ../..
    python3 cache.py

All data comes from the [Glottolog project](http://glottolog.org/),
so any credit for the actual data goes to them.

