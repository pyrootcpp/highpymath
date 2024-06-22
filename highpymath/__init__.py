from .highpymath import sum as _sum
from .highpymath import sub as _sub
from .highpymath import mul as _mul
from .highpymath import div as _div
from .highpymath import MathValueError as _mve

__all__ = ['sum', 'sub', 'mul', 'div', 'MathValueError']

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

def sum(a: any, b: any, return_int: bool = False, return_float: bool = True, return_string: bool = False):
    """
    Create the Summary of 2 Numbers.
    """
    if return_int and return_float:
        raise MathValueError("return_int and return_double cannot be used together")
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

def sub(a: any, b: any, return_int: bool = False, return_float: bool = True, return_string: bool = False):
    """
    Create the Subtraction of 2 Numbers.
    """
    if return_int and return_float:
        raise MathValueError("return_int and return_double cannot be used together")
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

