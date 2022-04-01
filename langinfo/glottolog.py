import csv
import json
import re
import os.path
import gzip
import pickle

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
DB_FILENAME = os.path.join(DATA_PATH, 'glottolog.gz')


class Languoid:
    RE_INT = re.compile(r'\d+$')

    def __init__(self, **kwargs):
        self.iso639_3 = None
        self.wals = None
        self.multitree = None
        for k,v in kwargs.items():
            if v == '': v = None
            elif k == 'jsondata': v = json.loads(v)
            elif Languoid.RE_INT.match(v): v = int(v)
            elif k in ('latitude', 'longitude'): v = float(v)
            setattr(self, k, v)
        self.children = []
        self.parent = None

    def ancestor(self, levels=None):
        if self.parent is None or levels <= 0: return self
        else: return self.parent.ancestor(levels-1)

    def descendants(self, predicate=lambda l: True):
        return [child for child in self.children if predicate(child)] + sum(
                [child.descendants(predicate) for child in self.children], [])


class GlottologDatabase:
    def __init__(self, glottocode_languoids, mapping):
        self.languoids = list(glottocode_languoids.values())
        self.glottocode_languoids = glottocode_languoids

        for k in ['hid', 'id']: self._add_index(k)

        ident_map = {
                'iso639-3': 'iso639_3',
                'WALS': 'wals',
                'multitree': 'multitree'
                }

        for resource in mapping['resources']:
            identifiers = resource['identifiers']
            if identifiers:
                if resource['id'] not in self.id_index:
                    print('WARNING:', resource['id'], 'not found')
                    continue
                l = self.id_index[resource['id']]
                for identifier in identifiers:
                    name = ident_map.get(identifier['type'])
                    if name: setattr(l, name, identifier['identifier'])

        for k in ['iso639_3']: self._add_index(k)
        for k in ['wals', 'multitree', 'name']: self._add_index(k, False)

        for l in self.languoids:
            if l.parent_id:
                l.parent = self.glottocode_languoids[l.parent_id]
                l.parent.children.append(l)

        self.toplevel = [l for l in self.languoids
                         if l.level == 'family' and l.parent is None]

    def __getitem__(self, k):
        for index in (self.id_index, self.iso639_3_index, self.name_index):
            v = index.get(k)
            if v: return v
        raise KeyError(k)

    def _add_index(self, k, unique=True):
        index = {}
        for l in self.languoids:
            try:
                v = getattr(l, k)
                if v:
                    if unique:
                        assert v not in index, (k, v)
                        index[v] = l
                    else:
                        index.setdefault(v, []).append(l)
            except AttributeError:
                pass
        setattr(self, k+'_index', index)

    @staticmethod
    def read(languoid_file, geo_file, alias_file):
        languoids = {}
        with open(languoid_file, newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            header = next(reader)
            for row in reader:
                l = Languoid(**dict(zip(header, row)))
                languoids[l.id] = l
        with open(geo_file, newline='') as f:
            reader = csv.DictReader(f, delimiter=',', quotechar='"')
            for row in reader:
                if row['glottocode'] in languoids:
                    languoids[row['glottocode']].macroarea = row['macroarea']

        with open(alias_file, 'r', encoding='utf-8') as f:
            mapping = json.load(f)
        return GlottologDatabase(languoids, mapping)


def build_database():
    return GlottologDatabase.read(
            os.path.join(DATA_PATH, 'languoid.csv'),
            os.path.join(DATA_PATH, 'languages_and_dialects_geo.csv'),
            os.path.join(DATA_PATH, 'resourcemap.json'))


def cache_database():
    with gzip.open(DB_FILENAME, 'wb') as f:
        pickle.dump(build_database(), f, -1)


if os.path.exists(DB_FILENAME):
    with gzip.open(os.path.join(DATA_PATH, 'glottolog.gz'), 'rb') as f:
        Glottolog = pickle.load(f)
else:
    Glottolog = build_database()

