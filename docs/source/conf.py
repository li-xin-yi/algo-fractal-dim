# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Algorithmic Fractal Dimensions Lecture Notes'
copyright = '2025, Xinyi Li'
author = 'Xinyi Li'
html_title = "Algorithmic Fractal Dimensions"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = [
    "custom.css",  # Our new CSS file
]


extensions = [
    'sphinx.ext.mathjax',
    # "myst_nb",
    # or "myst_parser" if you're just using MyST Markdown (no notebooks)
    "myst_parser", # Optional if you want $...$ style math
    "sphinx_design",
]

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown',
# }

myst_enable_extensions = ["linkify", "dollarmath", "amsmath", "colon_fence"]