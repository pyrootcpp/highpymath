from .highpymath import sum as _sum
from .highpymath import sub as _sub
from .highpymath import mul as _mul
from .highpymath import div as _div
from .highpymath import exp as _exp
from .highpymath import sqrt as _sqrt
from .highpymath import log as _log
from .highpymath import MathValueError as _mve
from .highpymath import factorial as _factorial
from .highpymath import reciprocal as _reciprocal

__all__ = ['sum', 'sub', 'mul', 'div', 'MathValueError', 'exp', 'sqrt', 'log', 'reciprocal']

class MathValueError(_mve):
    """
    Exception Class for Math Value Errors.
    """
    def __init__(self, *args: object):
        """
        Initial the Exception Class with Given Arguments.
        """
        self.args_list = list(args)
        self.args_str = str(args)
        super().__init__(*args)

def sum(a: any, b: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Summary of 2 Numbers.
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if not isinstance(b, (int, float)):
        raise MathValueError("b must be a number")
    if isinstance(a, int):
        a = float(a)
    if isinstance(b, int):
        b = float(b)
    _result = _sum(a=a, b=b)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def sub(a: any, b: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Subtraction of 2 Numbers.
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if not isinstance(b, (int, float)):
        raise MathValueError("b must be a number")
    if isinstance(a, int):
        a = float(a)
    if isinstance(b, int):
        b = float(b)
    _result = _sub(a=a, b=b)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def mul(a: any, b: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Multiplication of 2 Numbers.
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if not isinstance(b, (int, float)):
        raise MathValueError("b must be a number")
    if isinstance(a, int):
        a = float(a)
    if isinstance(b, int):
        b = float(b)
    _result = _mul(a=a, b=b)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def div(a: any, b: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Division of 2 Numbers.
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if not isinstance(b, (int, float)):
        raise MathValueError("b must be a number")
    if isinstance(a, int):
        a = float(a)
    if isinstance(b, int):
        b = float(b)
    _result = _div(a=a, b=b)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def exp(base: any, power: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Exponentiation of 2 Numbers.
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(base, (int, float)):
        raise MathValueError("base must be a number")
    if not isinstance(power, (int, float)):
        raise MathValueError("power must be a number")
    if isinstance(base, int):
        base = float(base)
    if isinstance(power, int):
        power = float(power)
    _result = _exp(base=base, power=power)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def sqrt(base: any, power: any = 2, return_int: bool = False, return_string: bool = False):
    """
    Create the Square Root of a Number.
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(base, (int, float)):
        raise MathValueError("base must be a number")
    if not isinstance(power, (int, float)):
        raise MathValueError("power must be a number")
    if isinstance(base, int):
        base = float(base)
    if isinstance(power, int):
        power = float(power)
    _result = _sqrt(base=base, power=power)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def log(base: any, power: any = 10, return_int: bool = False, return_string: bool = False):
    """
    Create the Logarithm of a Number.
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(base, (int, float)):
        raise MathValueError("base must be a number")
    if not isinstance(power, (int, float)):
        raise MathValueError("power must be a number")
    if isinstance(base, int):
        base = float(base)
    if isinstance(power, int):
        power = float(power)
    _result = _log(base=base, power=power)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def reciprocal(a: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Reciprocal of a Number.
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if isinstance(a, int):
        a = float(a)
    _result = _reciprocal(a=a)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def factorial(a: int, return_int: bool = False, return_string: bool = False):
    """
    Get the Factorial from a Number.
    """
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, int):
        raise MathValueError("a must be an integer")
    _result = _factorial(a=a)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result