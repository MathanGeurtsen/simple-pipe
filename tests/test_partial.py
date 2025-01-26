from simple_pipe.generated.partial import partial2, partial3


def test_partial2():
    def usetwo(a: int, b: list[float]):
        return b[a]

    func1 = partial2(usetwo, 1)

    assert func1([6, 5, 4]) == 5


def test_partial3():
    def usethree(a: int, b: str, c: float) -> float:
        return len(b[a:]) / c

    def usethree_(a: int, b: list[int], c: int) -> int:
        return (a + b[0]) // c

    func1 = partial3(usethree, 1, "asdf")
    func2 = partial3(usethree_, arg1=7, arg2=[3])

    assert func1(2.0) == 1.5
    assert func2(3) == 3
