[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Advent of Code 2023

##### Notes for self

Start new projects using `poetry` with the `--src` option

```
> poetry new --src my_package
```

Use groups

```
> poetry add ipython --group dev
> poetry add pytest --group tests
```

Make the `dev` group optional

```
[tool.poetry.group.dev]
optional = true
```
