import numpy as np


def Rx(theta):
    """Matriz homogénea de rotación alrededor del eje X."""
    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s,  c, 0],
        [0, 0, 0, 1]
    ])


def Ry(theta):
    """Matriz homogénea de rotación alrededor del eje Y."""
    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([
        [ c, 0, s, 0],
        [ 0, 1, 0, 0],
        [-s, 0, c, 0],
        [ 0, 0, 0, 1]
    ])


def Rz(theta):
    """Matriz homogénea de rotación alrededor del eje Z."""
    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])


def Trans(x, y, z):
    """Matriz homogénea de traslación."""
    return np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])