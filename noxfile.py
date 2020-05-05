"""Nox sessions."""
import tempfile
from typing import Any

import nox
from nox.sessions import Session


package = "pyproject_cookiecutter_test"
nox.options.sessions = "tests", "safety", "coverage"
locations = "src", "tests"


@nox.session(python="3.7")
def tests(session: Session) -> None:
    """Run the test suite."""
    session.run("make", "install", external=True)
    session.run("make", "tests", external=True)


@nox.session(python="3.7")
def safety(session: Session) -> None:
    """Run the test suite."""
    session.run("make", "install", external=True)
    session.run("make", "safety", external=True)


@nox.session(python="3.7")
def coverage(session: Session) -> None:
    """Run the test suite."""
    session.run("make", "install", external=True)
    session.run("make", "coverage", external=True)
