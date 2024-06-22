use pyo3::prelude::*;
use pyo3::exceptions::PyException;
use pyo3::create_exception;

create_exception!(highpymath, MathValueError, PyException);

#[cfg(target_pointer_width = "32")]
type PyFloat = f32;
#[cfg(target_pointer_width = "64")]
type PyFloat = f64;

#[cfg(target_pointer_width = "32")]
type PyInt = i32;
#[cfg(target_pointer_width = "64")]
type PyInt = i64;

#[cfg(target_pointer_width = "32")]
type PyIntLong = i64;
#[cfg(target_pointer_width = "64")]
type PyIntLong = i128;

#[pyfunction]
fn sum(a: PyFloat, b: PyFloat) -> PyResult<PyFloat> {
    Ok(a + b)
}

#[pyfunction]
fn sub(a: PyFloat, b: PyFloat) -> PyResult<PyFloat> {
    Ok(a - b)
}

#[pyfunction]
fn mul(a: PyFloat, b: PyFloat) -> PyResult<PyFloat> {
    Ok(a * b)
}

#[pyfunction]
fn div(a: PyFloat, b: PyFloat) -> PyResult<PyFloat> {
    if b == 0.0 {
        Err(MathValueError::new_err("Division by Zero"))
    } else {
        Ok(a / b)
    }
}

#[pyfunction]
fn exp(base: PyFloat, power: PyFloat) -> PyResult<PyFloat> {
    Ok(base.powf(power))
}

#[pyfunction]
fn sqrt(base: PyFloat, power: PyFloat) -> PyResult<PyFloat> {
    if base < 0.0 && power % 2.0 == 0.0 {
        Err(MathValueError::new_err("Negative Base for even Power"))
    } else {
        Ok(base.powf(1.0 / power))
    }
}

#[pyfunction]
fn log(base: PyFloat, power: PyFloat) -> PyResult<PyFloat> {
    if base <= 0.0 || base == 1.0 {
        Err(MathValueError::new_err("Base must be greater than 0 and not equal to 1"))
    } else if power <= 0.0 {
        Err(MathValueError::new_err("Power must be greater than 0"))
    } else {
        Ok(base.log(power))
    }
}

#[pyfunction]
fn reciprocal(a: PyFloat) -> PyResult<PyFloat> {
    if a == 0.0 {
        Err(MathValueError::new_err("Division by Zero"))
    } else {
        Ok(1.0 / a)
    }
}

#[pyfunction]
fn factorial(a: PyInt) -> PyResult<PyInt> {
    if a < 0 {
        Err(MathValueError::new_err("Negative input not allowed"))
    } else {
        let mut result: PyInt = 1;
        for i in 1..=a {
            result = result.checked_mul(i).ok_or_else(|| {
                PyErr::new::<PyException, _>("Integer overflow")
            })?;
        }
        Ok(result)
    }
}

#[pyfunction]
/// Berechnet die Summe von `a` und `b`. bei Gleichungen a + b = c
fn linear_base_c(a: PyFloat, b: PyFloat) -> PyResult<PyFloat> {
    Ok(a + b)
}

#[pyfunction]
/// Berechnet `c` minus `a`, um `b` zu isolieren. bei Gleichungen a + b = c
fn linear_base_b(a: PyFloat, c: PyFloat) -> PyResult<PyFloat> {
    Ok(c - a)
}

#[pyfunction]
/// Berechnet `c` minus `b`, um `a` zu isolieren. bei Gleichungen a + b = c
fn linear_base_a(b: PyFloat, c: PyFloat) -> PyResult<PyFloat> {
    Ok(c - b)
}

#[pyfunction]
fn sin(a: PyFloat) -> PyResult<PyFloat> {
    Ok(a.sin())
}

#[pyfunction]
fn cos(a: PyFloat) -> PyResult<PyFloat> {
    Ok(a.cos())
}

#[pyfunction]
fn tan(a: PyFloat) -> PyResult<PyFloat> {
    Ok(a.tan())
}

#[pyfunction]
fn asin(a: PyFloat) -> PyResult<PyFloat> {
    Ok(a.asin())
}

#[pyfunction]
fn acos(a: PyFloat) -> PyResult<PyFloat> {
    Ok(a.acos())
}

#[pyfunction]
fn atan(a: PyFloat) -> PyResult<PyFloat> {
    Ok(a.atan())
}

#[pyfunction]
fn arctan(x: PyFloat) -> PyResult<PyFloat> {
    /// Berechne den arcus tangens Wert mit der Leibniz-Reihe
    let mut result: PyFloat = 0.0;
    let mut term: PyFloat = x;  // Startterm x^1 / 1
    let mut i: PyInt = 1;

    while term.abs() > 1e-15 {
        if i % 2 == 1 {
            result += term;  // Addiere ungerade Terme
        } else {
            result -= term;  // Subtrahiere gerade Terme
        }
        i += 1;
        term = term * x * x / ((2 * i - 1) as PyFloat) * ((2 * i - 2) as PyFloat);  // Update term zu x^(2i+1) / (2i+1)
    }
    Ok(result)
}

/// A Python module implemented in Rust.
#[pymodule]
fn highpymath(m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum, m)?)?;
    m.add_function(wrap_pyfunction!(sub, m)?)?;
    m.add_function(wrap_pyfunction!(mul, m)?)?;
    m.add_function(wrap_pyfunction!(div, m)?)?;
    m.add_function(wrap_pyfunction!(exp, m)?)?;
    m.add_function(wrap_pyfunction!(sqrt, m)?)?;
    m.add_function(wrap_pyfunction!(log, m)?)?;
    m.add_function(wrap_pyfunction!(factorial, m)?)?;
    m.add_function(wrap_pyfunction!(reciprocal, m)?)?;
    m.add_function(wrap_pyfunction!(linear_base_c, m)?)?;
    m.add_function(wrap_pyfunction!(linear_base_b, m)?)?;
    m.add_function(wrap_pyfunction!(linear_base_a, m)?)?;
    m.add_function(wrap_pyfunction!(sin, m)?)?;
    m.add_function(wrap_pyfunction!(cos, m)?)?;
    m.add_function(wrap_pyfunction!(tan, m)?)?;
    m.add_function(wrap_pyfunction!(asin, m)?)?;
    m.add_function(wrap_pyfunction!(acos, m)?)?;
    m.add_function(wrap_pyfunction!(atan, m)?)?;
    m.add_function(wrap_pyfunction!(arctan, m)?)?;
    m.add("MathValueError", m.py().get_type::<MathValueError>())?;
    Ok(())
}