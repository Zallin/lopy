import re
import inspect
import importlib


def import_module_classes(mod_name):
    mod = importlib.import_module(mod_name)
    classes = []
    for _, obj in mod.__dict__.items():
        if inspect.isclass(obj) and obj.__module__ == mod_name:
            classes.append(obj)
    return classes
