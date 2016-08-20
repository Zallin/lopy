import operator as op
import functools as ft

# TO THINK
# change to function with corresponding repr ?


class EqualityOp:

    @staticmethod
    def __repr__():
        return '='

    @staticmethod
    def apply(a, b):
        return a == b


class SumOp:

    @staticmethod
    def __repr__():
        return '+'

    @staticmethod
    def apply(*args):
        return ft.reduce(lambda v, el: v + el, args, 0)


class MultOp:

    @staticmethod
    def __repr__():
        return '*'

    @staticmethod
    def apply(*args):
        return ft.reduce(lambda v, el: v * el, args, 1)


class SubstractOp:

    @staticmethod
    def __repr__():
        return '-'

    @staticmethod
    def apply(*args):
        return ft.reduce(lambda v, el: v - el, args[1:], args[0])


class GreaterOp:

    @staticmethod
    def __repr__():
        return '>'

    @staticmethod
    def apply(a, b):
        return a > b


class DivisionOp:

    @staticmethod
    def __repr__():
        return '/'

    @staticmethod
    def apply(a, b):
        return a / b


class RemainderOp:

    @staticmethod
    def __repr__():
        return 'remainder'

    @staticmethod
    def apply(a, b):
        return a % b
