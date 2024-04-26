# Exercise 9: My First Package

## Instructions

| Files to turn in | .py, .txt, .toml, README.md, LICENSE |
|-------------------|-----------------------------------------|
| Allowed functions | PyPI or any library for packaging |

Create your first package in python the way you want, it will appear in the list of
installed packages when you type the command "pip list" and display its characteristics when you type "pip show -v ft_package"

```sh
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>

```

The package will be installed via pip using one of the following commands (both
should work):

```sh
pip install ./dist/ft_package-0.0.1.tar.gz
```

```sh
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Your package must be able to be called from a script like this one:

```python
from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

## Definitions

| Term | Definition |
|------|------------|
| PyPI | Python Package Index |
| pip | Python package installer |
| wheel | A package format designed to ship libraries with compiled artifacts |
| Project | A collection of files that make up a package |
| sdist | Source distribution Package, re compressed archives (.tar.gz files) containing one or more packages or modules.|

## Resources

- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Writing PyProject TOML](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Hatch's documentation](https://hatch.pypa.io/latest/)
- [Structuring your Python Project](https://docs.python-guide.org/writing/structure/)
