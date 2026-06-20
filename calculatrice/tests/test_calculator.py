#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from modules.calculator import (
    DivisionByZeroError,
    add,
    subtract,
    multiply,
    divide
)

def test_add_positive() -> None: #un test a toujours ce typage
    assert add(2, 3) == 5 # un seul assert par test

def test_add_negative() -> None:
    assert add(-2, 3) == 1

def test_add_two_negative_numbers() -> None:
    assert add(-2, -3) == -5

def test_add_zero() -> None:
    assert add(0, 0) == 0

def test_add_float() -> None:
    assert add(2.5, 1.5) == 4.0

def test_subtract() -> None:
    assert subtract(5, 3) == 2

def test_subtract_negative_number() -> None:
    assert subtract(2, -3) == 5

def test_multiply() -> None:
    assert multiply(4, 3) == 12

def test_multiply_negative() -> None:
    assert multiply(4, -3) == -12

def test_multiply_two_negative_numbers() -> None:
    assert multiply(-4, -3) == 12

def test_multiply_zero() -> None:
    assert multiply(42, 0) == 0

def test_multiply_one() -> None:
    assert multiply(42, 1) == 42

def test_divide_by_zero() -> None:
    with pytest.raises(DivisionByZeroError):
        divide(10, 0)

def test_divide_float() -> None:
    assert divide(5, 2) == 2.5

def test_divide_int() -> None:
    assert divide(4, 2) == 2

def test_divide_negative() -> None:
    assert divide(4, -2) == -2

def test_divide_two_negative_numbers() -> None:
    assert divide(-4, -2) == 2