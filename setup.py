try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'Instest',
    'author': 'Sadegh',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '1',
    'install_requires': ['nose', 'requests', 'bs4'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Instest'
}

setup(**config)
