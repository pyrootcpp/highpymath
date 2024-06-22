highpymath
==========

This is a Python Library for High Quality Mathematical Calculations.

language
========

This library is written in Rust and Python.

The Main implementation for Calculations is in rust, in Python is written the Functions for User.

The Python wrapper functions do a better Conversion between Python and Rust.

For Example, we will Look the sqrt function!

The Rust implementation:

.. code-block:: rust

    #[pyfunction]
    fn sqrt(base: f32, power: f32) -> PyResult<f32> {
        if base < 0.0 && power % 2.0 == 0.0 {
            Err(MathValueError::new_err("Negative Base for even Power"))
        } else {
            Ok(base.powf(1.0 / power))
        }
    }

The Rust Function allowed only Float Numbers and Returned a float number as Result.

Now we will Look the Python Wrapper implementation for the Function sqrt:

.. code-block:: python

    # __init__.py

    from .highpymath import sqrt as _sqrt # We Import sqrt, but as an Private Function

    # The implementation looks so
    def sqrt(base: any, power: any, return_int: bool = False, return_string: bool = False):
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

You can see, now you can use finally int and float numbers, you can set the return number type and you can set, should the Result returned as Number or String.

The Full Python Module will be written so.

The Rust implementation calculate the Result, but the Python wrapper make the Function multi Useful and Easy to use.

.. code-block:: bash

    Python 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import highpymath as math
    >>> math.sqrt(81, 2)
    9.0
    >>> math.sqrt(81, 2, return_string=True)
    '9.0'
    >>> math.sqrt(81, 2, return_int=True)
    9
    >>> math.sqrt(81, 2, return_int=True, return_string=True)
    '9'
    >>>