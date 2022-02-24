import re
from pkg_resources import parse_requirements
from setuptools import find_packages, setup

README_FILE = 'README.md'
REQUIREMENTS_FILE = 'requirements.txt'
VERSION_FILE = 'counterattack/_version.py'
VERSION_REGEXP = r'^__version__ = \'(\d+\.\d+\.\d+)\''

r = re.search(VERSION_REGEXP, open(VERSION_FILE).read(), re.M)
if r is None:
    raise RuntimeError(f'Unable to find version string in {VERSION_FILE}.')

version = r.group(1)
long_description = open(README_FILE, encoding='utf-8').read()
install_requires = [str(r) for r in parse_requirements(open(REQUIREMENTS_FILE, 'rt'))]

setup(
    name='counterattack',
    version=version,
    description='counterattack is a collection of web scraping and football entity tools for Counter Attack: The Football Strategy Game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ryan Saxe',
    author_email='ryancsaxe@gmail.com',
    url='https://github.com/RyanSaxe/mtg',
    packages=find_packages(),
    install_requires=install_requires,
)