# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Spreadshirt API Client',
    'author': 'Peter Schröder',
    'url': 'https://github.com/phoet/spreadsnake',
    # 'download_url': 'Where to download it.',
    'author_email': 'phoetmail@googlemail.com',
    'version': '0.0.1',
    # 'install_requires': ['nose', 'lxml', 'BeautifulSoup'],
    'install_requires': ['nose', 'BeautifulSoup4'],
    'packages': ['spreadsnake'],
    'scripts': [],
    'name': 'SpreadSnake'
}

setup(**config)
