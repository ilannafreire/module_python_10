# FuncMage - Python Functional Programming

This repository contains five Python exercises focused on functional programming.
Each exercise explores a core concept, progressing from lambda expressions to
higher-order functions, closures, `functools`, and decorators.

## Requirements

- Python 3.10 or newer
- No third-party packages required by the exercises
- Optional: `flake8` for linting and `mypy` for type checking

Check the installed Python version:

```bash
python3 --version
```

## Run an Exercise

From the project root, run the desired exercise file directly:

```bash
python3 ex0/lambda_spells.py
```

Replace the path with any exercise listed below.

## Exercises

### ex0 - Lambda Sanctum

File: `ex0/lambda_spells.py`

Uses lambda expressions with `sorted()`, `filter()`, `map()`, `max()`, and
`min()` to organize magical artifacts, filter mages, transform spell names, and
calculate mage power statistics.

**Topics:** Lambda expressions, `map`, `filter`, sorting with keys, data
transformation

```bash
python3 ex0/lambda_spells.py
```

### ex1 - Higher Realm

File: `ex1/higher_magic.py`

Demonstrates higher-order functions by combining spells, amplifying power,
casting conditionally, and running a sequence of spells. Functions are passed
as arguments and returned as new functions.

**Topics:** First-class functions, higher-order functions, function composition,
`Callable`

```bash
python3 ex1/higher_magic.py
```

### ex2 - Memory Depths

File: `ex2/scope_mysteries.py`

Uses closures and lexical scoping to create independent counters, power
accumulators, enchantment factories, and a private memory vault.

**Topics:** Closures, lexical scoping, `nonlocal`, private state without globals

```bash
python3 ex2/scope_mysteries.py
```

### ex3 - Ancient Library

File: `ex3/functools_artifacts.py`

Explores tools from `functools`: `reduce` for aggregating spell power, `partial`
for specialized enchantments, `lru_cache` for memoized Fibonacci values, and
`singledispatch` for type-based spell handling.

**Topics:** `reduce`, `partial`, memoization, `lru_cache`, `singledispatch`,
`operator`

```bash
python3 ex3/functools_artifacts.py
```

### ex4 - Master's Tower

File: `ex4/decorator_mastery.py`

Builds decorators for timing spells, validating power levels, and retrying failed
spells. It also demonstrates a `@staticmethod` for mage-name validation.

**Topics:** Decorators, `functools.wraps`, decorator factories, retries,
`staticmethod`

```bash
python3 ex4/decorator_mastery.py
```

## Test Data Generator

The repository includes `generator.tar.gz`, containing a small generator for
sample mages, artifacts, and spells.

```bash
tar -xzf generator.tar.gz
python3 generator/data_generator.py
```

## Code Quality

All exercises include:

- Type hints for functions and return values
- English docstrings
- Clear and focused examples of functional programming patterns
- No external dependencies
- No file I/O or global state in the exercise implementations

Run the static checks from the project root:

```bash
mypy ex0 ex1 ex2 ex3 ex4
flake8 ex0 ex1 ex2 ex3 ex4
```

Run all exercises in sequence:

```bash
for file in ex0/lambda_spells.py ex1/higher_magic.py ex2/scope_mysteries.py ex3/functools_artifacts.py ex4/decorator_mastery.py; do
	python3 "$file"
done
```

## Module Theme: Functional Programming

These exercises teach how Python functions can be treated as values and combined
to build reusable behavior:

- **Lambda expressions:** concise transformations and filtering
- **Higher-order functions:** functions that receive or return functions
- **Closures:** functions that preserve their creation environment
- **Functools:** reusable functional tools from the standard library
- **Decorators:** reusable behavior around existing functions and methods

## Learning Outcomes

After completing this module, you should understand:

- When lambda expressions are useful
- How functions can be passed, returned, and composed
- How closures preserve state without global variables
- How `reduce`, `partial`, `lru_cache`, and `singledispatch` work
- How decorators separate reusable concerns from business logic
- The difference between static methods and instance methods