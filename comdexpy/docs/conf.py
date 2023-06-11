# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

import sphinx_rtd_theme


# -- Project information -----------------------------------------------------


project = 'comdexpy'
copyright = '2023, Comdex'
author = 'Comdex'
release = '0.0.1'

# -- General configuration ---------------------------------------------------


extensions = ['sphinx.ext.autodoc','sphinx.ext.coverage','sphinx.ext.todo','sphinx.ext.viewcode','sphinx_rtd_theme',]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
