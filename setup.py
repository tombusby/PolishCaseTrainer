try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Polish Case Trainer',
    'author': 'Thomas Busby',
    'url': 'https://github.com/tombusby/PolishCaseTrainer',
    'download_url': 'https://github.com/tombusby/PolishCaseTrainer',
    'author_email': 'tom@busby.ninja',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['polish_case_trainer'],
    'scripts': [],
    'name': 'polish_case_trainer'
}

setup(**config)
