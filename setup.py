from __future__ import absolute_import
from setuptools import setup, find_packages
from pkg_resources import parse_version

setup(
    name = "setuptools-zip_safe-ignored",
#    version_command = ("git describe --tags", "pep440-git-local"),
#    setup_requires = ["setuptools-version-command"],
    zip_safe = True,
    packages = find_packages(),
)
