"""Utilidades de visualización para marcos de referencia 3D."""

import matplotlib.pyplot as plt
import numpy as np


def plot_frames_3d(T_list, axis_length=0.1, link_tol=1e-12, ax=None, show=True, title=None):
    """
    Dibuja tramas 3D a partir de una lista/array (N,4,4) de matrices homogéneas (SE(3)).
    - Eje X (rojo), Y (verde), Z (azul) con etiquetas Xi, Yi, Zi en la punta.
    - Segmentos negros entre orígenes consecutivos (eslabones) si hay traslación.
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
