import dynamic_import as di
import settings

from lo_parser import Parser
from environment import Environment


class Interpreter:

    def __init__(self):
        self.global_env = Environment()
        for Proc_class in di.import_module_classes(settings.BUILTIN_PROC_MOD_NAME):
            proc_obj = Proc_class()
            self.global_env.set_binding(repr(proc_obj), proc_obj)
        self.parser = Parser()

    def eval(self, raw_src):
        exprs = self.parser.parse(raw_src)
        return [exp.eval(self.global_env) for exp in exprs][-1]
