from __future__ import annotations
from collections.abc import Callable
from typing import TypeVar, Generic


T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")


class _PipeStart:
    """Helper class defining the start of a pipe.

    This allows the syntax to start simply with an object instead of a function call.
    """

    def __init__(self) -> None:
        pass

    def __or__(self, func: Callable[[T], U]) -> _Pipe[T, U]:
        return _Pipe(func)


class _Pipe(Generic[T, U]):
    """Actual pipe implementation.

    Pipes are composed by the use of the  `|` operator,
    chaining functions together to produce a single function.
    """

    def __init__(self, func: Callable[[T], U]) -> None:
        self.func = func

    def __or__(self, func: Callable[[U], V]) -> _Pipe[T, V]:
        return _Pipe(lambda x: func(self.func(x)))

    def __call__(self, x: T) -> U:
        return self.func(x)


Pipe = _PipeStart()
