# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "NetcdfData Microservice"
copyright = "2023, Marco Antonio Vega Marichalar"
author = "Marco Antonio Vega Marichalar"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "autoapi.extension",
    "sphinx_rtd_theme",
    "myst_nb",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
# html_theme = 'furo'
# html_theme = 'sphinx_book_theme'

html_title = project + " v" + release

# -- Options for autoapi ext -------------------------------------------------

autoapi_modules = {"app/api": None}
autoapi_dirs = ["../app/"]
autoapi_ignore = ["*/test_*.py"]
