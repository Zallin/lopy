import context
import pytest

from interpreter import Interpreter
from expressions.special import *


@pytest.fixture
def ipr():
    return Interpreter()


def test_number_evaluation(ipr):
    assert ipr.eval('1') == 1.0


def test_variable_lookup(ipr):
    expr = '(define a 3) a'
    assert ipr.eval(expr) == 3.0


def test_proc_definition(ipr):
    expr = '(define (f a) (+ a 1)) f'
    proc_obj = ipr.eval(expr)
    assert isinstance(proc_obj, RuntimeLambda)


def test_proc_definition_with_multiple_inner_exprs(ipr):
    expr = '(define (f a) (+ a 1) 3) f'
    proc_obj = ipr.eval(expr)
    assert isinstance(proc_obj, RuntimeLambda)


def test_variable_assignment(ipr):
    expr = '(define a 1) (set! a 2) a'
    assert ipr.eval(expr) == 2


def test_if_cond_with_true_predicate(ipr):
    expr = '(if (= 1 1) 3 4)'
    assert ipr.eval(expr) == 3


def test_if_cond_with_false_predicate(ipr):
    expr = '(if (= 2 1) 3 4)'
    assert ipr.eval(expr) == 4


def test_lambda_definition(ipr):
    expr = '(lambda (x) (+ x 1))'
    lambda_obj = ipr.eval(expr)
    assert isinstance(lambda_obj, RuntimeLambda)


def test_lambda_application(ipr):
    expr = '((lambda (x) (+ x 1)) 1)'
    assert ipr.eval(expr) == 2


def test_begin(ipr):
    expr = '(begin (define a 1) (set! a 2) (set! a 3) a)'
    assert ipr.eval(expr) == 3


def test_cond_without_else(ipr):
    expr = '(cond ((= 2 1) 1) ((= 1 1) 2))'
    assert ipr.eval(expr) == 2


def test_cond_with_else(ipr):
    expr = '(cond ((= 2 1) 1) ((= 3 1) 2) (else 3))'
    assert ipr.eval(expr) == 3


def test_recursive_proc(ipr):
    expr = '(define (factorial n) (if (= n 1) 1 (* n (factorial (- n 1))))) (factorial 10)'
    assert ipr.eval(expr) == 3628800


def test_proc_with_inner_definition(ipr):
    expr = '(define (expt b n) (define (expt-iter counter product) (if (= counter 0) product (expt-iter (- counter 1) (* b product)))) (expt-iter n 1)) (expt 3 3)'
    assert ipr.eval(expr) == 27


def test_higher_order_proc(ipr):
    expr = '(define (sum term a next b) (if (> a b) 0 (+ (term a) (sum term (next a) next b)))) (define (cube x) (* x x x)) (define (inc a) (+ a 1)) (sum cube 1 inc 4)'
    assert ipr.eval(expr) == 100
