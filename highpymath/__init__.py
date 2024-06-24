from .highpymath import MathValueError as _mve
from .highpymath import GeometryError as _ge

__all__ = ['sum', 'sub', 'mul', 'div', 'MathValueError', 'exp', 'sqrt', 'log', 'reciprocal', 'factorial', 'calc_pi', 'calc_e']

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

class GeometryError(_ge):
    """
    Exception Class for Geometry Errors.
    """
    def __init__(self, *args: object):
        """
        Initial the Exception Class with Given Arguments.
        """
        self.args_list = list(args)
        self.args_str = str(args)
        super().__init__(*args)

__all__.append('GeometryError')

def sum(a: any, b: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Summary of 2 Numbers.
    """
    from .highpymath import sum as _sum
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
    from .highpymath import sub as _sub
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
    from .highpymath import mul as _mul
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
    from .highpymath import div as _div
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
    from .highpymath import exp as _exp
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
    from .highpymath import sqrt as _sqrt
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
    from .highpymath import log as _log
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
    from .highpymath import reciprocal as _reciprocal
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
    from .highpymath import factorial as _factorial
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

def sin(a: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Sinus of a Number.
    """
    from .highpymath import sin as _sin
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if isinstance(a, int):
        a = float(a)
    _result = _sin(a=a)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def cos(a: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Cosinus of a Number.
    """
    from .highpymath import cos as _cos
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if isinstance(a, int):
        a = float(a)
    _result = _cos(a=a)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def tan(a: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Tanus of a Number.
    """
    from .highpymath import tan as _tan
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if isinstance(a, int):
        a = float(a)
    _result = _tan(a=a)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def asin(a: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Arcus Sinus of a Number.
    """
    from .highpymath import asin as _asin
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if isinstance(a, int):
        a = float(a)
    _result = _asin(a=a)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def acos(a: any, return_int: bool = False, return_string: bool = False):
    """
    Create the Arcus Cosinus of a Number.
    """
    from .highpymath import acos as _acos
    return_float = True
    if return_int:
        return_float = False
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if isinstance(a, int):
        a = float(a)
    _result = _acos(a=a)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def atan(a: any, use_leibniz: bool = False, return_int: bool = False, return_string: bool = False):
    """
    Create the Arcus Tanus of a Number.
    """
    from .highpymath import atan as _atan1
    from .highpymath import arctan as _atan2
    return_float = True
    if return_int:
        return_float = False
    if use_leibniz:
        _atan = _atan2
    else:
        _atan = _atan1
    if not isinstance(a, (int, float)):
        raise MathValueError("a must be a number")
    if isinstance(a, int):
        a = float(a)
    _result = _atan(a)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

def calc_pi(return_int: bool = False, return_string: bool = False):
    """
    Get the Value of Pi.
    """
    from .highpymath import calc_pi as _calc_pi
    return_float = True
    if return_int:
        return_float = False
    _result = _calc_pi()
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

pi = calc_pi()

def calc_e(max: int = 20, return_int: bool = False, return_string: bool = False):
    """
    Calculate the euler number.
    """
    from .highpymath import factorial as _fact
    return_float = True
    if return_int:
        return_float = False
    _result = 0
    i = 0
    while i < max:
        _result += 1 / _fact(i)
        i += 1
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

e = calc_e()

class equation:
    """
    Class to Solve equations.
    """
    @staticmethod
    def quadratic(a: any, b: any, c: any = None, use_pq: bool = False, return_int: bool = False, return_string: bool = False) -> tuple:
        """
        Function to Solve a Quadratic Equation.
        Attention:
        - If you use use_pq = True, a will be used as p and b will be used as q.
        - If you use use_pq = False, a will be used as a, b will be used as b and c will be used as c.
        """
        from .highpymath import quadratic_base as _base
        from .highpymath import quadratic_pq as _pq
        return_float = True
        if return_int:
            return_float = False
        if not isinstance(a, (int, float)):
            raise MathValueError("a must be a Number")
        if not isinstance(b, (int, float)):
            raise MathValueError("b must be a Number")
        if not use_pq and c is None:
            raise MathValueError("c is set as None, but you don't use pq")
        if not use_pq and not isinstance(c, (int, float)):
            raise MathValueError("c must be a Number")
        if isinstance(a, int):
            a = float(a)
        if isinstance(b, int):
            b = float(b)
        if not use_pq and isinstance(c, int):
            c = float(c)
        if use_pq:
            p = a
            q = b
        if not use_pq:
            _result = _base(a=a, b=b, c=c)
        else:
            _result = _pq(p=p, q=q)
        _result1 = _result[0]
        _result2 = _result[1]
        if return_int:
            _result1 = int(_result1)
            _result2 = int(_result2)
        elif return_float:
            _result1 = float(_result1)
            _result2 = float(_result2)
        if return_string:
            _result1 = str(_result1)
            _result2 = str(_result2)
        return _result1, _result2
    
    @staticmethod
    def linear(a: any = None, b: any = None, c: any = None, search_a: bool = False, search_b: bool = False, search_c: bool = False, return_int: bool = False, return_string: bool = False):
        """
        Solve the Linear Function from type: a + b = c
        """
        from .highpymath import linear_base_a as _linear_base_a
        from .highpymath import linear_base_b as _linear_base_b
        from .highpymath import linear_base_c as _linear_base_c
        return_float = True
        if return_int:
            return_float = False
        if search_a and search_b and search_c:
            raise MathValueError("You need to specify one of the 3 arguments")
        if search_a and search_b:
            raise MathValueError("You need to specify one of the 3 arguments")
        if search_a and search_c:
            raise MathValueError("You need to specify one of the 3 arguments")
        if search_b and search_c:
            raise MathValueError("You need to specify one of the 3 arguments")
        if search_a:
            if not isinstance(b, (int, float)):
                raise MathValueError("b must be a number")
            if not isinstance(c, (int, float)):
                raise MathValueError("c must be a number")
            if isinstance(b, int):
                b = float(b)
            if isinstance(c, int):
                c = float(c)
            _result = _linear_base_a(b=b, c=c)
        elif search_b:
            if not isinstance(a, (int, float)):
                raise MathValueError("a must be a number")
            if not isinstance(c, (int, float)):
                raise MathValueError("c must be a number")
            if isinstance(a, int):
                a = float(a)
            if isinstance(c, int):
                c = float(c)
            _result = _linear_base_b(a=a, c=c)
        elif search_c:
            if not isinstance(a, (int, float)):
                raise MathValueError("a must be a number")
            if not isinstance(b, (int, float)):
                raise MathValueError("b must be a number")
            if isinstance(a, int):
                a = float(a)
            if isinstance(b, int):
                b = float(b)
            _result = _linear_base_c(a=a, b=b)
        if return_int:
            _result = int(_result)
        elif return_float:
            _result = float(_result)
        if return_string:
            _result = str(_result)
        return _result

equation = equation()

__all__.append('equation')

def sqrt2(base: any, return_int: bool = False, return_string: bool = False):
    """
    Calculate the Square Root of a Number.
    """
    from .highpymath import sqrt2 as _sqrt2
    return_float = True
    if return_int:
        return_float = False
    _result = _sqrt2(base=base)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

__all__.append('sqrt2')

def exp2(base: any, return_int: bool = False, return_string: bool = False):
    """
    Calculate the Exponentiation of a Number.
    """
    from .highpymath import exp2 as _exp2
    return_float = True
    if return_int:
        return_float = False
    _result = _exp2(base=base)
    if return_int:
        _result = int(_result)
    elif return_float:
        _result = float(_result)
    if return_string:
        _result = str(_result)
    return _result

__all__.append('exp2')

class GeometricProperties:
    """
    Class to Work with Geometric Properties.
    """
    @staticmethod
    def rectangle(a: any, b: any, return_area: bool = False, return_circumference: bool = False, return_both: bool = False, return_int: bool = False, return_string: bool = False):
        """
        Calculate the Area or the Circumference of a Rectangle.
        Attention
        - If you use return_both, the result will be a tuple.
        - If you use return_area, the result will be the area.
        - If you use return_circumference, the result will be the circumference.
        - If you use return_area and return_circumference, the result will be an Error.
        - You can select only one, but you must set one.
        """
        from .highpymath import rectangle_area as _ra
        from .highpymath import rectangle_circumference as _rc
        if not return_area and not return_circumference and not return_both:
            raise MathValueError("You need to specify one of the 3 arguments")
        if return_area and return_circumference:
            raise MathValueError("You need to specify one of the 3 arguments")
        if return_area and return_both:
            raise MathValueError("You need to specify one of the 3 arguments")
        if return_circumference and return_both:
            raise MathValueError("You need to specify one of the 3 arguments")
        return_flaot = True
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
        _area = _ra(a=a, b=b)
        _circumference = _rc(a=a, b=b)
        if return_int:
            _area = int(_area)
            _circumference = int(_circumference)
        elif return_float:
            _area = float(_area)
            _circumference = float(_circumference)
        if return_string:
            _area = str(_area)
            _circumference = str(_circumference)
        if return_both:
            return _area, _circumference
        elif return_area:
            return _area
        elif return_circumference:
            return _circumference
        
    @staticmethod
    def quadratic(a: any, return_area: bool = False, return_circumference: bool = False, return_both: bool = False, return_int: bool = False, return_string: bool = False):
        """
        Calculate the Area or the Circumference of a Quadratic.
        Attention
        - If you use return_both, the result will be a tuple.
        - If you use return_area, the result will be the area.
        - If you use return_circumference, the result will be the circumference.
        - If you use return_area and return_circumference, the result will be an Error.
        - You can select only one, but you must set one.
        """
        from .highpymath import quadratic_area as _qa
        from .highpymath import quadratic_circumference as _qc
        if not return_area and not return_circumference and not return_both:
            raise MathValueError("You need to specify one of the 3 arguments")
        if return_area and return_circumference:
            raise MathValueError("You need to specify one of the 3 arguments")
        if return_area and return_both:
            raise MathValueError("You need to specify one of the 3 arguments")
        if return_circumference and return_both:
            raise MathValueError("You need to specify one of the 3 arguments")
        return_float = True
        if return_int:
            return_float = False
        if not isinstance(a, (int, float)):
            raise MathValueError("a must be a number")
        if isinstance(a, int):
            a = float(a)
        _area = _qa(a=a)
        _circumference = _qc(a=a)
        if return_int:
            _area = int(_area)
            _circumference = int(_circumference)
        elif return_float:
            _area = float(_area)
            _circumference = float(_circumference)
        if return_string:
            _area = str(_area)
            _circumference = str(_circumference)
        if return_both:
            return _area, _circumference
        elif return_area:
            return _area
        elif return_circumference:
            return _circumference

GeometricProperties = GeometricProperties()

__all__.append('GeometricProperties')