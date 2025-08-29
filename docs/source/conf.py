# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Mantys Healthcare System API'
copyright = '2025, Mantys'
author = 'Mantys'

release = '1.0'
version = '1.0.0'

# -- Project metadata
html_title = 'Mantys Healthcare System API Documentation'
html_short_title = 'Mantys API Docs'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'display_version': True,
}

# Add any paths that contain custom static files (such as style sheets)
html_static_path = ['_static']

# Custom CSS files
html_css_files = []

# HTML context variables
html_context = {
    'display_github': False,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
