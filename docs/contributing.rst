Contributing
============

This page describes how to set up a local development environment.

Prerequisites
-------------

- Python 3.10 or later
- Git
- ``make``

Getting started
---------------

Clone the repository:

.. code-block:: bash

    git clone https://github.com/niccokunzmann/sphinx-icalendar-extension.git
    cd sphinx-icalendar-extension

Create a virtual environment and install the package with its development
dependencies in editable mode:

.. code-block:: bash

    make venv

This runs ``python3 -m venv .venv`` and then ``pip install -e ".[dev]"``,
which installs ``pytest``, ``sphinx``, and ``sphinx-autobuild`` alongside the
extension itself.

Building the docs
-----------------

Build the HTML documentation once:

.. code-block:: bash

    make html

The output is written to ``docs/_build/html/``.  Open
``docs/_build/html/index.html`` in a browser to review the result.

For a live-reloading preview while editing:

.. code-block:: bash

    make livehtml

Running the tests
-----------------

.. code-block:: bash

    make test

Cleaning up
-----------

Remove the built docs:

.. code-block:: bash

    make clean

Remove the virtual environment as well:

.. code-block:: bash

    make clean-all
