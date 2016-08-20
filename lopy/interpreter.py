import dynamic_import as di

from parser import Parser


class Environment:

    def __init__(self, enclosing=None):
        self.env = {}
        self.enclosing = enclosing

    def set_binding(self, name, obj):
        self.env[name] = obj

    def find(self, name):
        if name in self.env:
            return self.env[name]
        if self.enclosing:
            return self.enclosing.find(name)

    def extend(self):
        return type(self)(enclosing=self)


class Interpreter:

    def __init__(self):
        self.global_env = Environment()
        for Proc_class in di.import_module_classes('builtin'):
            proc_obj = Proc_class()
            self.global_env.set_binding(repr(proc_obj), proc_obj)
        self.parser = Parser()

    def eval(self, raw_src):
        exprs = self.parser.parse(raw_src)
        for exp in exprs:
            res = exp.eval(self.global_env)
        return res
