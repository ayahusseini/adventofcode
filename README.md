# README

The main folders contain solutions to https://adventofcode.com/ problems ordered by year. Inputs and test inputs can be found within the `inputs/` folder of each year. Test files are named `test_day_{x}.py`. Solution files are named `day_{x}.py`. A general template can be found in `template/`

## Current progress

|Year| Stars ⭐|
|----|--------|
|2015|30|
|2021|29|
|2022|4|
|2023|15|
|2024|24|
|**Total**|**102** ⭐ |

## Setup 

### Using UV (Recommended)

[UV](https://github.com/astral-sh/uv) is a fast Python package installer and resolver. It automatically creates and manages a virtual environment for you. To use UV:

0. If you haven't, install UV: `curl -LsSf https://astral.sh/uv/install.sh | sh` (or see [installation instructions](https://github.com/astral-sh/uv#installation))
1. Install dependencies: `uv sync`
2. `cd` into the correct folder `cd YYYY/day_x/`
3. Run code: `uv run python3 day_x.py` 
4. Run tests: `uv run pytest -vv` 


### Using pip/venv (Alternative)

- Setup a virtual environment using `python3 -m venv venv` and `source venv/bin/activate` 
- Install requirements by running `pip install -r requirements.txt`
- `cd` into the directory for a problem and run the tests using `pytest -vv`. Run the code itself with my input using `python3 day_x.py` 
