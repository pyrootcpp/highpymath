highpymath
==========

This is a Python library for high-quality mathematical calculations.

Language
========

This library is written in Rust and Python, combining the performance of Rust with the ease of use of Python.

The main implementation for calculations is in Rust, while Python is used to write user-facing functions. This approach ensures efficient computation with user-friendly interfaces.

Python Wrapper Functions
========================

The Python wrapper functions enhance the conversion between Python and Rust, making it easier for users to utilize the core Rust implementations. These wrappers add flexibility by allowing various input types and output formats.

Example: The `sqrt` Function
---------------------------

Let's examine the `sqrt` function, which calculates the root of a number based on the specified power.

Rust Implementation:
--------------------

.. code-block:: rust

    #[pyfunction]
    fn sqrt(base: f32, power: f32) -> PyResult<f32> {
        if base < 0.0 && power % 2.0 == 0.0 {
            Err(MathValueError::new_err("Negative base for even power"))
        } else {
            Ok(base.powf(1.0 / power))
        }
    }

This Rust function accepts only floating-point numbers and returns a float as a result. It handles errors for cases where the base is negative and the power is even, as these conditions would result in a non-real number.

Python Wrapper Implementation:
------------------------------

.. code-block:: python

    # __init__.py

    from .highpymath import sqrt as _sqrt  # Import sqrt as a private function

    def sqrt(base: any, power: any, return_int: bool = False, return_string: bool = False):
        """
        Calculate the root of a number with specified power.
        Allows for returning results as integer or string.
        """
        if not isinstance(base, (int, float)):
            raise MathValueError("Base must be a numeric type")
        if not isinstance(power, (int, float)):
            raise MathValueError("Power must be a numeric type")

        base = float(base)
        power = float(power)
        result = _sqrt(base=base, power=power)

        if return_int:
            result = int(result)
        elif return_string:
            result = str(result)
        return result

Usage Examples:
---------------

.. code-block:: bash

    Python 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0] on linux
    >>> import highpymath as math
    >>> math.sqrt(81, 2)
    9.0
    >>> math.sqrt(81, 2, return_string=True)
    '9.0'
    >>> math.sqrt(81, 2, return_int=True)
    9
    >>> math.sqrt(81, 2, return_int=True, return_string=True)
    '9'

This section provides practical examples of how to use the `sqrt` function with different settings for return types.

Conclusion
==========

The `highpymath` library offers a robust solution for mathematical calculations by leveraging the strengths of both Rust and Python. It is designed to be both efficient and user-friendly, accommodating a wide range of user requirements.
