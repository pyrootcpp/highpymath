use pyo3::prelude::*;
use pyo3::exceptions::PyException;
use pyo3::create_exception;

create_exception!(highpymath, MathValueError, PyException);

#[pyfunction]
fn sum(a: f32, b: f32) -> PyResult<f32> {
    Ok(a + b)
}

#[pyfunction]
fn sub(a: f32, b: f32) -> PyResult<f32> {
    Ok(a - b)
}

#[pyfunction]
fn mul(a: f32, b: f32) -> PyResult<f32> {
    Ok(a * b)
}

#[pyfunction]
fn div(a: f32, b: f32) -> PyResult<f32> {
    if b == 0.0 {
        Err(MathValueError::new_err("Division by Zero"))
    } else {
        Ok(a / b)
    }
}

#[pyfunction]
fn exp(base: f32, power: f32) -> PyResult<f32> {
    Ok(base.powf(power))
}

#[pyfunction]
fn sqrt(base: f32, power: f32) -> PyResult<f32> {
    if base < 0.0 && power % 2.0 == 0.0 {
        Err(MathValueError::new_err("Negative Base for even Power"))
    } else {
        Ok(base.powf(1.0 / power))
    }
}

#[pyfunction]
fn log(base: f32, power: f32) -> PyResult<f32> {
    if base <= 0.0 {
        Err(MathValueError::new_err("Base must be greater than 0"))
    } else {
        Ok(power.log(base))
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
    m.add("MathValueError", m.py().get_type::<MathValueError>())?;
    Ok(())
}