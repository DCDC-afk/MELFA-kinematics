"""Transformaciones homogéneas elementales en SE(3) para cinemática robótica.

Convenciones matemáticas:
- Todas las transformaciones se representan mediante matrices homogéneas reales de 4x4:
      T = [[R, p],
           [0, 1]]
  donde R in SO(3) es una matriz de rotación ortogonal de 3x3 y p in R^3 es el vector
  de traslación respecto al sistema de referencia previo.
- Todos los ángulos (theta) se expresan en radianes.
- Las componentes de traslación (x, y, z) se expresan en las unidades de longitud
  consistentes con el modelo geométrico del robot (metros o milímetros).
- La composición de transformaciones consecutivas se realiza mediante multiplicación
  matricial estándar (@ en NumPy), siguiendo la convención del notebook original.
"""

import numpy as np


def _validar_escalar(valor, nombre: str) -> float:
    """Valida que un parámetro sea un número real escalar y lo convierte a float."""
    if isinstance(valor, (bool, np.bool_)):
        raise TypeError(f"El parámetro '{nombre}' debe ser un número real, no booleano.")
    arr = np.asarray(valor)
    if arr.ndim != 0:
        raise ValueError(f"El parámetro '{nombre}' debe ser un escalar.")
    try:
        resultado = float(valor)
    except (TypeError, ValueError) as exc:
        raise TypeError(f"El parámetro '{nombre}' debe ser numérico.") from exc
    if not np.isfinite(resultado):
        raise ValueError(f"El parámetro '{nombre}' debe ser un número finito.")
    return resultado


def Rx(theta: float) -> np.ndarray:
    """Matriz homogénea 4x4 de rotación alrededor del eje X.

    Parámetros
    ----------
    theta : float
        Ángulo de rotación en radianes alrededor del eje X local.

    Retorna
    -------
    np.ndarray
        Matriz homogénea de dimensión (4, 4) en SE(3).
    """
    ang = _validar_escalar(theta, "theta")
    c = np.cos(ang)
    s = np.sin(ang)

    return np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0,   c,  -s, 0.0],
        [0.0,   s,   c, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ], dtype=float)


def Ry(theta: float) -> np.ndarray:
    """Matriz homogénea 4x4 de rotación alrededor del eje Y.

    Parámetros
    ----------
    theta : float
        Ángulo de rotación en radianes alrededor del eje Y local.

    Retorna
    -------
    np.ndarray
        Matriz homogénea de dimensión (4, 4) en SE(3).
    """
    ang = _validar_escalar(theta, "theta")
    c = np.cos(ang)
    s = np.sin(ang)

    return np.array([
        [  c, 0.0,   s, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [ -s, 0.0,   c, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ], dtype=float)


def Rz(theta: float) -> np.ndarray:
    """Matriz homogénea 4x4 de rotación alrededor del eje Z.

    Parámetros
    ----------
    theta : float
        Ángulo de rotación en radianes alrededor del eje Z local.

    Retorna
    -------
    np.ndarray
        Matriz homogénea de dimensión (4, 4) en SE(3).
    """
    ang = _validar_escalar(theta, "theta")
    c = np.cos(ang)
    s = np.sin(ang)

    return np.array([
        [  c,  -s, 0.0, 0.0],
        [  s,   c, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ], dtype=float)


def Trans(x: float = 0.0, y: float = 0.0, z: float = 0.0) -> np.ndarray:
    """Matriz homogénea 4x4 de traslación pura en el espacio 3D.

    Parámetros
    ----------
    x : float, opcional
        Desplazamiento a lo largo del eje X (por defecto 0.0).
    y : float, opcional
        Desplazamiento a lo largo del eje Y (por defecto 0.0).
    z : float, opcional
        Desplazamiento a lo largo del eje Z (por defecto 0.0).

    Retorna
    -------
    np.ndarray
        Matriz homogénea de dimensión (4, 4) en SE(3).
    """
    tx = _validar_escalar(x, "x")
    ty = _validar_escalar(y, "y")
    tz = _validar_escalar(z, "z")

    return np.array([
        [1.0, 0.0, 0.0,  tx],
        [0.0, 1.0, 0.0,  ty],
        [0.0, 0.0, 1.0,  tz],
        [0.0, 0.0, 0.0, 1.0],
    ], dtype=float)
