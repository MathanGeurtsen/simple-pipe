from simple_pipe import partial2, partial3, partial4, partial5


def test_partial2() -> None:
    def usetwo(a: int, b: list[float]) -> float:
        return b[a]

    func1 = partial2(usetwo, 1)

    assert func1([6.0, 5.0, 4.0]) == 5.0


def test_partial3() -> None:
    def usethree(a: int, b: str, c: float) -> float:
        return len(b[a:]) / c

    def usethree_(a: int, b: list[int], c: int) -> int:
        return (a + b[0]) // c

    func1 = partial3(usethree, 1, "asdf")
    func2 = partial3(usethree_, arg1=7, arg2=[3])

    assert func1(2.0) == 1.5
    assert func2(3) == 3


def test_partial2_with_strings() -> None:
    def concat(prefix: str, suffix: str) -> str:
        return prefix + suffix

    add_hello = partial2(concat, "Hello, ")
    assert add_hello("World!") == "Hello, World!"


def test_partial3_with_math() -> None:
    def weighted_sum(a: float, b: float, weight: float) -> float:
        return (a + b) * weight

    half_sum = partial3(weighted_sum, 10.0, arg3=0.5)
    assert half_sum(20.0) == 15.0


def test_partial4_with_list_ops() -> None:
    def list_insert(lst: list[int], pos: int, val: int, count: int) -> list[int]:
        return lst[:pos] + [val] * count + lst[pos:]

    insert_zeros = partial4(list_insert, arg2=1, arg3=0, arg4=3)
    assert insert_zeros([1, 2, 3]) == [1, 0, 0, 0, 2, 3]


def test_partial5_with_complex_function() -> None:
    def format_string(
        template: str, name: str, age: int, city: str, country: str
    ) -> str:
        return template.format(name=name, age=age, city=city, country=country)

    template = "{name} is {age} years old and lives in {city}, {country}"
    format_person = partial5(
        format_string, template, arg3=25, arg4="Berlin", arg5="Germany"
    )

    expected = "Alice is 25 years old and lives in Berlin, Germany"
    assert format_person("Alice") == expected
