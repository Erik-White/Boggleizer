import io
import re
from pathlib import Path
from setuptools import setup, find_namespace_packages


def read(*names, **kwargs):
    with io.open(
        Path.joinpath(Path(__file__).parent, *names),
        encoding = kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


# Combine the readme and changelog to form the long_description
long_description = "%s\n%s" % (
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub("", read("README.md")),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.md"))
    )


setup(
    python_requires = ">=3.8",
    name = "boggleizer",
    version = "0.1.0",
    description = "A Boggle puzzle image recognition solver",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Erik-White/Boggleizer/",
    author = "Erik White",
    author_email = "",
    license = "GPL-3.0",
    packages = find_namespace_packages(where = "src", exclude = ["tests", "tests.*"]),
    package_dir = {"": "src"},
    zip_safe = False,
    install_requires = [
        "marisa-trie"
        "numpy",
        "matplotlib",
        "scikit-image"
    ],
    extras_require = {
        "dev": [
            "flake8",
            "black",
            "check-manifest",
            "pytest",
            "pytest-cov"
        ],
        "test": [
            "flake8",
            "black",
            "pytest",
            "pytest-cov"
        ],
    },
    entry_points={
        'console_scripts': [
            'boggleizer = boggleizer.main:main',
        ],
    },
)