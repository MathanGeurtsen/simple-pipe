# simple-pipe
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)

A Python package that provides a simple typed pipe operator for function composition.

This is a weekend hobby project. If you wish to use a pipe operator in your code, take a look at the [alternatives](#comparison-to-alternatives), or simply check out the extremely short implementation in [pipe.py](src/simple_pipe/pipe.py).

## Usage

`simple-pipe` allows for chaining together typed functions using a pipe operator (`|`). Pipes can be type checked by pyright.

For example, reverse a list and get the length of the last item:
```python
>>> from simple_pipe import Pipe

>>> # Chain multiple functions together
>>> reversed_first = Pipe | list | reversed | iter | next | len

>>> # call the function with input
>>> result = reversed_first(("a", "bb", "ccc"))
>>> assert result == 3

```

Calculate the sum of the squares of the first 10 integers:
```python
>>> from itertools import islice, count
>>> from simple_pipe import Pipe
>>> from simple_pipe import partial2
>>> first_ten_quad = Pipe | count | partial2(map, lambda x: x**int(2)) | partial2(islice, arg2=10) | sum
>>> assert first_ten_quad(0) == 285

```

All of these calls are fully compatible with type checking, but will also function without specific type annotations for example as in the use of the lambdas above.

## Requirements

- Python 3.12+

## Comparison to alternatives

How does this compare to [Pipe](https://github.com/JulienPalard/Pipe)? First off, simple-pipe is just a weekend hobby project whereas Pipe has had a couple of years of development, so in terms of code maturity, there's no comparison. 

The intended use of simple-pipe's `Pipe` is to be a Forward Pipe Operator and nothing more, making no assumptions as to what kind of data passes through. 

Pipe's class `Pipe.Pipe` is specific to generators, so the two work slightly differently in use.

However, since `Pipe.Pipe` exposes its internal function through `.function`, we are actually compatible and can use those same functions in simple-pipe pipes:

```python
from itertools import count
from pipe import select, take
from simple_pipe import Pipe

function_simple_pipe = Pipe | count | select(lambda x: x **2).function | take(10).function | sum

assert function_simple_pipe(0) == 285
```

Note that for  `function_simple_pipe` the definition is completely defined in forward composition: the functions are applied in the order in which you read them. It's also reusable since the pipe defines a function instead of executing directly. 

## Development

For testing and linting, setup the extra dependencies:
```
uv venv
uv sync --extra dev
```

You can check if tests and building work with `poe build`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
