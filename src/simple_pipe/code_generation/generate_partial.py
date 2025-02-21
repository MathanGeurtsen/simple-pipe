from itertools import combinations
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

CODE_GENERATION_DIR = Path("src") / "simple_pipe" / "code_generation"
CODE_GENERATION_OUTPUT_DIR = Path("src") / "simple_pipe" / "generated"


def function_args(combo: tuple[int], num_args: int) -> str:
    """Generate the function arguments string."""
    args: list[str] = []
    for i in range(1, num_args + 1):
        if i in combo:
            args.append(f"arg{i}")
        else:
            args.append("free_arg")
    return ", ".join(args)


def generate_partial4num(num_args: int) -> str:
    """Generate code for partial function with specified number of arguments."""
    template_path = CODE_GENERATION_DIR / "partial.py.jinja2"

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(str(template_path))

    # Generate all possible argument combinations
    combos = list(combinations(range(1, num_args + 1), num_args - 1))

    rendered = template.render(
        num_args=num_args,
        combinations=combos,
        function_args=function_args,
    )

    return rendered


def generate_partial() -> None:
    """Generate the `partial.py` file with all required functions."""
    header_content = (CODE_GENERATION_DIR / "partial_header.py.jinja2").read_text()

    partial_code = (
        header_content
        + generate_partial4num(2)
        + generate_partial4num(3)
        + generate_partial4num(4)
        + generate_partial4num(5)
    )

    output_path = CODE_GENERATION_OUTPUT_DIR / "partial.py"
    output_path.write_text(partial_code)


if __name__ == "__main__":
    generate_partial()
