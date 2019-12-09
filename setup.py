#! usr/bin/python
# -*- coding: utf-8 *-* 

from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

from distutils.core import setup
setup(
  name = 'caspertools',
  packages = ['caspertools'],
  version = '0.2',
  description = 'Tools used for hidden navigation',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'José Fº Queija',
  author_email = 'pepekiko@gmail.com',
  url = 'https://github.com/jfqueija/caspertools',
  download_url = 'https://github.com/jfqueija/caspertools/tarball/0.1',
  keywords = ['hidden', 'navigation', 'tor','privoxy'],
  classifiers = [  
        # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish
        'License :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/jfqueija/caspertools/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'https://github.com/jfqueija/caspertools/stargazers',
        'Source': 'https://github.com/jfqueija/caspertools',
    },
)