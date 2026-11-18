# MELFA Kinematics

Proyecto de estudio, organización y modularización de un taller académico sobre transformaciones homogéneas, visualización de tramas 3D y cinemática de un robot industrial **Mitsubishi MELFA de 6 grados de libertad (GDL)**.

---

## 1. Descripción del Proyecto y Propósito

Este repositorio toma como punto de partida un notebook académico de cinemática robótica y lo organiza como un proyecto técnico en Python versionado con Git y GitHub.

El objetivo no es únicamente conservar el notebook original, sino establecer una estructura de software científico ordenada, reutilizable, reproducible y verificable mediante pruebas automatizadas.

## 2. Contexto del Robot MELFA de 6 GDL

El manipulador estudiado corresponde a un brazo industrial **Mitsubishi MELFA de 6 articulaciones rotacionales (6R)** con **muñeca esférica** (los ejes de las articulaciones $J_4, J_5, J_6$ se intersectan en el centro de muñeca).

Para describir la posición y orientación de cada eslabón y del efector final (TCP) respecto a la base $\{0\}$ en el espacio tridimensional:
* Se emplean **matrices de transformación homogénea de $4 \times 4$** pertenecientes al grupo especial euclidiano $SE(3)$.
* Se sigue la convención **Denavit–Hartenberg modificada ($\text{DH}_{\text{mod}}$, estilo Craig)** para encadenar los marcos de referencia $\{0\}, \{1\}, \dots, \{6\}, \{\text{EF}\}$.
* Se visualizan los sistemas de coordenadas locales en 3D siguiendo el código de colores estándar RGB (eje $X$ en rojo, eje $Y$ en verde, eje $Z$ en azul) y los segmentos que conectan los orígenes consecutivos.

## 3. Objetivos Académicos

El caso de estudio permite practicar y demostrar competencias en:

* Control de versiones con **Git** y trabajo colaborativo en **GitHub** (ramas y Pull Requests).
* Organización de proyectos técnicos y científicos en Python.
* Separación clara entre material exploratorio (Jupyter Notebook) y código reusable (`src/`).
* Gestión de **ambientes virtuales** (`.venv`) y registro reproducible de **dependencias** (`requirements.txt`).
* Implementación y documentación de **transformaciones homogéneas** en $SE(3)$.
* Extracción modular de herramientas de **visualización 3D** con Matplotlib.
* Verificación mediante **pruebas automatizadas** con `pytest`.
* **Uso responsable, auditable y documentado de agentes de inteligencia artificial** en tareas de programación.

## 4. Origen del Notebook

El punto de partida es el cuaderno del *Mini-taller 2 — Transformaciones homogéneas, tramas 3D y operación del robot MELFA (jog)*, el cual reúne transformaciones elementales, visualización 2D/3D, cinemática directa e inversa para mecanismos RR, PR, RP, RPR y el robot MELFA, junto con la validación numérica de cuatro objetivos de laboratorio.

El archivo original se conserva **intacto y sin modificaciones** como referencia histórica en:

```text
notebooks/00_mini_taller_original.ipynb
```

## 5. Estructura Real del Repositorio

```text
MELFA-kinematics/
│
├── README.md
├── AGENTS.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
│
├── docs/
│   ├── auditoria_inicial.md
│   ├── caso_de_estudio.md
│   ├── bitacora_ia.md
│   └── informe_final.md
│
├── notebooks/
│   └── 00_mini_taller_original.ipynb
│
├── src/
│   └── melfa_kinematics/
│       ├── __init__.py
│       ├── transforms.py
│       └── plotting.py
│
└── tests/
    ├── test_smoke.py
    └── test_plotting.py
```

### Descripción de Carpetas y Archivos Principales

* **`README.md`**: Guía general del proyecto, contexto matemático, instalación, uso y ejecución de pruebas.
* **`AGENTS.md`**: Reglas de arquitectura, convenciones matemáticas/Python y restricciones obligatorias para agentes de IA.
* **`requirements.txt` y `pyproject.toml`**: Declaración de dependencias científicas/pruebas y configuración del paquete Python.
* **`docs/`**: Documentación técnica y académica del proyecto:
  * `caso_de_estudio.md`: Justificación del diseño y evolución por etapas.
  * `auditoria_inicial.md`: Diagnóstico técnico y matriz de cumplimiento de la Fase Cero.
  * `bitacora_ia.md`: Registro transparente de las interacciones con herramientas de IA.
  * `informe_final.md`: Resumen ejecutivo, comparación Antes/Después y matriz de evaluación de los 15 puntos.
* **`notebooks/`**: Conserva intacto el cuaderno original `00_mini_taller_original.ipynb`.
* **`src/melfa_kinematics/`**: Paquete Python reusable con las transformaciones homogéneas (`transforms.py`) y la visualización 3D de tramas (`plotting.py`).
* **`tests/`**: Pruebas automatizadas con `pytest` para transformaciones (`test_smoke.py`) y visualización 3D (`test_plotting.py`).

---

## 6. Requisitos e Instalación

### 6.1 Instalación de Python
Se requiere **Python 3.10 o superior** (desarrollado y probado con Python 3.12).
* Verifica tu versión instalada ejecutando:
  ```bash
  python --version
  ```
