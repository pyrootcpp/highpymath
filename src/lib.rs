use pyo3::prelude::*;
use pyo3::exceptions::PyException;
use pyo3::create_exception;

create_exception!(highpymath, MathValueError, PyException);

#[cfg(target_pointer_width = "32")]
type PyFloat = f32;
#[cfg(target_pointer_width = "64")]
type PyFloat = f64;

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
    m.add_function(wrap_pyfunction!(reciprocal, m)?)?;
    m.add("MathValueError", m.py().get_type::<MathValueError>())?;
    Ok(())
}