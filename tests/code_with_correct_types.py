from typing import Callable, Iterator, Protocol, NewType, Sequence

from typing import TypeVar, Union, Any
from dataclasses import dataclass



class Addable(Protocol):
    def __add__(self, other: 'Addable') -> 'Addable': ...

def recursive_sum[T: (Addable, int, float, str)](iter: Iterator[T], acc: T | None = None) -> T:
    try:
        return recursive_sum(acc=next(iter) + acc if acc else next(iter), iter = iter)
    except StopIteration:
        if not acc:
            raise ValueError()
        return acc

assert recursive_sum(iter([1,2,3,4])) == 10















_initial_missing = object()

def reduce_cp(function, sequence, initial=_initial_missing):
    """
    reduce(function, iterable, /[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of an iterable, from left to right.

    This effectively reduces the iterable to a single value.  If initial is present,
    it is placed before the items of the iterable in the calculation, and serves as
    a default when the iterable is empty.

    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
    calculates ((((1 + 2) + 3) + 4) + 5).
    """

    it = iter(sequence)

    if initial is _initial_missing:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError(
                "reduce() of empty iterable with no initial value") from None
    else:
        value = initial

    for element in it:
        value = function(value, element)

    return value

from functools import reduce


@dataclass(frozen=True)
class _InitialMissing:
    pass

def reduce_[T, U](iter: Iterator[T], func: Callable[[T, U | T],U], acc: U | T | _InitialMissing = _InitialMissing()) -> U | T:
    if isinstance(acc, _InitialMissing):
        try:
            new_acc = next(iter)
        except StopIteration:
                raise TypeError(
                    "reduce_() of empty iterable with no initial value") from None
    else:
        try:
            new_value = next(iter)
        except StopIteration:
            return acc
        new_acc = func(new_value, acc)
    return reduce_(iter, func, new_acc)
    

assert reduce_(iter([1,2,3,4]), lambda x,y: x+y) == 10



from simple_pipe import Pipe, partial3, partial2
from simple_pipe.generated.partial import EMPTY
from src.simple_pipe.pipe import _PipeStart

# def SelfPipe(x: _PipeStart) -> _PipeStart:
#     return sum_pipe(x)


# sum_pipe = Pipe | SelfPipe


sum_pipe_imp = Pipe | sum
print((sum_pipe_imp([1,2,3,4]), 10))

sum_pipe_reduce = Pipe | partial3(reduce_, EMPTY, lambda x,y:x+y, None, arg1=asdf)
print((sum_pipe_reduce(iter([1,2,3,4])), 10))
