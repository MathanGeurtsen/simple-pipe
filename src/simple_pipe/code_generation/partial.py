from itertools import combinations
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

CODE_GENERATION_DIR = Path("src") / "simple_pipe" / "code_generation"
CODE_GENERATION_OUTPUT_DIR = Path("src") / "simple_pipe" / "generated"


def function_args(combo, num_args: int):
    """Generate the function arguments string."""
    args = []
    for i in range(1, num_args + 1):
        if i in combo:
            args.append(f"arg{i}")
        else:
            args.append("free_arg")
    return ", ".join(args)


def generate_partial4num(num_args: int) -> str:
    """Generate an iteration of `partial<n>` up to `n` arguments."""
    partial_function_file = CODE_GENERATION_DIR / "partial.py.jinja2"

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(str(partial_function_file))

    # Generate all possible argument combinations
    combos = list(combinations(range(1, num_args + 1), num_args - 1))

    rendered = template.render(
        num_args=num_args, combinations=combos, function_args=function_args
    )

    return rendered


def generate_partial():
    """Generate the `partial.py` file."""
    header_file = CODE_GENERATION_DIR / "partial_header.py.jinja2"
    partial = header_file.read_text()
    partial += generate_partial4num(2)
    partial += generate_partial4num(3)
    partial += generate_partial4num(4)
    partial += generate_partial4num(5)

    output_path = CODE_GENERATION_OUTPUT_DIR / "partial.py"
    output_path.write_text(partial)


if __name__ == "__main__":
    generate_partial()
