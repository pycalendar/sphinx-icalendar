Contributing
============

Please report all issues on `GitHub <https://github.com/pycalendar/sphinx-icalendar/issues>`__.

This page describes how to set up a local development environment.

Prerequisites
-------------

- Python 3.10 or later
- Git
- ``make``
- `pre-commit <https://pre-commit.com/#install>`_

Getting started
---------------

Clone the repository:

.. code-block:: bash

    git clone https://github.com/pycalendar/sphinx-icalendar.git
    cd sphinx-icalendar

Create a virtual environment and install the package with its development
dependencies in editable mode:

.. code-block:: bash

    make venv

This runs ``python3 -m venv .venv`` and then ``pip install -e ".[dev]"``,
which installs ``pytest``, ``sphinx``, and ``sphinx-autobuild`` alongside the
extension itself.

Install the pre-commit hooks so they run automatically on every commit:

.. code-block:: bash

    pre-commit install

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

New release
-----------

Before the release, check the documentation and that it renders properly.

To create a new release, run:

.. code-block:: bash

    git checkout main
    git tag v0.1.1
    git push origin v0.1.1

Notes on documentation
----------------------

- Use "iCalendar" when describing a file format that follows that standard.
- Use "jCal" when describing a file format that follows that standard.
- Use ".ics" or ".ifb" when describing a file's extension. See :rfc:`5545#section-8.1`.
- Don't use "ICS" anywhere, including the tabbed interface. It's not used as an acronym in RFC 5545. Use "iCalendar" instead.

.. seealso::
    :issue:`3`
