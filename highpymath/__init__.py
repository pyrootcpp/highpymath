from .highpymath import sum as _sum
from .highpymath import sub as _sub
from .highpymath import mul as _mul
from .highpymath import div as _div

__all__ = ['sum', 'sub', 'mul', 'div']

def sum(a: float, b: float):
    """
    Create the Summary from 2 Numbers.
    """
    return _sum(a=a, b=b)
