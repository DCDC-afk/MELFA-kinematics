import numpy as np

from src.melfa_kinematics.transforms import Rx, Ry, Rz, Trans


def test_rotaciones_identidad():
    identidad = np.eye(4)

    assert np.allclose(Rx(0), identidad)
    assert np.allclose(Ry(0), identidad)
    assert np.allclose(Rz(0), identidad)

def test_traslacion():
    T = Trans(10, 20, 30)

    esperado = np.array([
        [1, 0, 0, 10],
        [0, 1, 0, 20],
        [0, 0, 1, 30],
        [0, 0, 0, 1]
    ])

    assert np.allclose(T, esperado)

def test_rz_90_grados():
    esperado = np.array([
        [0, -1, 0, 0],
        [1,  0, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])

    assert np.allclose(Rz(np.pi / 2), esperado)