from typing import TypeVar, Callable, Any, overload

A1 = TypeVar('A1')
A2 = TypeVar('A2')
A3 = TypeVar('A3')
A4 = TypeVar('A4')
A5 = TypeVar('A5')

R = TypeVar('R')

EMPTY = object()


@overload
def partial2(func: Callable[[A1, A2], R],
    arg1: Any = EMPTY,
    arg2: A2 = None) -> Callable[[A1], R]: ...


@overload
def partial2(func: Callable[[A1, A2], R],
    arg1: A1 = None,
    arg2: Any = EMPTY) -> Callable[[A2], R]: ...



def partial2( # pyright: ignore [reportInconsistentOverload]
    func: Callable[[A1,A2], R],
    arg1=EMPTY,
    arg2=EMPTY):
    """
    Partially apply a function.

    Takes in a function and all but one of its arguments to bind to the function.
    Returns a function with a single free argument.
    """
    if (arg1 is not EMPTY):
        return lambda free_arg: func(arg1, free_arg)  # pyright: ignore [reportArgumentType]

    if (arg2 is not EMPTY):
        return lambda free_arg: func(free_arg, arg2)  # pyright: ignore [reportArgumentType]

    raise ValueError("Couldn't bind provided function to provided arguments.")


@overload
def partial3(func: Callable[[A1, A2, A3], R],
    arg1: Any = EMPTY,
    arg2: A2 = None,
    arg3: A3 = None) -> Callable[[A1], R]: ...


@overload
def partial3(func: Callable[[A1, A2, A3], R],
    arg1: A1 = None,
    arg2: Any = EMPTY,
    arg3: A3 = None) -> Callable[[A2], R]: ...


@overload
def partial3(func: Callable[[A1, A2, A3], R],
    arg1: A1 = None,
    arg2: A2 = None,
    arg3: Any = EMPTY) -> Callable[[A3], R]: ...



def partial3( # pyright: ignore [reportInconsistentOverload]
    func: Callable[[A1,A2,A3], R],
    arg1=EMPTY,
    arg2=EMPTY,
    arg3=EMPTY):
    """
    Partially apply a function.

    Takes in a function and all but one of its arguments to bind to the function.
    Returns a function with a single free argument.
    """
    if (arg1 is not EMPTY
        and arg2 is not EMPTY):
        return lambda free_arg: func(arg1, arg2, free_arg)  # pyright: ignore [reportArgumentType]

    if (arg1 is not EMPTY
        and arg3 is not EMPTY):
        return lambda free_arg: func(arg1, free_arg, arg3)  # pyright: ignore [reportArgumentType]

    if (arg2 is not EMPTY
        and arg3 is not EMPTY):
        return lambda free_arg: func(free_arg, arg2, arg3)  # pyright: ignore [reportArgumentType]

    raise ValueError("Couldn't bind provided function to provided arguments.")


@overload
def partial4(func: Callable[[A1, A2, A3, A4], R],
    arg1: Any = EMPTY,
    arg2: A2 = None,
    arg3: A3 = None,
    arg4: A4 = None) -> Callable[[A1], R]: ...


@overload
def partial4(func: Callable[[A1, A2, A3, A4], R],
    arg1: A1 = None,
    arg2: Any = EMPTY,
    arg3: A3 = None,
    arg4: A4 = None) -> Callable[[A2], R]: ...


@overload
def partial4(func: Callable[[A1, A2, A3, A4], R],
    arg1: A1 = None,
    arg2: A2 = None,
    arg3: Any = EMPTY,
    arg4: A4 = None) -> Callable[[A3], R]: ...


@overload
def partial4(func: Callable[[A1, A2, A3, A4], R],
    arg1: A1 = None,
    arg2: A2 = None,
    arg3: A3 = None,
    arg4: Any = EMPTY) -> Callable[[A4], R]: ...



