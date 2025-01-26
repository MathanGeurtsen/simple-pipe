# simple-pipe
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)

A Python package that provides a simple typed pipe operator for function composition.

## Installation

```bash
pip install simple-pipe
```

## Usage

`simple-pipe` allows for chaining together typed functions using a pipe operator (`|`). Pipes can be type checked by pyright.

For example:
```python
from simple_pipe import Pipe

# Chain multiple functions together
pipeline = Pipe | list | reversed | iter | next

# Apply the pipeline to your data
result = pipeline((1, 2, 3))  # Returns 3
```

### How It Works

The pipe operator (`|`) composes functions from left to right. Each function's output becomes the input for the next function in the chain.

```python
# These are equivalent:
result1 = next(iter(reversed(list((1, 2, 3)))))
result2 = (Pipe | list | reversed | iter | next)((1, 2, 3))
```

## Features
- extremely simple implementation
- Simple and intuitive syntax
- Lightweight with no dependencies
- Type-hint friendly
- Works with built-in Python functions and custom callables

## Requirements

- Python 3.12+

## Development

The codebase is laughably tiny: therefore the only dependency is Generics (and Generics syntax from 3.12). 

For testing and linting, setup the extra dependencies:
```
uv venv
uv sync --extra dev
```

You can check if tests and building work with `poe build`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
