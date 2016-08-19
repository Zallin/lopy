from src.lopy_abc import Expression


class Number(Expression):

    def __init__(self, n):
        self.number = float(n)

    def eval(self, env):
        return self.number

    @staticmethod
    def supported_exprs():
        return ['Number']


class Variable(Expression):

    def __init__(self, v):
        self.var_name = v

    def eval(self, env):
        return env.find(self.var_name)

    @staticmethod
    def supported_exprs():
        return ['Variable']

    def name(self):
        return self.var_name
