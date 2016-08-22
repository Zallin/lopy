import operator as op
import functools as ft

from lopy_abc import BuiltinProcedure

# TO THINK
# change to function with corresponding repr ?


class EqualityOp(BuiltinProcedure):

    @staticmethod
    def apply(a, b):
        return a == b

    @staticmethod
    def __repr__():
        return '='


class SumOp(BuiltinProcedure):

    @staticmethod
    def apply(*args):
        return ft.reduce(lambda v, el: v + el, args, 0)

    @staticmethod
    def __repr__():
        return '+'


class MultOp(BuiltinProcedure):

    @staticmethod
    def apply(*args):
        return ft.reduce(lambda v, el: v * el, args, 1)

    @staticmethod
    def __repr__():
        return '*'


class SubstractOp(BuiltinProcedure):

    @staticmethod
    def apply(*args):
        return ft.reduce(lambda v, el: v - el, args[1:], args[0])

    @staticmethod
    def __repr__():
        return '-'


class GreaterOp(BuiltinProcedure):

    @staticmethod
    def apply(a, b):
        return a > b

    @staticmethod
    def __repr__():
        return '>'


class DivisionOp(BuiltinProcedure):

    @staticmethod
    def apply(a, b):
        return a / b

    @staticmethod
    def __repr__():
        return '/'


class RemainderOp(BuiltinProcedure):

    @staticmethod
    def apply(a, b):
        return a % b

    @staticmethod
    def __repr__():
        return 'remainder'
