# Mini-Project 4: Calculator

## Introduction

You are building a command-line calculator. You want to use Python's built-in `eval` function, but can't risk doing so without sanitizing user input to avoid command injection.

You have decided to write your own `calculate` function that behaves the same way as `eval`, but only for numeric calculations.

## Setup

As usual, start by running `poetry install`. To run the calculator, simply use `python calculator.py`. To run the tests, use `poetry run pytest`.

## Grading

Each of the 100 tests is worth 1 point, meaning that an overall grade of 100 can be achieved by passing all tests.

You are not allowed to use the `eval` function, or anything similar, anywhere in your calculator code - you must parse and execute any given expression manually.

Any situation which would result in complex arithmetic, such as fractional powers of negative numbers, is not required to be handled, although you may do so if you wish.
