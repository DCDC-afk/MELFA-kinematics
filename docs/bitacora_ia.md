# Bitácora de uso de inteligencia artificial

Este documento registra con transparencia las interacciones con herramientas de inteligencia artificial durante el desarrollo y consolidación del proyecto `MELFA-kinematics`, diferenciando explícitamente el trabajo realizado previamente con **Codex** del trabajo de auditoría, pruebas, documentación y consolidación realizado con **Google Antigravity (Gemini)**.

---

## Interacción 1: Extracción inicial de visualización 3D (Rama `codex/extraer-plot-frames-3d`)
- **Fecha:** 2026-09-14
- **Herramienta:** Codex (flujo de rama `codex/extraer-plot-frames-3d` en GitHub)
- **Modelo:** Codex
- **Objetivo:** Extraer la función `plot_frames_3d` desde `notebooks/00_mini_taller_original.ipynb` hacia un módulo independiente `src/melfa_kinematics/plotting.py` sin alterar el notebook original ni la matemática de las transformaciones.
- **Prompt resumido:** Extraer `plot_frames_3d` del notebook original al módulo de visualización `src/melfa_kinematics/plotting.py` y registrar `matplotlib` en `requirements.txt`.
- **Archivos modificados:**
  - `src/melfa_kinematics/plotting.py` (creado, 85 líneas)
  - `requirements.txt` (actualizado con `matplotlib==3.11.2`)
- **Cambios aceptados:**
  - Implementación de `plot_frames_3d` en `src/melfa_kinematics/plotting.py` respetando la firma, los colores RGB (`r`, `g`, `b`), el trazado de eslabones y el ajuste cúbico de límites.
- **Cambios rechazados / Observaciones posteriores:**
  - En ese commit (`3f750d8`), `requirements.txt` conservó la codificación binaria UTF-16 LE proveniente de PowerShell y no se incluyeron pruebas unitarias automatizadas para `plotting.py` ni exportación en `__init__.py`. Estos aspectos fueron detectados en la auditoría y corregidos en la interacción de consolidación.
- **Pruebas realizadas:** Revisión del diff e integración mediante Pull Request.
- **Commit asociado:** `3f750d8` (`Extraer plot_frames_3d a módulo de visualización`) y merge commit `b518f1b`.
- **Pull Request:** PR #1 (`DCDC-afk/codex/extraer-plot-frames-3d` -> `main`) en `https://github.com/DCDC-afk/MELFA-kinematics/pull/1`.

---

## Interacción 2: Auditoría integral del repositorio (Fase Cero)
- **Fecha:** 2026-11-18
- **Herramienta:** Google Antigravity
- **Modelo:** Gemini (High Reasoning)
- **Objetivo:** Inspeccionar todos los archivos existentes, el historial de Git, el entorno virtual `.venv`, el notebook original y el estado de las pruebas respecto a los requisitos de las tres etapas (15 puntos), sin modificar archivos del proyecto.
- **Prompt resumido:** Ejecutar exclusivamente la Fase Cero (Auditoría) inspeccionando archivos, historial Git y notebook original; generar `docs/auditoria_inicial.md` con matriz de cumplimiento, comparación de estado actual vs. objetivo y plan de ejecución por bloques.
- **Resultado:**
  - Se detectó que `requirements.txt` estaba codificado en UTF-16 LE con BOM (`\xff\xfe`), siendo tratado como binario por Git.
  - Se identificó que ejecutar `pytest` directamente fallaba con `ModuleNotFoundError: No module named 'src'` y emitía warnings por `.pytest_cache/` (no incluido en `.gitignore`).
  - Se comprobó que `src/melfa_kinematics/__init__.py` estaba vacío (`0` bytes) y que no existían pruebas automatizadas para `plotting.py`, ni los archivos `AGENTS.md`, `docs/bitacora_ia.md` y `docs/informe_final.md`.
  - Se verificó que `notebooks/00_mini_taller_original.ipynb` es un JSON válido de 45 celdas y se encontraba intacto.
- **Cambios aceptados:** Creación de `docs/auditoria_inicial.md`.
- **Cambios rechazados:** Ninguno.
- **Verificación:** Comprobación mediante `git status`, `git log --oneline -10`, `git remote -v` y lectura completa de celdas del notebook.

---

## Interacción 3: Modularización, configuración de paquete, pruebas automatizadas y documentación
- **Fecha:** 2026-11-18
- **Herramienta:** Google Antigravity
- **Modelo:** Gemini (High Reasoning)
- **Objetivo:** Completar los entregables faltantes de las Etapas 1, 2 y 3 respetando el trabajo previo: crear `AGENTS.md`, actualizar `README.md` y `docs/caso_de_estudio.md`, normalizar `requirements.txt` a UTF-8, completar `.gitignore`, configurar `pyproject.toml`, documentar y exportar `transforms.py` y `plotting.py` en `__init__.py`, y ampliar la suite de pruebas (`tests/test_smoke.py` y `tests/test_plotting.py`).
- **Prompt resumido:** Ejecutar los bloques autorizados de la Instrucción Maestra preservando intacto el notebook original y el historial Git, verificando cada bloque con `python -m pytest -v`.
- **Archivos modificados y creados:**
  - Creados: `AGENTS.md`, `pyproject.toml`, `tests/test_plotting.py`, `docs/auditoria_inicial.md`, `docs/bitacora_ia.md`, `docs/informe_final.md`.
  - Modificados: `README.md`, `.gitignore`, `requirements.txt`, `docs/caso_de_estudio.md`, `src/melfa_kinematics/__init__.py`, `src/melfa_kinematics/transforms.py`, `src/melfa_kinematics/plotting.py`, `tests/test_smoke.py`.
