"""Pruebas automatizadas para la visualización 3D de tramas (melfa_kinematics.plotting)."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pytest

from melfa_kinematics.plotting import plot_frames_3d
from melfa_kinematics.transforms import Rx, Ry, Rz, Trans


@pytest.fixture(autouse=True)
def cerrar_figuras():
    """Cierra todas las figuras de Matplotlib después de cada prueba."""
    yield
    plt.close("all")


def test_plot_frames_3d_valida_dimensiones():
    """Debe lanzar ValueError cuando la entrada no tiene forma (N, 4, 4)."""
    with pytest.raises(ValueError, match=r"\(N,4,4\)"):
        plot_frames_3d(np.eye(4), show=False)

    with pytest.raises(ValueError, match=r"\(N,4,4\)"):
        plot_frames_3d(np.zeros((2, 3, 3)), show=False)


def test_plot_frames_3d_genera_ejes_etiquetas_y_eslabones():
    """Verifica que se generen las etiquetas RGB, los ejes X/Y/Z y los eslabones esperados."""
    T0 = np.eye(4)
    T1 = T0 @ Trans(0.0, 0.0, 0.15) @ Rz(np.pi / 2)
    T2 = T1 @ Trans(0.30, 0.0, 0.0) @ Ry(-np.pi / 4)
    frames = np.stack([T0, T1, T2], axis=0)

    ax = plot_frames_3d(frames, axis_length=0.08, show=False, title="Cadena MELFA Prueba")

    assert ax.name == "3d"
    assert ax.get_title() == "Cadena MELFA Prueba"
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"
    assert ax.get_zlabel() == "Z"

    # 3 tramas -> 9 etiquetas de texto: X0, Y0, Z0, X1, Y1, Z1, X2, Y2, Z2
    textos = {t.get_text(): t.get_color() for t in ax.texts}
    for i in range(3):
        assert textos.get(f"X{i}") == "r"
        assert textos.get(f"Y{i}") == "g"
        assert textos.get(f"Z{i}") == "b"

    # Hay traslación entre T0->T1 (0.15 m) y T1->T2 (0.30 m), por lo que deben trazarse 2 segmentos negros
    assert len(ax.lines) == 2


def test_plot_frames_3d_no_modifica_datos_entrada():
    """Garantiza que la función de visualización no mute el arreglo de transformaciones de entrada."""
    T0 = np.eye(4)
    T1 = Trans(1.0, 2.0, 3.0) @ Rx(np.pi / 3)
    frames = np.stack([T0, T1], axis=0)
    copia_original = frames.copy()

    plot_frames_3d(frames, axis_length=0.1, show=False)

    assert np.array_equal(frames, copia_original)


def test_plot_frames_3d_sin_eslabon_en_rotacion_pura_y_ax_existente():
    """Si dos tramas comparten el mismo origen, no debe dibujar segmento de eslabón; debe reutilizar ax."""
    T0 = np.eye(4)
    T1 = Rz(np.pi / 4)  # Mismo origen (0, 0, 0)
    frames = [T0, T1]

    fig = plt.figure()
    custom_ax = fig.add_subplot(111, projection="3d")

    returned_ax = plot_frames_3d(frames, axis_length=0.1, ax=custom_ax, show=False)

    assert returned_ax is custom_ax
    assert len(returned_ax.lines) == 0
    assert len(returned_ax.texts) == 6
