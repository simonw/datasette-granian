# datasette-granian

[![PyPI](https://img.shields.io/pypi/v/datasette-granian.svg)](https://pypi.org/project/datasette-granian/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-granian?include_prereleases&label=changelog)](https://github.com/simonw/datasette-granian/releases)
[![Tests](https://github.com/simonw/datasette-granian/workflows/Test/badge.svg)](https://github.com/simonw/datasette-granian/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-granian/blob/main/LICENSE)

Run Datasette using the Granian HTTP server

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-granian

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-granian
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
