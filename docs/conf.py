import sphinx_icalendar

project = "sphinx-icalendar"
author = "sphinx-icalendar contributors"
release = sphinx_icalendar.__version__

extensions = [
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_icalendar",
    "sphinx_issues",
]

html_theme = "alabaster"

html_theme_options = {
    "description": "Render iCalendar events directly in your Sphinx docs.",
    "github_user": "pycalendar",
    "github_repo": "sphinx-icalendar",
}

html_context = {
    #     "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": html_theme_options["github_user"],
    "github_repo": html_theme_options["github_repo"],
    "github_version": "main",
    "doc_path": "docs",
}


source_suffix = {".rst": "restructuredtext"}

# -- sphinx_copybutton configuration ----------------------------------
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html
# Exclude line numbers, prompts, and console output when copying code blocks.
copybutton_exclude = ".linenos, .gp, .go"


# -- sphinx_issues configuration ----------------------------------
issues_github_path = "pycalendar/sphinx-icalendar"

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/pycalendar/sphinx-icalendar",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
            "attributes": {
                "target": "_blank",
                "rel": "noopener me",
                "class": "nav-link custom-fancy-css",
            },
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/sphinx-icalendar",
            "icon": "fa-custom fa-pypi",
            "type": "fontawesome",
            "attributes": {
                "target": "_blank",
                "rel": "noopener me",
                "class": "nav-link custom-fancy-css",
            },
        },
    ],
    "use_edit_page_button": True,
}

html_theme = "pydata_sphinx_theme"
html_static_path = [
    "_static",
]
html_js_files = [
    ("js/custom-icons.js", {"defer": "defer"}),
]
pygments_style = "sphinx"
