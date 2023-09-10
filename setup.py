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


setup(
    name="find-similar",
    version="1.2.1",
    packages=["find_similar"],
    include_package_data=True,
    license="MIT",
    description="Algorithm to define similarity rating between objects",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/findsimilar/find-similar",
    author="findsimilar",
    author_email="help@findsimilar.org",
    keywords=["rating", "similarity", "tokens"],
    install_requires=[
        'pymorphy3==1.2.0',
        "nltk==3.8.1",
        "pydantic==1.10.7",
    ],
    python_requires=">=3",
    classifiers=[
        'Development Status :: 4 - Beta'
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Linguistic",
    ],
)
