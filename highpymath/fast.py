from highpymath import log as _log
from highpymath import exp as _exp
from highpymath import MathTypeError, MathValueError

def fast_mul(a: any, b: any, return_int: bool = False, return_string: bool = False):
    """
    Fast multiplication of two numbers
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathTypeError("a must be a number")
    if not isinstance(b, (int, float)):
        raise MathTypeError("b must be a number")
    if isinstance(a, int):
        a = float(a)
    if isinstance(b, int):
        b = float(b)
    _result = _log(base=a, power=10) + _log(base=b, power=10)
    _result = _exp(base=10, power=_result)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def fast_div(a: any, b: any, return_int: bool = False, return_string: bool = False):
    """
    Fast division of two numbers
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathTypeError("a must be a number")
    if not isinstance(b, (int, float)):
        raise MathTypeError("b must be a number")
    if isinstance(a, int):
        a = float(a)
    if isinstance(b, int):
        b = float(b)
    _result = _log(base=a, power=10) - _log(base=b, power=10)
    _result = _exp(base=10, power=_result)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def fast_exp(base: any, power: any = 2, return_int: bool = False, return_string: bool = False):
    """
    Fast exponentiation of a number
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(base, (int, float)):
        raise MathTypeError("base must be a number")
    if not isinstance(power, (int, float)):
        raise MathTypeError("power must be a number")
    if isinstance(base, int):
        base = float(base)
    if isinstance(power, int):
        power = float(power)
    _start = 1
    _result = 0
    while _start < power:
        _result += _log(base=base, power=10)
        _start += 1
    _result = _exp(base=10, power=_result)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result