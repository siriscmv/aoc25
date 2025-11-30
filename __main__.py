import os
import sys
import time
from importlib import import_module
from dotenv import load_dotenv
import pyaoc.commands as aoc

load_dotenv()
aoc.set_session(os.environ.get("SESSION_TOKEN"))


def pad(n: str) -> str:
    return f"{int(n):02}"


# Get command-line arguments
args = sys.argv[1:]

if len(args) < 2:
    print("Usage: python3 . <day> <part>")
    sys.exit(1)

day = int(args[0])
day_padded = pad(args[0])

try:
    part = int(args[1])
except ValueError:
    print("Part must be 1 or 2")
    sys.exit(1)

if part not in [1, 2]:
    print("Part must be 1 or 2")
    sys.exit(1)

# Read input data
input_data = aoc.get_day_input(day=day, year=2025)

# Import solution module
try:
    runner = import_module(f"solutions.d{day_padded}")
except ModuleNotFoundError:
    print(f"Solution module solutions.d{day_padded} not found")
    sys.exit(1)

# Parse input if parser is defined
if hasattr(runner, "parser"):
    input_data = runner.parser(input_data)

# Run the selected part
start = time.perf_counter()
if part == 1:
    output = runner.p1(input_data)
else:
    output = runner.p2(input_data)
end = time.perf_counter()

print(output, f"in {(end - start) * 1000:.2f} ms")
