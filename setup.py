"""
Setup.py file to build and install package
"""
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding='utf-8') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def read(filename):
    """
    read some file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


PACKAGE_PYPI_NAME = 'find-similar'
PACKAGE_NAME = "find_similar"

PROJECT_URLS = {
    'Documentation': 'https://docs.findsimilar.org',
    'Source': 'https://github.com/findsimilar/find-similar',
    'Tracker': 'https://github.com/findsimilar/find-similar/issues',
    'Release notes': 'https://github.com/findsimilar/find-similar/releases',
    'Changelog': 'https://github.com/findsimilar/find-similar/releases',
    'Download': 'https://pypi.org/project/find-similar/',
}

setup(
    name=PACKAGE_PYPI_NAME,
    version="1.5.1",
    packages=[PACKAGE_NAME],
    package_data={
        PACKAGE_NAME: ['*', '*/*', '*/*/*']
    },
    include_package_data=True,
    license="MIT",
    description="Algorithm to define similarity rating between objects",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/findsimilar/find-similar",
    author="findsimilar",
    author_email="quill@craftsman.lol",
    keywords=["rating", "similarity", "tokens"],
    install_requires=[
        'pymorphy3==1.2.0',
        "nltk==3.8.1",
        "pydantic==1.10.7",
        'PyYAML==6.0.1',
    ],
    python_requires=">=3",
    classifiers=[
        'Development Status :: 4 - Beta',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Linguistic",
    ],
    project_urls= PROJECT_URLS,
)
