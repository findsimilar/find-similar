# FindSimilar

Mission Statement
-----------------

The mission of the "Find Similar" project is to provide a powerful and versatile open source library that empowers developers to efficiently find similar objects and perform comparisons across a variety of data types. Whether dealing with texts, images, audio, or more, our project aims to simplify the process of identifying similarities and enhancing decision-making.

Key Objectives
---------------
1. **Extensibility:** We strive to build a flexible framework that goes beyond textual comparisons, with plans to expand compatibility to various data formats, including images, audio, and more.
2. **Ease of Integration:** Our library will offer an intuitive interface that integrates seamlessly into existing applications and workflows, making it accessible to developers regardless of their experience level.
3. **Scalability:** Our focus is on creating efficient algorithms and data structures that can handle datasets of varying sizes, ensuring performance and accuracy as the project scales.
4. **Community Collaboration:** By embracing the principles of open source development, we invite a diverse community of contributors to collaborate, improve, and innovate upon the project, fostering a culture of shared knowledge and expertise.
5. **Documentation and Education:** We are committed to providing comprehensive documentation, tutorials, and resources to help users and contributors understand the library's capabilities and use them effectively.
6. **Privacy and Ethics:** As we expand into various data types, we are dedicated to upholding privacy and ethical considerations, ensuring that our library is built and used responsibly.

Join Us
--------

We invite developers, data scientists, and enthusiasts from all backgrounds to join our mission. Together, we can shape the future of "Find Similar," creating a powerful tool that enhances decision-making, discovery, and innovation across diverse fields.

Get Started
-----------

Explore our GitHub repository, engage with the community on our forums, and join us in building a more connected and informed world through the "Find Similar" project.

Installation:
-------------

```bash
git clone https://github.com/findsimilar/find-similar
pip3 install wheel
python text-finder/setup.py bdist_wheel
pip3 install text-finder/dist/*
```

Usage example:
------

```python
from algorithm import find_similar, TokenText, get_tokens

texts = ['one two', 'two three', 'three four']
texts_with_tokens = []
for text in texts:
    tokens = get_tokens(text)
    text_token = TokenText(text, tokens)
    texts_with_tokens.append(text_token)

text_to_compare = 'one four'
result = find_similar(texts_with_tokens, texts, count=10)
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

Development
--------
* algorithm - this is the main package to install and use
* analytics - help functions to improve the main algorithm
* lab - python scripts to research

Lab
---
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
