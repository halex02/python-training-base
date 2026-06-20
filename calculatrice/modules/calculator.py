#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class DivisionByZeroError(Exception):
    """Raised when typing to divide by zero."""

def add(a:float, b:float)->float:
    """Return the sum of a and b."""
    return a + b

def substract(a:float, b:float)->float:
    """Return the difference between a and b."""
    return a - b

def multiply(a:float, b:float)->float:
    """Return the product of a and b."""
    return a * b

def divide(a:float, b:float)->float:
    """Return a divided by b."""
    if b == 0:
        raise DivisionByZeroError("Division by zero is not allowed.")
    return a / b

