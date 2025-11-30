# Advent of Code 2025

- List of problems can be found [here](https://adventofcode.com/2025/)

## File structure

- `run.py` - main file that runs the solution
- `solutions/d*.py` - solutions for each day

## Setup

- Create a virtual environment: `python3 -m venv .venv`
- Activate the virtual environment: `source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Create a `.env` file in the root directory and add your session token:

  ```bash
  SESSION_TOKEN="your_session_token_here"
  ```

## Solutions

- Each solution exports `p1` and `p2` functions that take the input data and return the solution
- Solutions that export a `parser` function will have the input data passed through the parser before being passed to `p1` and `p2`
- Solutions can be run with `python . <day> <part>`