* Si no está instalado, descárgalo desde [python.org](https://www.python.org/downloads/) asegurándote de marcar la opción *"Add Python to PATH"* en Windows.

### 6.2 Instalación de Git
Se requiere **Git** para el control de versiones:
```bash
git --version
```
Si no cuentas con Git, instálalo desde [git-scm.com](https://git-scm.com/) y configura tu identidad:
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
git config --global init.defaultBranch main
```

### 6.3 Creación y Activación del Ambiente Virtual (`.venv`)
Desde la raíz del repositorio `MELFA-kinematics`, crea el ambiente virtual aislado:

```bash
python -m venv .venv
```

Actívalo según tu sistema operativo:

* **Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
* **Windows (CMD):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```
* **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

Verifica que el intérprete activo corresponda al ambiente virtual:
```bash
python --version
python -m pip --version
```

### 6.4 Instalación de Dependencias
Con el ambiente virtual activo, instala las dependencias registradas en `requirements.txt` y el paquete en modo editable:

```bash
python -m pip install -r requirements.txt
python -m pip install --no-build-isolation --no-deps -e .
```

Puedes comprobar las bibliotecas principales instaladas con:
```bash
python -m pip show numpy matplotlib pytest
```

---

## 7. Ejecución de Pruebas Automatizadas

Desde la raíz del repositorio (con `.venv` activado), ejecuta la suite completa de pruebas con `pytest`:

```bash
python -m pytest -v
```

Las pruebas verifican automáticamente:
1. Identidades de rotación y traslación en cero (`Rx(0)`, `Ry(0)`, `Rz(0)`, `Trans(0, 0, 0)`).
2. Traslaciones espaciales (`Trans(1, 2, 3)` y `Trans(10, 20, 30)`).
3. Rotaciones conocidas de $90^\circ$ ($\pi/2\text{ rad}$) alrededor de los ejes $X, Y, Z$.
4. Invariantes de $SE(3)$: dimensión `(4, 4)`, fila homogénea `[0, 0, 0, 1]`, ortogonalidad $R^T R = I_3$ y determinante $\det(R) = 1$.
5. Generación correcta de gráficos 3D con `plot_frames_3d`, validación de dimensiones `(N, 4, 4)` e inmutabilidad de los datos de entrada.

---

## 8. Explicación de las Matrices Homogéneas en $SE(3)$

Una matriz de transformación homogénea $T \in SE(3)$ de dimensión $4 \times 4$ representa simultáneamente la orientación y la posición de un marco de referencia respecto a otro:

$$T = \begin{bmatrix} R & p \\ 0 & 1 \end{bmatrix}$$

donde $R \in SO(3)$ es la submatriz de rotación ortogonal de $3 \times 3$ y $p = [x, y, z]^T \in \mathbb{R}^3$ es el vector columna de traslación.

En `melfa_kinematics.transforms` se implementan las cuatro transformaciones elementales (con ángulos $\theta$ en **radianes**):

$$R_x(\theta) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta & 0 \\ 0 & \sin\theta & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}, \quad R_y(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta & 0 \\ 0 & 1 & 0 & 0 \\ -\sin\theta & 0 & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

$$R_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}, \quad \text{Trans}(x, y, z) = \begin{bmatrix} 1 & 0 & 0 & x \\ 0 & 1 & 0 & y \\ 0 & 0 & 1 & z \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

---

## 9. Ejemplos de Utilización

### 9.1 Uso de Transformaciones Homogéneas (`transforms.py`)

```python
import numpy as np
from melfa_kinematics.transforms import Rx, Ry, Rz, Trans

print("Rx(0):\n", Rx(0))
print("Ry(0):\n", Ry(0))
print("Rz(pi/2):\n", Rz(np.pi / 2))
print("Trans(1, 2, 3):\n", Trans(1, 2, 3))
```

### 9.2 Uso de Visualización 3D de Tramas (`plotting.py`)

La función `plot_frames_3d` recibe una secuencia o arreglo `(N, 4, 4)` de transformaciones acumuladas $T_0^i$ y dibuja en 3D cada sistema de coordenadas ($X_i$ en rojo, $Y_i$ en verde, $Z_i$ en azul) junto con los eslabones que unen orígenes consecutivos:

```python
import numpy as np
from melfa_kinematics.transforms import Rz, Trans
from melfa_kinematics.plotting import plot_frames_3d

T0 = np.eye(4)
T1 = T0 @ Rz(np.pi / 4) @ Trans(0.0, 0.0, 0.15)
T2 = T1 @ Trans(0.30, 0.0, 0.0)

frames = np.stack([T0, T1, T2], axis=0)
ax = plot_frames_3d(frames, axis_length=0.08, title="Tramas 3D de Ejemplo", show=True)
```

---

## 10. Limitaciones Conocidas

* **Alcance actual de la modularización:** En esta fase se han extraído las transformaciones elementales $SE(3)$ (`transforms.py`) y la visualización 3D de tramas (`plotting.py`). Las funciones específicas de la cadena Denavit–Hartenberg modificada (`make_chain_MELFA`) y la cinemática inversa analítica (`cinematica_inversa_MELFA`) permanecen en el notebook original para futuras iteraciones de modularización.
* **Modelo geométrico idealizado:** Los parámetros geométricos del notebook representan una aproximación académica de laboratorio con muñeca esférica ideal, sin modelar límites articulares físicos, colisiones, calibración de fábrica ni dinámica.

## 11. Uso Responsable de Inteligencia Artificial y Bitácora

Las herramientas de inteligencia artificial (incluyendo **Codex** para la extracción inicial en la rama `codex/extraer-plot-frames-3d` y **Google Antigravity con Gemini** para la auditoría, pruebas, documentación y consolidación del paquete) se han utilizado bajo supervisión humana para tareas pequeñas, delimitadas y verificables.

Todos los cambios fueron inspeccionados mediante `git diff` y validados con `pytest` antes de su integración. El registro detallado de las interacciones y decisiones técnicas se encuentra documentado en:

* `docs/bitacora_ia.md`
* `docs/auditoria_inicial.md`
* `docs/informe_final.md`

## 12. Autores

* **Daniel Cartagena** (`DCDC-afk`)
* **Julian Zambrano**
* **Edwin Vela**
