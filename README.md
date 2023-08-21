# FindSimilar

[findsimilar.org][homepage]

> User-friendly library to find similar objects

* [Mission Statement][mission_statement]
* [Open Source Collaboration][open_source_collaboration]
* [Installation][installation]
* [Usage][usage]
* [Development][development]

## Mission Statement

The mission of the "Find Similar" project is to provide a powerful and versatile open source library that empowers developers to efficiently find similar objects and perform comparisons across a variety of data types. Whether dealing with texts, images, audio, or more, our project aims to simplify the process of identifying similarities and enhancing decision-making.

### Key Objectives

1. **Extensibility:** We strive to build a flexible framework that goes beyond textual comparisons, with plans to expand compatibility to various data formats, including images, audio, and more.
2. **Ease of Integration:** Our library will offer an intuitive interface that integrates seamlessly into existing applications and workflows, making it accessible to developers regardless of their experience level.
3. **Scalability:** Our focus is on creating efficient algorithms and data structures that can handle datasets of varying sizes, ensuring performance and accuracy as the project scales.
4. **Community Collaboration:** By embracing the principles of open source development, we invite a diverse community of contributors to collaborate, improve, and innovate upon the project, fostering a culture of shared knowledge and expertise.
5. **Documentation and Education:** We are committed to providing comprehensive documentation, tutorials, and resources to help users and contributors understand the library's capabilities and use them effectively.
6. **Privacy and Ethics:** As we expand into various data types, we are dedicated to upholding privacy and ethical considerations, ensuring that our library is built and used responsibly.

### Join Us

We invite developers, data scientists, and enthusiasts from all backgrounds to join our mission. Together, we can shape the future of "Find Similar," creating a powerful tool that enhances decision-making, discovery, and innovation across diverse fields.

## Open Source Collaboration

"Find Similar" is an open source project, fostering collaboration and innovation. We welcome contributors from all backgrounds to join us in shaping the future of similarity comparisons across various data types.

## Installation:

### From PyPi

```bash
pip install find-similar
```

You install core package from pypi. If you want to use tests and laboratory you can install find-similar from python package

### From python package

```bash
git clone https://github.com/findsimilar/find-similar
pip3 install wheel
python find-similar/setup.py bdist_wheel
pip3 install find-similar/dist/*
```

## Usage example:

### Simple usage

```python
from find_similar import find_similar

texts = ['one two', 'two three', 'three four']

text_to_compare = 'one four'
result = find_similar(text_to_compare, texts, count=10)
for item in result:
    print(item.text)
    print(item.cos)
```

expected result:
```
one two
0.5
three four
0.5
two three
0.0
```

## Development

* find_similar - this is the main package to install and use
* analytics - help functions to improve the main algorithm
* lab - python scripts to research

### Lab

You can run any useful script from lab package
```bash
cd lab
```
* Use load_data_from_file.py to load test data
```bash
python load_data_from_file.py /my/path/to/file.xlsx
```
* Use check_total_rating.py to analyze algorithm accuracy
```bash
python check_total_rating.py
```
Example result:
```
Поиск выполнен для 529 позиций:
топ 1 -- 353 (66.73 %)
топ 5 -- 442 (83.55 %)
топ 10 -- 468 (88.47 %)
топ 25 -- 501 (94.71 %)
топ 50 -- 515 (97.35 %)
топ 100 -- 519 (98.11 %)
топ 500 -- 523 (98.87 %)
топ 1000 -- 529 (100.0 %)
топ 2000 -- 529 (100.0 %)
```

* Use check_time_one_item to check how long time algorithm works for one item
```bash
python check_time_one_item.py
```
Example result:
```
Load base items...
1999 items loaded
RESULT TIME FOR ONE ITEM (REPEAT 1 times) = 0.03772415800085582
```

* Use compare_two to compare two different texts. You can change texts in compare_two.txt file
```bash
python compare_two.py
```

* Use tokenize_one to check how one text will be tokenized. You can set the text in tokenize_one.txt file
```bash
python tokenize_one.py
```

[mission_statement]: https://github.com/findsimilar/find-similar#mission-statement
[open_source_collaboration]: https://github.com/findsimilar/find-similar#open-source-collaboration
[installation]: https://github.com/findsimilar/find-similar#installation
[usage]: https://github.com/findsimilar/find-similar#usage-example
[development]: https://github.com/findsimilar/find-similar#development
[homepage]: https://findsimilar.org