from src.interpreter import Parser

from src.expressions.atom import *
from src.expressions.special import *
from src.expressions.combinations import *


@pytest.fixture
def pr():
    return Parser()


# atom expression tests


def test_number_parsing(pr):
    numb_obj = pr.parse('1')
    assert isinstance(numb_obj, Number)


def test_variable_lookup_parsing(pr):
    var_obj = pr.parse('a')
    assert isinstance(var_obj, Variable)


# special forms tests


def test_quote_expr_parsing_0(pr):
    quote_obj = pr.parse('\'some_text')
    assert isinstance(quote_obj, Quote)


def test_quote_expr_parsing_1(pr):
    quote_obj = pr.parse('\'(1 2 3)')
    assert isinstance(quote_obj, Quote)


def test_assignment_parsing(pr):
    assign_obj = pr.parse('(set! a 1)')
    assert isinstance(assign_obj, Assignment)


def test_definition_parsing_0(pr):
    def_obj = pr.parse('(define a 1)')
    assert isinstance(def_obj, Definition)


def test_definition_parsing_1(pr):
    def_obj = pr.parse('(define (f a b) (+ a b))')
    assert isinstance(def_obj, Definition)


def test_if_cond_parsing(pr):
    if_obj = pr.parse('(if (= 1 1) (+ 1 1) (* 2 2))')
    assert isinstance(if_obj, IfCondition)


def test_lambda_parsing(pr):
    lambda_obj = pr.parse('(lambda (x) (* x x))')
    assert isinstance(lambda_obj, Lambda)


def test_begin_parsing(pr):
    begin_obj = pr.parse('(begin (define x 1) (* x x))')
    assert isinstance(begin_obj, BeginExpr)


def test_cond_parsing(pr):
    cond_obj = pr.parse('(cond ((= 1 2) 2) (else 3))')
    assert isinstance(cond_obj, Cond)


# application tests


def test_application_parsing_0(pr):
    appl_obj = pr.parse('(+ 1 2)')
    assert isinstance(appl_obj, Application)


def test_application_parsing_1(pr):
    appl_obj = pr.parse('(+ a b)')
    assert isinstance(appl_obj, Application)
