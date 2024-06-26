# FindSimilar

User-friendly library to find similar objects

You can find **Full Project Documentation** [here][documentation_path]

<hr>

#### Workflows
[![Tests](https://github.com/findsimilar/find-similar/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/findsimilar/find-similar/actions/workflows/run-tests.yml)
[![Pylint](https://github.com/findsimilar/find-similar/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/findsimilar/find-similar/actions/workflows/lint.yml)

#### PyPi
[![Version](https://img.shields.io/pypi/v/find-similar.svg)](https://pypi.python.org/pypi/find-similar/)
[![Development Status](https://img.shields.io/pypi/status/find-similar.svg)](https://pypi.python.org/pypi/find-similar)
[![Python version](https://img.shields.io/pypi/pyversions/find-similar.svg)](https://pypi.python.org/pypi/find-similar/)
[![Wheel](https://img.shields.io/pypi/wheel/find-similar.svg)](https://pypi.python.org/pypi/find-similar/)

### Anaconda
[![Version](https://anaconda.org/quillcraftsman/find-similar/badges/version.svg)](https://anaconda.org/quillcraftsman/find-similar/)
[![Last Updated](https://anaconda.org/quillcraftsman/find-similar/badges/latest_release_date.svg)](https://anaconda.org/quillcraftsman/find-similar/)
[![Platforms](https://anaconda.org/quillcraftsman/find-similar/badges/platforms.svg)](https://anaconda.org/quillcraftsman/find-similar/)

### License
[![License](https://img.shields.io/pypi/l/find-similar)](https://github.com/findsimilar/find-similar/blob/main/LICENSE)

#### Support
[![Documentation](https://img.shields.io/badge/docs-0094FF.svg)][documentation_path]
[![Discussions](https://img.shields.io/badge/discussions-ff0068.svg)](https://github.com/findsimilar/find-similar/discussions/)
[![Issues](https://img.shields.io/badge/issues-11AE13.svg)](https://github.com/findsimilar/find-similar/issues/)

#### PyPi Downloads
[![Day Downloads](https://img.shields.io/pypi/dd/find-similar)](https://pepy.tech/project/find-similar)
[![Week Downloads](https://img.shields.io/pypi/dw/find-similar)](https://pepy.tech/project/find-similar)
[![Month Downloads](https://img.shields.io/pypi/dm/find-similar)](https://pepy.tech/project/find-similar)
#### Anaconda Downloads
[![Anaconda](https://anaconda.org/quillcraftsman/find-similar/badges/downloads.svg)](https://anaconda.org/quillcraftsman/find-similar/)

#### Languages
[![Languages](https://img.shields.io/github/languages/count/findsimilar/find-similar)](https://github.com/findsimilar/find-similar)
[![Top Language](https://img.shields.io/github/languages/top/findsimilar/find-similar)](https://github.com/findsimilar/find-similar)

#### Development
- [![Release date](https://img.shields.io/github/release-date/findsimilar/find-similar
)](https://github.com/findsimilar/find-similar/releases)
[![Last Commit](https://img.shields.io/github/last-commit/findsimilar/find-similar/main
)](https://github.com/findsimilar/find-similar)
- [![Issues](https://img.shields.io/github/issues/findsimilar/find-similar
)](https://github.com/findsimilar/find-similar/issues/)
[![Closed Issues](https://img.shields.io/github/issues-closed/findsimilar/find-similar
)](https://github.com/findsimilar/find-similar/issues/)
- [![Pull Requests](https://img.shields.io/github/issues-pr/findsimilar/find-similar
)](https://github.com/findsimilar/find-similar/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/findsimilar/find-similar
)](https://github.com/findsimilar/find-similar/pulls)
- [![Discussions](https://img.shields.io/github/discussions/findsimilar/find-similar
)](https://github.com/findsimilar/find-similar/discussions/)

#### Repository Stats

[![Stars](https://img.shields.io/github/stars/findsimilar/find-similar
)](https://github.com/findsimilar/find-similar)
[![Contributors](https://img.shields.io/github/contributors/findsimilar/find-similar
)](https://github.com/findsimilar/find-similargraphs/contributors)
[![Forks](https://img.shields.io/github/forks/findsimilar/find-similar
)](https://github.com/findsimilar/find-similar)

<hr>

## Menu

- [Mission](#mission)
- [Open Source Project](#open-source-project)
- [Features](#features)
- [Requirements](#requirements)
- [Development Status](#development-status)
- [Install](#install)
- [Quickstart](#quickstart)
- [Contributing](#contributing)

## Mission

The mission of the **FindSimilar** project is to provide a powerful and versatile open source library that empowers 
developers to efficiently find similar objects and perform comparisons across a variety of data types.
Whether dealing with texts, images, audio, or more, 
our project aims to simplify the process of identifying similarities and enhancing decision-making.

## Open Source Project

This is the open source project with [MIT license](LICENSE). 
Be free to use, fork, clone and contribute.

## Features

Find similar texts
- on different languages
- with or without stopwords
- using dictionary (or not)
- using keywords (or not)

## Requirements

- nltk, pymorphy3
- See more in [Full Documentation](https://findsimilar.craftsman.lol/about.html#requirements)

## Development Status

- Package already available on [PyPi](https://pypi.org/project/find-similar/)
- See more in [Full Documentation](https://findsimilar.craftsman.lol/about.html#development-status)

## Install

### with pip

```commandline
pip install find-similar
```

See more in [Full Documentation](https://findsimilar.craftsman.lol/install.html)

## Quickstart

```python
from find_similar import find_similar

texts = ['one two', 'two three', 'three four']

text_to_compare = 'one four'
find_similar(text_to_compare, texts, count=10)
```

```commandline
[TokenText(text="one two", len(tokens)=2, cos=0.5), TokenText(text="three four", len(tokens)=2, cos=0.5), TokenText(text="two three", len(tokens)=2, cos=0)]
```

- The result is the list of `TokenText` instances ordering by `cos`
- `cos` is the mark of texts similarity

### See more examples in [Full Documentation][documentation_path]

## Contributing

You are welcome! To easy start please check:
- [Full Documentation][documentation_path]
- [Contributing](CONTRIBUTING.md)
- [Developer Documentation](https://findsimilar.craftsman.lol/dev_documentation.html)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Governance](GOVERNANCE.md)
- [Support](SUPPORT.md)

[documentation_path]: https://findsimilar.craftsman.lol