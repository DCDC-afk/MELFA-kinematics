"""Pruebas automatizadas (smoke y propiedades SE(3)) para melfa_kinematics.transforms."""

import numpy as np
import pytest

from melfa_kinematics.transforms import Rx, Ry, Rz, Trans


def test_rotaciones_identidad():
    """Rx(0), Ry(0) y Rz(0) deben ser iguales a la matriz identidad 4x4."""
    identidad = np.eye(4)

    assert np.allclose(Rx(0), identidad)
    assert np.allclose(Ry(0), identidad)
    assert np.allclose(Rz(0), identidad)


def test_traslacion_identidad():
    """Trans(0, 0, 0) y Trans() sin argumentos deben producir la identidad 4x4."""
    identidad = np.eye(4)

    assert np.allclose(Trans(0, 0, 0), identidad)
    assert np.allclose(Trans(), identidad)


def test_traslacion():
    """Trans(1, 2, 3) y Trans(10, 20, 30) deben colocar el vector en la cuarta columna."""
    T_123 = Trans(1, 2, 3)
    esperado_123 = np.array([
        [1.0, 0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0, 2.0],
        [0.0, 0.0, 1.0, 3.0],
        [0.0, 0.0, 0.0, 1.0],
    ])
    assert np.allclose(T_123, esperado_123)

    T_102030 = Trans(10, 20, 30)
    esperado_102030 = np.array([
        [1.0, 0.0, 0.0, 10.0],
        [0.0, 1.0, 0.0, 20.0],
        [0.0, 0.0, 1.0, 30.0],
        [0.0, 0.0, 0.0, 1.0],
    ])
    assert np.allclose(T_102030, esperado_102030)


def test_rz_90_grados():
    """Rz(pi/2) debe corresponder a una rotación de 90 grados alrededor de Z."""
    esperado = np.array([
        [0.0, -1.0, 0.0, 0.0],
        [1.0,  0.0, 0.0, 0.0],
        [0.0,  0.0, 1.0, 0.0],
        [0.0,  0.0, 0.0, 1.0],
    ])

    assert np.allclose(Rz(np.pi / 2), esperado)


def test_rx_ry_90_grados():
    """Rx(pi/2) y Ry(pi/2) deben corresponder a rotaciones de 90 grados en X e Y."""
    esperado_rx = np.array([
        [1.0, 0.0,  0.0, 0.0],
        [0.0, 0.0, -1.0, 0.0],
        [0.0, 1.0,  0.0, 0.0],
        [0.0, 0.0,  0.0, 1.0],
    ])
    esperado_ry = np.array([
        [ 0.0, 0.0, 1.0, 0.0],
        [ 0.0, 1.0, 0.0, 0.0],
        [-1.0, 0.0, 0.0, 0.0],
        [ 0.0, 0.0, 0.0, 1.0],
    ])

    assert np.allclose(Rx(np.pi / 2), esperado_rx)
    assert np.allclose(Ry(np.pi / 2), esperado_ry)


def test_forma_y_ultima_fila_homogenea():
    """Todas las matrices deben tener forma (4, 4) y última fila [0, 0, 0, 1]."""
    matrices = [
        Rx(0.35),
        Ry(-0.72),
        Rz(1.25),
        Trans(4.5, -2.0, 8.1),
    ]
    fila_homogenea = np.array([0.0, 0.0, 0.0, 1.0])

    for M in matrices:
        assert M.shape == (4, 4)
        assert np.allclose(M[3, :], fila_homogenea)


@pytest.mark.parametrize("angulo", [-np.pi, -0.85, 0.0, 0.42, np.pi / 3, np.pi])
def test_ortogonalidad_y_determinante_rotaciones(angulo):
    """La submatriz de rotación 3x3 debe ser ortogonal (R^T R = I) y tener det(R) = 1."""
    identidad_3 = np.eye(3)

    for func in (Rx, Ry, Rz):
        T = func(angulo)
        R = T[:3, :3]
        assert np.allclose(R.T @ R, identidad_3)
        assert np.allclose(R @ R.T, identidad_3)
        assert np.isclose(np.linalg.det(R), 1.0)
        assert np.allclose(T[:3, 3], np.zeros(3))


def test_validacion_entradas_invalidas():
    """Las funciones deben rechazar entradas no escalares o no numéricas."""
    with pytest.raises((TypeError, ValueError)):
        Rx([0.1, 0.2])

    with pytest.raises(TypeError):
        Rz("noventa")

    with pytest.raises(ValueError):
        Trans(np.nan, 0.0, 0.0)