- **Cambios aceptados:**
  - Conversión de `requirements.txt` a UTF-8 para permitir diffs legibles en Git.
  - Configuración de `pyproject.toml` para que `melfa_kinematics` sea importable sin manipulaciones manuales de `sys.path`.
  - Ampliación de `tests/test_smoke.py` a 13 pruebas unitarias parametrizadas (identidades, traslaciones, rotaciones de $90^\circ$ en $X, Y, Z$, forma `(4, 4)`, fila `[0, 0, 0, 1]`, ortogonalidad $R^T R = I_3$, $\det(R) = 1$ y validación de entradas).
  - Creación de `tests/test_plotting.py` con 4 pruebas automatizadas usando backend no interactivo `Agg` (`show=False`).
- **Cambios rechazados:**
  - Se descartó modificar `notebooks/00_mini_taller_original.ipynb` a pesar de detectar detalles menores en sus textos/docstrings internos, cumpliendo la regla estricta de preservación del material original.
- **Pruebas realizadas:**
  - `.\.venv\Scripts\python.exe -m pytest -v` -> **17 passed in 1.36s** (`13` en `test_smoke.py` y `4` en `test_plotting.py`).
  - `.\.venv\Scripts\pytest.exe -v` -> **17 passed**.
  - `git diff notebooks/00_mini_taller_original.ipynb` -> Vacío (0 cambios en el notebook original).
- **Commit asociado:** `df687fa` (`docs: establish project guidelines and repository audit`), `955dbe0` (`feat: implement homogeneous transforms and smoke tests`) y commit de cierre en `feature/melfa-project-completion`.
- **Pull Request:** PR #1 histórico (`https://github.com/DCDC-afk/MELFA-kinematics/pull/1`) y rama de cierre lista para PR de consolidación.

---

## Reflexión final

### 1. Qué parte del código entiendo completamente
* La formulación y estructura de las matrices de transformación homogénea de $4 \times 4$ en $SE(3)$ (`Rx`, `Ry`, `Rz`, `Trans`), donde la submatriz superior izquierda de $3 \times 3$ representa una rotación ortogonal en $SO(3)$ y la cuarta columna contiene el vector de traslación $[x, y, z, 1]^T$.
* La lógica de `plot_frames_3d`: cómo extrae los orígenes (`T_arr[:, :3, 3]`) y los vectores directores de los ejes locales $X, Y, Z$ (columnas 0, 1 y 2 de la submatriz de rotación) para graficarlos con `ax.quiver` y unir los eslabones consecutivos.
* Las pruebas unitarias en `pytest` utilizando `np.allclose` para comparar arreglos de punto flotante con tolerancia numérica.

### 2. Qué parte necesito estudiar con mayor profundidad
* El desacoplamiento cinemático completo para la cinemática inversa analítica del robot MELFA de 6 GDL con muñeca esférica (`resolver_posicion` y `resolver_orientacion` mediante la matriz $R_3^6 = (R_0^3)^T R_0^6$), especialmente el manejo de múltiples configuraciones (codo arriba / codo abajo, muñeca invertida) y las singularidades cuando $\sin(q_5) \approx 0$ (*gimbal lock*).

### 3. Qué errores o problemas detectó la revisión humana y la auditoría
* Que el archivo `requirements.txt` generado en PowerShell tenía codificación UTF-16 LE con BOM, haciendo que Git lo tratara como binario (`Binary files differ`) e impidiendo auditar cambios de paquetes en los diffs.
* Que las pruebas iniciales en `tests/test_smoke.py` dependían de `from src.melfa_kinematics...` sin configuración de paquete, fallando al invocar `pytest` directamente.
* Que el módulo `plotting.py` extraído en el primer PR carecía de pruebas automatizadas y no estaba exportado en `src/melfa_kinematics/__init__.py`.
* Que `docs/caso_de_estudio.md` contenía atributos residuales (`id="..."`) en los bloques de código y que tanto `README.md` como `caso_de_estudio.md` seguían describiendo el proyecto como si estuviera en la Etapa 1.

### 4. Qué riesgos habría tenido aceptar los cambios sin verificar
* Confiar en que "el código existe" sin ejecutar `pytest` habría dejado oculto el `ModuleNotFoundError` al correr `pytest` directamente.
* No revisar `git diff` habría mantenido `requirements.txt` como archivo binario ilegible en el repositorio.
* No verificar la integridad del notebook original podría haber sobrescrito metadatos o salidas académicas de referencia.

### 5. Qué aprendí sobre el uso responsable de IA
* Los agentes de IA son altamente efectivos cuando operan sobre tareas pequeñas, acotadas y gobernadas por reglas explícitas (`AGENTS.md`), pero todo cambio propuesto debe validarse con tres filtros humanos indispensables: **inspección de `git diff`**, **ejecución real de pruebas automatizadas (`pytest -v`)** y **trazabilidad honesta de qué herramienta hizo cada cambio**.
