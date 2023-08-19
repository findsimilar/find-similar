import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


setup(
    name='find-similar',
    version='1.0',
    packages=['find_similar'],
    include_package_data=True,
    license='MIT',
    description='Algorithm to define similarity rating between objects',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/findsimilar/find-similar',
    author='findsimilar',
    author_email='help@findsimilar.org',
    keywords=['rating', 'similarity', 'tokens'],
    install_requires=[
        'pymorphy2==0.9.1',
        'pymorphy2-dicts-ru==2.4.417127.4579844',
        'nltk==3.8.1',
        'pydantic==1.10.7'
    ],
    python_requires='>=3',
)


