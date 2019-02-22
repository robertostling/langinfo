"""Script to plot maps using Basemap

Each line in the input file contains a language/value pair, e.g.:

afr 0.001
eng 0.123
zul 0.981
...

The language identifiers may be either ISO639-3 codes or Glottocodes.
"""

import sys

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

from langinfo.glottolog import Glottolog

def main():
    input_file = sys.argv[1]
    output_file = input_file + '.pdf'
    marker_size = 4
    title = 'Example map'

    with open(input_file) as f:
        data = [line.split() for line in f]
        for line in data:
            if len(line) != 2:
                raise ValueError('Expected two fields, found: ' + str(line))
        data = {k:float(v) for k,v in data}

    lon_lat_v = []
    for k, v in data.items():
        try:
            lang = Glottolog[k]
            lon_lat_v.append((lang.longitude, lang.latitude, v))
        except KeyError:
            print('Warning: language code unknown (%s)' % k, file=sys.stderr)

    m = Basemap(projection='kav7',lon_0=0)
    lons, lats = zip(*[(lon, lat) for lon, lat, _ in lon_lat_v])
    x, y = m(lons, lats)

    def get_color(v):
        n = int(255.0 * v)
        rgb = (n, 0, 255-n)
        return '#%02x%02x%02x' % rgb

    m.drawmapboundary(fill_color='lightblue')
    m.fillcontinents(color='beige',lake_color='lightblue')

    for i, (_, _, v) in enumerate(lon_lat_v):
        m.plot(x[i], y[i], ms=marker_size, marker='o', color=get_color(v),
                markeredgewidth=0)

    plt.title(title, fontsize=12)

    plt.savefig(output_file, dpi=300, format='pdf', bbox_inches='tight')


if __name__ == '__main__': main()