def partial4( # pyright: ignore [reportInconsistentOverload]
    func: Callable[[A1,A2,A3,A4], R],
    arg1=EMPTY,
    arg2=EMPTY,
    arg3=EMPTY,
    arg4=EMPTY):
    """
    Partially apply a function.

    Takes in a function and all but one of its arguments to bind to the function.
    Returns a function with a single free argument.
    """
    if (arg1 is not EMPTY
        and arg2 is not EMPTY
        and arg3 is not EMPTY):
        return lambda free_arg: func(arg1, arg2, arg3, free_arg)  # pyright: ignore [reportArgumentType]

    if (arg1 is not EMPTY
        and arg2 is not EMPTY
        and arg4 is not EMPTY):
        return lambda free_arg: func(arg1, arg2, free_arg, arg4)  # pyright: ignore [reportArgumentType]

    if (arg1 is not EMPTY
        and arg3 is not EMPTY
        and arg4 is not EMPTY):
        return lambda free_arg: func(arg1, free_arg, arg3, arg4)  # pyright: ignore [reportArgumentType]

    if (arg2 is not EMPTY
        and arg3 is not EMPTY
        and arg4 is not EMPTY):
        return lambda free_arg: func(free_arg, arg2, arg3, arg4)  # pyright: ignore [reportArgumentType]

    raise ValueError("Couldn't bind provided function to provided arguments.")


@overload
def partial5(func: Callable[[A1, A2, A3, A4, A5], R],
    arg1: Any = EMPTY,
    arg2: A2 = None,
    arg3: A3 = None,
    arg4: A4 = None,
    arg5: A5 = None) -> Callable[[A1], R]: ...


@overload
def partial5(func: Callable[[A1, A2, A3, A4, A5], R],
    arg1: A1 = None,
    arg2: Any = EMPTY,
    arg3: A3 = None,
    arg4: A4 = None,
    arg5: A5 = None) -> Callable[[A2], R]: ...


@overload
def partial5(func: Callable[[A1, A2, A3, A4, A5], R],
    arg1: A1 = None,
    arg2: A2 = None,
    arg3: Any = EMPTY,
    arg4: A4 = None,
    arg5: A5 = None) -> Callable[[A3], R]: ...


@overload
def partial5(func: Callable[[A1, A2, A3, A4, A5], R],
    arg1: A1 = None,
    arg2: A2 = None,
    arg3: A3 = None,
    arg4: Any = EMPTY,
    arg5: A5 = None) -> Callable[[A4], R]: ...


@overload
def partial5(func: Callable[[A1, A2, A3, A4, A5], R],
    arg1: A1 = None,
    arg2: A2 = None,
    arg3: A3 = None,
    arg4: A4 = None,
    arg5: Any = EMPTY) -> Callable[[A5], R]: ...



def partial5( # pyright: ignore [reportInconsistentOverload]
    func: Callable[[A1,A2,A3,A4,A5], R],
    arg1=EMPTY,
    arg2=EMPTY,
    arg3=EMPTY,
    arg4=EMPTY,
    arg5=EMPTY):
    """
    Partially apply a function.

    Takes in a function and all but one of its arguments to bind to the function.
    Returns a function with a single free argument.
    """
    if (arg1 is not EMPTY
        and arg2 is not EMPTY
        and arg3 is not EMPTY
        and arg4 is not EMPTY):
        return lambda free_arg: func(arg1, arg2, arg3, arg4, free_arg)  # pyright: ignore [reportArgumentType]

    if (arg1 is not EMPTY
        and arg2 is not EMPTY
        and arg3 is not EMPTY
        and arg5 is not EMPTY):
        return lambda free_arg: func(arg1, arg2, arg3, free_arg, arg5)  # pyright: ignore [reportArgumentType]

    if (arg1 is not EMPTY
        and arg2 is not EMPTY
        and arg4 is not EMPTY
        and arg5 is not EMPTY):
        return lambda free_arg: func(arg1, arg2, free_arg, arg4, arg5)  # pyright: ignore [reportArgumentType]

    if (arg1 is not EMPTY
        and arg3 is not EMPTY
        and arg4 is not EMPTY
        and arg5 is not EMPTY):
        return lambda free_arg: func(arg1, free_arg, arg3, arg4, arg5)  # pyright: ignore [reportArgumentType]

    if (arg2 is not EMPTY
        and arg3 is not EMPTY
        and arg4 is not EMPTY
        and arg5 is not EMPTY):
        return lambda free_arg: func(free_arg, arg2, arg3, arg4, arg5)  # pyright: ignore [reportArgumentType]

    raise ValueError("Couldn't bind provided function to provided arguments.")
