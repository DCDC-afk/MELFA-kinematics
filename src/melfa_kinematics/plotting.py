"""Utilidades de visualización para marcos de referencia 3D en SE(3)."""

from typing import Any, Optional, Sequence, Union

import matplotlib.pyplot as plt
import numpy as np


def plot_frames_3d(
    T_list: Union[np.ndarray, Sequence[np.ndarray]],
    axis_length: float = 0.1,
    link_tol: float = 1e-12,
    ax: Optional[Any] = None,
    show: bool = True,
    title: Optional[str] = None,
) -> Any:
    """Dibuja tramas 3D a partir de una lista o arreglo (N, 4, 4) de matrices homogéneas SE(3).

    Características visuales:
    - Eje X (rojo), Y (verde), Z (azul) con etiquetas Xi, Yi, Zi en la punta de cada eje.
    - Segmentos negros entre orígenes consecutivos (eslabones) cuando la distancia supera `link_tol`.
    - Ajuste automático de límites espaciales con proporción cúbica (1:1:1).

    Parámetros
    ----------
    T_list : array_like de forma (N, 4, 4)
        Secuencia o arreglo NumPy con N matrices de transformación homogénea 4x4.
    axis_length : float, opcional
        Longitud visual de las flechas de los ejes coordenados locales (por defecto 0.1).
    link_tol : float, opcional
        Distancia mínima entre orígenes consecutivos para trazar un segmento de eslabón (por defecto 1e-12).
    ax : Axes3D, opcional
        Ejes 3D de Matplotlib existentes donde dibujar. Si es `None`, se crea una nueva figura.
    show : bool, opcional
        Si es `True` y se creó una figura nueva, invoca `plt.show()` (por defecto `True`).
    title : str, opcional
        Título opcional para el gráfico 3D.

    Retorna
    -------
    Axes3D
        Objeto de ejes 3D de Matplotlib con las tramas y eslabones representados.

    Ejemplo
    -------
    >>> import numpy as np
    >>> from melfa_kinematics.transforms import Rz, Trans
    >>> from melfa_kinematics.plotting import plot_frames_3d
    >>> frames = np.stack([np.eye(4), Trans(0, 0, 0.15) @ Rz(np.pi / 4)], axis=0)
    >>> ax = plot_frames_3d(frames, axis_length=0.05, show=False, title="Ejemplo")
    """
    T_arr = np.asarray(T_list)
    if T_arr.ndim != 3 or T_arr.shape[1:] != (4, 4):
        raise ValueError("T_list debe ser de forma (N,4,4).")

    created_ax = False
    if ax is None:
        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(111, projection="3d")
        created_ax = True

    # Origen y ejes locales
    origins = T_arr[:, :3, 3]  # (N, 3)
    x_dirs = T_arr[:, :3, 0]  # (N, 3) eje X local
    y_dirs = T_arr[:, :3, 1]  # (N, 3) eje Y local
    z_dirs = T_arr[:, :3, 2]  # (N, 3) eje Z local

    # Dibujar ejes y etiquetas
    for i in range(T_arr.shape[0]):
        ox, oy, oz = origins[i]
        dx, dy, dz = axis_length * x_dirs[i]
        ux, uy, uz = axis_length * y_dirs[i]
        wx, wy, wz = axis_length * z_dirs[i]

        ax.quiver(ox, oy, oz, dx, dy, dz, length=1.0, normalize=False, color="r")
        ax.text(ox + dx, oy + dy, oz + dz, f"X{i}", color="r", fontsize=9)

        ax.quiver(ox, oy, oz, ux, uy, uz, length=1.0, normalize=False, color="g")
        ax.text(ox + ux, oy + uy, oz + uz, f"Y{i}", color="g", fontsize=9)

        ax.quiver(ox, oy, oz, wx, wy, wz, length=1.0, normalize=False, color="b")
        ax.text(ox + wx, oy + wy, oz + wz, f"Z{i}", color="b", fontsize=9)

    # Eslabones (segmentos negros entre orígenes)
    for i in range(1, origins.shape[0]):
        p0 = origins[i - 1]
        p1 = origins[i]
        if np.linalg.norm(p1 - p0) > link_tol:
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]], [p0[2], p1[2]], "k-")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Encajar límites alrededor de todas las puntas y orígenes
    all_pts = np.vstack([
        origins,
        origins + axis_length * x_dirs,
        origins + axis_length * y_dirs,
        origins + axis_length * z_dirs,
    ])
    mins = all_pts.min(axis=0)
    maxs = all_pts.max(axis=0)
    center = (mins + maxs) / 2.0
    span = (maxs - mins).max()
    if span <= 0:
        span = axis_length * 2
    margin = 0.2 * span
    ax.set_xlim(center[0] - span / 2 - margin, center[0] + span / 2 + margin)
    ax.set_ylim(center[1] - span / 2 - margin, center[1] + span / 2 + margin)
    ax.set_zlim(center[2] - span / 2 - margin, center[2] + span / 2 + margin)

    # Aspecto cúbico
    try:
        ax.set_box_aspect((1, 1, 1))
    except Exception:
        pass

    if title:
        ax.set_title(title)

    if created_ax and show:
        plt.show()
    return ax
