import pytest

from src.interpreter import Parser

from src.expressions.atom import *
from src.expressions.special import *
from src.expressions.application import *


@pytest.fixture
def pr():
    return Parser()


# atom expression tests


def test_number_parsing(pr):
    numb_obj = pr.parse('1')[0]
    assert isinstance(numb_obj, Number)


def test_variable_lookup_parsing(pr):
    var_obj = pr.parse('a')[0]
    assert isinstance(var_obj, Variable)


# special forms tests


def test_quote_expr_parsing_0(pr):
    quote_obj = pr.parse('\'some_text')[0]
    assert isinstance(quote_obj, Quote)


def test_quote_expr_parsing_1(pr):
    quote_obj = pr.parse('\'(1 2 3)')[0]
    assert isinstance(quote_obj, Quote)


def test_assignment_parsing(pr):
    assign_obj = pr.parse('(set! a 1)')[0]
    assert isinstance(assign_obj, Assignment)


def test_definition_parsing_0(pr):
    def_obj = pr.parse('(define a 1)')[0]
    assert isinstance(def_obj, Definition)


def test_definition_parsing_1(pr):
    def_obj = pr.parse('(define (f a b) (+ a b))')[0]
    assert isinstance(def_obj, Definition)


def test_if_cond_parsing(pr):
    if_obj = pr.parse('(if (= 1 1) (+ 1 1) (* 2 2))')[0]
    assert isinstance(if_obj, IfCondition)


def test_lambda_parsing(pr):
    lambda_obj = pr.parse('(lambda (x) (* x x))')[0]
    assert isinstance(lambda_obj, Lambda)


def test_begin_parsing(pr):
    begin_obj = pr.parse('(begin (define x 1) (* x x))')[0]
    assert isinstance(begin_obj, BeginExpr)


def test_cond_parsing(pr):
    cond_obj = pr.parse('(cond ((= 1 2) 2) (else 3))')[0]
    assert isinstance(cond_obj, Cond)


# application tests


def test_application_parsing_0(pr):
    appl_obj = pr.parse('(+ 1 2)')[0]
    assert isinstance(appl_obj, Application)


def test_application_parsing_1(pr):
    appl_obj = pr.parse('(+ a b)')[0]
    assert isinstance(appl_obj, Application)


# inner methods tests


def test_tokenize_on_simple_expr(pr):
    expr = '(+ 1 2)'
    assert pr._tokenize(expr) == [['+', '1', '2']]


def test_tokenize_on_multiple_simple_expr(pr):
    expr = '(define a 3) (+ a 4)'
    assert pr._tokenize(expr) == [['define', 'a', '3'], ['+', 'a', '4']]


def test_tokenize_on_nested_expr_0(pr):
    expr = '(define (a b) (+ b 1))'
    assert pr._tokenize(expr) == [['define', ['a', 'b'], ['+', 'b', '1']]]


def test_tokenize_on_nested_expr_1(pr):
    expr = '(+ (* (/ 2 1) 3) (- 5 2))'
    assert pr._tokenize(expr) == [
        ['+', ['*', ['/', '2', '1'], '3'], ['-', '5', '2']]]


def test_tokenize_on_cond_expr(pr):
    expr = '(cond ((= 1 2) 3) (else 4))'
    assert pr._tokenize(expr) == [
        ['cond', [['=', '1', '2'], '3'], ['else', '4']]]
