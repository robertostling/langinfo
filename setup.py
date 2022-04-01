from setuptools import setup

setup(
        name='langinfo',
        version='0.2',
        description='Glottolog database interface',
        url='https://github.com/robertostling/langinfo',
        author='Robert Östling',
        author_email='robert@ling.su.se',
        license='GNU GPLv3',
        packages=['langinfo'],
        package_data={'langinfo': ['data/glottolog.gz', 'data/download.sh']})

