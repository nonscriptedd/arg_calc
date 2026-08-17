import argparse
from math import sqrt, prod
from functools import reduce
from statistics import multimode
from operator import sub, truediv
from rich import print as rprint

def calculate_power_tower(numbers: list[float]) -> float | int:
    return reduce(lambda x, y: y ** x, reversed(numbers))

parser = argparse.ArgumentParser(description="A simple calculator that works with command line arguments.")

parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide", "sqrt", "exponent", "mean", "median", "mode"], help="The operation to apply to the numbers.")
parser.add_argument(
    "numbers",
    type=int,
    nargs="+",
    help="The numbers to use when calculating.",
)

args = parser.parse_args()

match args.operation:
    case "add":
        rprint(f"{" + ".join(map(str, args.numbers))} = [#FFA500 bold]{sum(args.numbers)}[/]")
    case "subtract":
        rprint(f"{" - ".join(map(str, args.numbers))} = [#FFA500 bold]{reduce(sub, args.numbers)}[/]")
    case "multiply":
        rprint(f"{" * ".join(map(str, args.numbers))} = [#FFA500 bold]{prod(args.numbers)}[/]")
    case "divide":
        try:
            rprint(f"{" / ".join(map(str, args.numbers))} = [#FFA500 bold]{reduce(truediv, args.numbers)}[/]")
        except ZeroDivisionError:
            rprint("[red bold]Division by 0!!![/]")
    case "sqrt":
        for i in args.numbers:
            rprint(f"√{i} = [#FFA500 bold]{sqrt(i)}[/]")
    case "exponent":
        rprint(f"{" ^ ".join(str(x) for x in args.numbers)} = [#FFA500 bold]{calculate_power_tower(args.numbers)}[/]")
    case "mean":
        rprint(f"The mean of {args.numbers} = [#FFA500 bold]{sum(args.numbers) / 4}[/]")
    case "median":
        numbers = sorted(args.numbers)
        mid = len(numbers) // 2

        if len(numbers) % 2 == 0:
            result = (numbers[mid - 1] + numbers[mid]) / 2
        else:
            result = numbers[mid]
        rprint(f"The median of {args.numbers} = [#FFA500 bold]{result}[/]")
    case "mode":
        modes = multimode(args.numbers)
        unique_count = len(set(args.numbers))
        total_count = len(args.numbers)

        if len(modes) == unique_count and unique_count > 1:
            rprint(f"The dataset of {args.numbers} has [#FFA500 bold i]no mode[/].")
        elif len(modes) > 1:
            formatted_modes = ", ".join(str(x) for x in modes)
            rprint(f"The dataset of {args.numbers} has the modes of [#FFA500 bold]{formatted_modes}[/].")
        else:
            rprint(f"The mode of {args.numbers} is [#FFA500 bold]{modes[0]}[/].")
