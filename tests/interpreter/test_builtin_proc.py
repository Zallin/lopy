import pytest

from src.interpreter import Interpreter


def test_builtin_addition_with_two_args(ipr):
    expr = '(+ 1 1)'
    ipr.eval(expr) == 2.0


def test_builtin_addition_with_three_args(ipr):
    expr = '(+ 1 1 1)'
    ipr.eval(expr) == 3.0


def test_builtin_addition_nested(ipr):
    expr = '(+ (+ 1 2) (+ (+ 1 2) 2))'
    ipr.eval(expr) == 8.0


def test_builtin_substr_with_two_args(ipr):
    expr = '(- 2 1)'
    ipr.eval(expr) == 1.0


def test_builtin_substr_with_three_args(ipr):
    expr = '(- 3 2 1)'
    ipr.eval(expr) == 0.0


def test_builtin_substr_nested(ipr):
    expr = '(- 10 (- 1 (- 4 3)) 5)'
    ipr.eval(expr) == 5.0


def test_builtin_mul(ipr):
    expr = '(* 2 2)'
    ipr.eval(expr) == 4.0


def test_builtin_mul_with_three_args(ipr):
    expr = '(* 1 2 3)'
    ipr.eval(expr) == 6


def test_builtin_mul_nested(ipr):
    expr = '(* 2 (* 1 (* 2 4)) 4)'
    ipr.eval(expr) == 64


def test_builtin_div(ipr):
    expr = '(/ 4 2)'
    ipr.eval(expr) == 2.0


def test_builtin_div_nested(ipr):
    expr = '(/ 4 (/ 2 2))'
    ipr.eval(expr) == 4
