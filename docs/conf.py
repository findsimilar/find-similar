"""
Configuration file for the Sphinx documentation builder.
"""
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from find_similar.package import name, version, status  # pylint: disable=wrong-import-position

project = name  # pylint: disable=invalid-name
author = 'findsimilar'  # pylint: disable=invalid-name
copyright = f'2023, {author}'  # pylint: disable=redefined-builtin
release = version  # pylint: disable=invalid-name

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # pylint: disable=invalid-name
html_static_path = ['_static']

rst_prolog = f"""
.. |development_status| replace:: {status}
.. |project_name| replace:: {project}
"""
