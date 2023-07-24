import pathlib
import sys
from datetime import datetime

import ophyd
import ophyd.docs
import sphinx_rtd_theme

module_path = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(module_path))

import hxrsnd  # noqa: E402 F401

project = "HXRSnD"
author = "SLAC National Accelerator Laboratory"

copyright = f"{datetime.now().year}, {author}"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = ""

# -- General configuration ---------------------------------------------------
needs_sphinx = "3.2.1"

extensions = [
    "sphinxcontrib.jquery",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "numpydoc",
    # 'docs-versions-menu',
    "sphinx_rtd_theme",
]

templates_path = [ophyd.docs.templates.PATH]

source_suffix = ".rst"
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "python"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# html_theme_options = {}
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
# html_sidebars = {}

# -- Options for HTMLHelp output ---------------------------------------------
htmlhelp_basename = project

# -- Extension configuration -------------------------------------------------
autodoc_default_options = {
    "members": "",
    "member-order": "bysource",
    "special-members": "",
    "undoc-members": False,
    "exclude-members": "",
}

intersphinx_mapping = {
    "ophyd": ("https://blueskyproject.io/ophyd", None),
    "python": ("https://docs.python.org/3", None),
    # 'numpy': ('https://docs.scipy.org/doc/numpy', None),
    "caproto": ("https://caproto.github.io/caproto/master", None),
}

autosummary_generate = True

# Duplicate attributes will be generated without this:
autoclass_content = "init"

# Tons of warnings will be emitted without this:
numpydoc_show_class_members = False
autosummary_context = {
    **ophyd.docs.autosummary_context,
    "project_root": "..",
}
html_context = {
    **autosummary_context,
    # 'css_files': [
    #     '_static/theme_overrides.css',  # override wide tables in RTD theme
    # ],
}


def setup(app):
    # Add your own setup here
    ophyd.docs.setup(app)
