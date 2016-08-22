import abc


class Expression(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def eval(self, env):
        pass

    @staticmethod
    @abc.abstractmethod
    def supported_exprs():
        pass


class BuiltinProcedure(metaclass=abc.ABCMeta):

    @staticmethod
    @abc.abstractmethod
    def apply(*args):
        pass

    @staticmethod
    @abc.abstractmethod
    def __repr__():
        pass
