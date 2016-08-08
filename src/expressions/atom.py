import src.expressions.expression_abc as e_abc


class Number(e_abc.Expression):

    def __init__(self, n):
        self.number = float(n)

    def eval(self, env):
        return self.number

    @staticmethod
    def supported_exprs():
        return ['Number']


class Variable(e_abc.Expression):

    def __init__(self, v):
        self.var_name = v

    def eval(self, env):
        pass

    @staticmethod
    def supported_exprs():
        return ['Variable']
