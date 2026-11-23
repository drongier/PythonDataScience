# ft_package

A sample package that counts the number of occurrences of a value in a list.

## Build

```bash
python -m build
```

## Installation

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

or

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```
