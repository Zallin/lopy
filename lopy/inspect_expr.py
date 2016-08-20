def is_procedure(expr):
    return 'lambda' in expr.supported_exprs()


def is_builtin(expr):
    return getattr(expr, 'apply', None) and True


def is_application(expr):
    return getattr(expr, 'operands_names', None) and True
