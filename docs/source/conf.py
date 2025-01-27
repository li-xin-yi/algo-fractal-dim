# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Algo Fractal Dim'
copyright = '2025, Xinyi Li'
author = 'Xinyi Li'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_static_path = ['_static']


extensions = [
    # "myst_nb",
    # or "myst_parser" if you're just using MyST Markdown (no notebooks)
    "sphinx_math_dollar", 
    "myst_parser", # Optional if you want $...$ style math
]

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown',
# }