import codecs
import os
import re

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="twikirefs",
    version=find_version("twikirefs", "__init__.py"),
    desription="CERN CMS Twiki reference runs retriever",
    url="https://github.com/ptrstn/twikirefs",
    author="Peter Stein",
    author_email="peter.stein@cern.ch",
    packages=find_packages(),
    install_requires=["cernrequests", 'beautifulsoup4'],
    entry_points={"console_scripts": ["twikirefs=twikirefs.main:main"]},
)
