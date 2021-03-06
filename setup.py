#!/usr/bin/env python

from setuptools import find_packages, setup

from atlas_tools import __version__


package_name = 'atlas_tools'

setup(
    name=package_name,
    version=__version__,
    author='Alexander Yakushkin',
    author_email='ay@qrator.net',
    packages=find_packages(),
    install_requires=[
        'Cartopy',
        'folium',
        'geopandas',
        'geopy',
        'holoviews',
        'matplotlib',
        'numpy',
        'pandas',
        'Pillow',
        'ripe.atlas.cousteau',
        'scipy',
        'xarray',
    ],
    package_data={
        package_name: ['countries/*'],
    },
    entry_points={
        'console_scripts': [
            'atlas-heatmap = ' +
            '{}.latency_heatmap:HeatMapper.create_run'.format(package_name),

            'atlas-reachability = ' +
            '{}.reachability:do_ip_test'.format(package_name),

            'atlas-countrymap = ' +
            '{}.latency_countrymap:CountryMapper.create_run'.format(package_name),

            'atlas-nslookupmap = ' +
            '{}.nslookup_map:NsLookupMapper.create_run'.format(package_name),
        ],
    },
)
