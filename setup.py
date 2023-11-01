"""
Setup.py file to build and install package
"""
import codecs
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


# PACKAGE_PYPI_NAME = 'find-similar'
PACKAGE_NAME = "find_similar"


def open_local(paths, mode="r", encoding="utf8"):
    """
    Open local package file
    :param paths: list of paths to file
    :param mode: read, write, ...
    :param encoding: Encoding
    :return: file object
    """
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)
    return codecs.open(path, mode, encoding)


def get_value_from_package_info(line, value, old_value):
    """
    Get value from text line
    :param line: file text line
    :param value: value to parse
    :param old_value: if value has already founded
    :return:
    """
    if old_value:
        return old_value
    if line.startswith(value):
        _, val = line.split('=')
        return val.strip().replace("'", '')
    return None


with open_local([PACKAGE_NAME, "package.py"]) as fp:
    package_pypi_name, package_version, package_status = None, None, None
    for file_line in fp:
        package_pypi_name = get_value_from_package_info(file_line, 'name', package_pypi_name)
        package_version = get_value_from_package_info(file_line, 'version', package_version)
        package_status = get_value_from_package_info(file_line, 'status', package_status)

    if not (package_pypi_name and package_version and package_status):
        raise RuntimeError("Unable to determine Package Info.")

PROJECT_URLS = {
    'Documentation': 'https://docs.findsimilar.org',
    'Source': 'https://github.com/findsimilar/find-similar',
    'Tracker': 'https://github.com/findsimilar/find-similar/issues',
    'Release notes': 'https://github.com/findsimilar/find-similar/releases',
    'Changelog': 'https://github.com/findsimilar/find-similar/releases',
    'Download': 'https://pypi.org/project/find-similar/',
}

setup(
    name=package_pypi_name,
    version=package_version,
    packages=[PACKAGE_NAME],
    package_data={
        PACKAGE_NAME: ['*', '*/*', '*/*/*']
    },
    include_package_data=True,
    license="MIT",
    description="User-friendly library to find similar objects",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/findsimilar/find-similar",
    author="findsimilar",
    author_email="quill@craftsman.lol",
    keywords=[
        'python',
        'search',
        'machine-learning',
        'natural-language-processing',
        'find',
        'words',
        'texts',
        'similar'
        ],
    install_requires=[
        'setuptools',
        'nltk == 3.8.1',
        'pymorphy3 == 1.2.1',
        'pydantic == 2.4.2',
        'PyYAML == 6.0.1',
    ],
    python_requires=">=3",
    classifiers=[
        f'Development Status :: {package_status}',
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
