import sys

from langinfo.glottolog import Glottolog

level = int(sys.argv[2]) if len(sys.argv) > 2 else 1

try:
    ancestor = Glottolog[sys.argv[1]].ancestor(level)
    for lang in ancestor.descendants(
            lambda l: l.level == 'language' and l.iso639_3):
        print(lang.iso639_3 + '\t' + lang.name)
except KeyError:
    print('Unknown language ID', file=sys.stderr)

