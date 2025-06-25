"""This file is used to configure the Sphinx build of our documentation.
The documentation on setting this up is here: https://www.sphinx-doc.org/en/master/usage/configuration.html 
"""

# This is the standard readthedocs theme.
import sphinx_rtd_theme
import sys, os

sys.path.insert(0, os.path.abspath("extensions"))

# What Sphinx extensions do we need
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.imgmath",
    "sphinx.ext.ifconfig",
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    "nbsphinx",
]


html_theme = "sphinx_rtd_theme"
nbsphinx_execute = 'never'

html_static_path = ["_static"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Praktikumsaufgaben'
copyright = u'2019, Fabian Senf'
author = u'Fabian Senf'


version = u'0.1'
# The full version, including alpha/beta/rc tags.
release = u'0.1'


pygments_style = "sphinx"

