# Informe Final del Proyecto — `MELFA-kinematics`

**Repositorio:** `https://github.com/DCDC-afk/MELFA-kinematics`  
**Autores del taller original:** Daniel Cartagena, Julian Zambrano, Edwin Vela  
**Fecha del informe:** 2026-11-18

---

## 1. Resumen Ejecutivo

El proyecto **MELFA-kinematics** completó la transición desde un cuaderno exploratorio de Jupyter (*Mini-taller 2 — Transformaciones homogéneas, tramas 3D y operación del robot MELFA*) hacia un repositorio de software científico en Python estructurado, documentado, reproducible y verificado mediante pruebas automatizadas con `pytest`.

Se preservaron íntegramente el notebook original (`notebooks/00_mini_taller_original.ipynb`) y el historial de commits de las tres etapas académicas, completando la documentación técnica (`README.md`, `AGENTS.md`, `docs/caso_de_estudio.md`, `docs/auditoria_inicial.md`, `docs/bitacora_ia.md`), corrigiendo la codificación de `requirements.txt` a UTF-8, habilitando la instalación e importación limpia del paquete `melfa_kinematics` mediante `pyproject.toml`, y alcanzando **17 pruebas automatizadas aprobadas al 100%** tanto para las transformaciones homogéneas (`transforms.py`) como para la visualización 3D de tramas (`plotting.py`).

---

## 2. Estado Inicial del Proyecto (Fase Cero)

Al iniciar la auditoría (Fase Cero), el repositorio contaba con 5 commits y un primer Pull Request fusionado (`b518f1b`), pero presentaba brechas importantes respecto a los requisitos de los 15 puntos:

* **Documentación incompleta o desfasada:** No existían `AGENTS.md`, `docs/auditoria_inicial.md`, `docs/bitacora_ia.md` ni `docs/informe_final.md`. Tanto `README.md` como `docs/caso_de_estudio.md` describían el proyecto como si continuara en la Etapa 1, y `docs/caso_de_estudio.md` tenía atributos residuales `id="..."` en bloques Markdown.
* **Problemas de entorno y configuración:** `requirements.txt` estaba codificado en **UTF-16 LE con BOM**, por lo que Git lo trataba como archivo binario (`Binary files differ`). `.gitignore` no excluía `.pytest_cache/` ni `.ipynb_checkpoints/`.
* **Paquete y pruebas incompletos:** `src/melfa_kinematics/__init__.py` estaba vacío (`0` bytes). Invocar `pytest` directamente fallaba con `ModuleNotFoundError: No module named 'src'`. Solo existían 3 pruebas básicas en `tests/test_smoke.py` y **0 pruebas automatizadas** para `src/melfa_kinematics/plotting.py`.

---

## 3. Estado Final del Proyecto

En su estado final, el repositorio cuenta con:
* Documentación completa, coherente y alineada con el árbol real del proyecto.
* Reglas explícitas de arquitectura y gobernanza para agentes de IA en `AGENTS.md`.
* Entorno virtual `.venv` con Python 3.12.10, `requirements.txt` en texto plano UTF-8, `.gitignore` completo y `pyproject.toml` configurado.
* Paquete `melfa_kinematics` con interfaz pública limpia en `__init__.py`, transformaciones homogéneas documentadas y validadas en `transforms.py`, y visualización 3D tipada y documentada en `plotting.py`.
* Suite de **17 pruebas automatizadas** (`tests/test_smoke.py` y `tests/test_plotting.py`) que pasan al 100% sin errores ni advertencias.
* Trazabilidad completa y honesta del uso de inteligencia artificial en `docs/bitacora_ia.md`.

---

## 4. Comparación de Estructura Inicial y Final

### Estructura Inicial Encontrada
```text
MELFA-kinematics/
├── .gitignore
├── README.md
├── requirements.txt                         # Binario UTF-16 LE
├── docs/
│   └── caso_de_estudio.md
├── notebooks/
│   └── 00_mini_taller_original.ipynb
├── src/
│   └── melfa_kinematics/
│       ├── __init__.py                      # Vacío (0 bytes)
│       ├── plotting.py
│       └── transforms.py
└── tests/
    └── test_smoke.py                        # 3 pruebas (fallaba con `pytest` directo)
```

### Estructura Final consolidada
```text
MELFA-kinematics/
├── .gitignore                               # Completo (.venv, __pycache__, .pytest_cache, .ipynb_checkpoints)
├── AGENTS.md                                # Reglas técnicas y restricciones para agentes de IA
├── README.md                                # Documentación integral (19 secciones/puntos)
├── pyproject.toml                           # Configuración de paquete editable y pytest
├── requirements.txt                         # UTF-8 texto plano legible en git diff
├── docs/
│   ├── auditoria_inicial.md                 # Diagnóstico de Fase Cero y matriz inicial
│   ├── bitacora_ia.md                       # Registro trazable de Codex y Antigravity/Gemini
│   ├── caso_de_estudio.md                   # Caso de estudio actualizado a las 3 etapas
│   └── informe_final.md                     # Informe ejecutivo final y matriz de 15 puntos
├── notebooks/
│   └── 00_mini_taller_original.ipynb        # Preservado 100% intacto
├── src/
│   └── melfa_kinematics/
│       ├── __init__.py                      # Exporta Rx, Ry, Rz, Trans, plot_frames_3d
│       ├── plotting.py                      # Visualización 3D documentada y tipada
│       └── transforms.py                    # Transformaciones SE(3) documentadas y validadas
└── tests/
    ├── test_plotting.py                     # 4 pruebas automatizadas (backend Agg, show=False)
    └── test_smoke.py                        # 13 pruebas unitarias y de invariantes SE(3)
```

### Tabla Comparativa Sintética (Antes vs. Después)

| Aspecto | Antes (Estado Inicial Verificado) | Después (Estado Final Verificado) |
| :--- | :--- | :--- |
| **Organización** | Estructura inicial incompleta (sin `AGENTS.md`, `pyproject.toml`, `bitacora_ia.md` ni `informe_final.md`). | Proyecto modular completo con separación clara entre `notebooks/`, `src/`, `tests/` y `docs/`. |
| **Código reusable** | `transforms.py` y `plotting.py` presentes, pero `__init__.py` vacío (`0` bytes) y sin configuración de paquete instalable. | Paquete `melfa_kinematics` importable limpiamente (`Rx`, `Ry`, `Rz`, `Trans`, `plot_frames_3d`), con docstrings, validación y tipado. |
| **Ambiente** | `.venv` local existente (Python 3.12.10), pero `.pytest_cache/` no ignorado y con conflicto de permisos. | `.venv` verificado, paquete registrado en `.venv` y `pytest` configurado en `pyproject.toml` sin conflictos de caché. |
| **Dependencias** | `requirements.txt` codificado en UTF-16 LE con BOM (tratado como archivo binario por Git). | `requirements.txt` en UTF-8 estándar, verificable en `git diff` y reproducible con `pip install -r requirements.txt`. |
| **Pruebas** | 3 pruebas básicas en `test_smoke.py`; fallaba al ejecutar `pytest` directo (`ModuleNotFoundError`); 0 pruebas para `plotting.py`. | **17 pruebas automatizadas** (`13` en `test_smoke.py` + `4` en `test_plotting.py`) aprobadas en `1.36s` tanto con `python -m pytest -v` como con `pytest -v`. |
| **Visualización** | `plot_frames_3d` extraída en `plotting.py` sin pruebas automatizadas. | `plot_frames_3d` documentada, exportada en el paquete y verificada con backend no interactivo `Agg`. |
| **IA** | Rama `codex/extraer-plot-frames-3d` sin bitácora ni directrices `AGENTS.md`. | Gobernanza en `AGENTS.md` y trazabilidad completa en `docs/bitacora_ia.md` diferenciando Codex y Antigravity/Gemini. |
| **GitHub** | Repositorio con 5 commits y PR #1 integrado; documentación desactualizada en Etapa 1. | Historial preservado, documentación sincronizada con las 3 etapas y cambios listos para commit/PR revisable. |

---

## 5. Cambios Implementados

1. **Auditoría inicial (Fase Cero):** Diagnóstico exhaustivo del repositorio y creación de `docs/auditoria_inicial.md`.
2. **Gobernanza y documentación (Etapa 1):**
   * Creación de `AGENTS.md` con convenciones de Python, convenciones matemáticas $SE(3)$, protección del notebook original y las 9 restricciones obligatorias para agentes de IA.
   * Ampliación de `README.md` con contexto del robot MELFA de 6 GDL, árbol real del repositorio, guía paso a paso de Python, Git, `.venv`, dependencias, `pytest`, explicación matemática de matrices $4 \times 4$, ejemplos ejecutables de transformaciones y visualización 3D, limitaciones y autores.
3. **Saneamiento de entorno y configuración (Etapa 2):**
   * Conversión de `requirements.txt` de UTF-16 LE (binario) a UTF-8 estándar.
   * Ampliación de `.gitignore` con `.ipynb_checkpoints/`, `.pytest_cache/`, `*.egg-info/`, `build/`, `dist/`.
   * Creación de `pyproject.toml` para definir el paquete `melfa-kinematics` en `src/` y configurar `pytest`.
4. **Consolidación de `melfa_kinematics` y pruebas (Etapas 2 y 3):**
   * Documentación detallada y validación de entradas escalares en `src/melfa_kinematics/transforms.py`, incluyendo valores por defecto `Trans(x=0.0, y=0.0, z=0.0)`.
   * Exportación de `Rx`, `Ry`, `Rz`, `Trans` y `plot_frames_3d` en `src/melfa_kinematics/__init__.py`.
   * Ampliación de `tests/test_smoke.py` de 3 a 13 pruebas unitarias.
   * Documentación y anotaciones de tipos en `src/melfa_kinematics/plotting.py` y creación de `tests/test_plotting.py` con 4 pruebas automatizadas sobre backend `Agg`.
   * Actualización de `docs/caso_de_estudio.md` y creación de `docs/bitacora_ia.md` y `docs/informe_final.md`.

---

## 6. Archivos Creados

* `AGENTS.md`
* `pyproject.toml`
* `tests/test_plotting.py`
* `docs/auditoria_inicial.md`
* `docs/bitacora_ia.md`
* `docs/informe_final.md`

---

## 7. Archivos Modificados

* `README.md`
* `.gitignore`
* `requirements.txt`
* `docs/caso_de_estudio.md`
* `src/melfa_kinematics/__init__.py`
* `src/melfa_kinematics/transforms.py`
* `src/melfa_kinematics/plotting.py`
* `tests/test_smoke.py`

---

## 8. Archivos Preservados Intactos

* **`notebooks/00_mini_taller_original.ipynb`**: Verificado mediante `git diff notebooks/00_mini_taller_original.ipynb` (0 líneas modificadas; conserva exactamente sus 2719 líneas y 45 celdas originales).
* **Historial de commits previos (`e1bb7f0`, `bae7e3e`, `6b0f6ce`, `3f750d8`, `b518f1b`)**: Intacto, sin reescritura de historial.

---

## 9. Ambiente y Dependencias Verificadas

* **Sistema Operativo:** Windows (`win32`)
* **Intérprete del ambiente virtual (`.venv`):** `Python 3.12.10`
* **Gestor de paquetes:** `pip 25.0.1`
* **Dependencias principales verificadas (`python -m pip show`):**
  * `numpy==2.5.3`
  * `matplotlib==3.11.2`
  * `pytest==9.1.1`
* **Archivo `requirements.txt` (UTF-8):**
  ```text
  colorama==0.4.6
  iniconfig==2.3.0
  matplotlib==3.11.2
  numpy==2.5.3
  packaging==26.3
  pluggy==1.6.0
  Pygments==2.21.0
  pytest==9.1.1
  ```

---

## 10. Pruebas Ejecutadas y 11. Resultados Reales

Comando ejecutado desde la raíz del proyecto:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Resultado real obtenido:

```text
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\danie\MELFA-kinematics\.venv\Scripts\python.exe
rootdir: C:\Users\danie\MELFA-kinematics
configfile: pyproject.toml
testpaths: tests
collecting ... collected 17 items

tests/test_plotting.py::test_plot_frames_3d_valida_dimensiones PASSED    [  5%]
tests/test_plotting.py::test_plot_frames_3d_genera_ejes_etiquetas_y_eslabones PASSED [ 11%]
tests/test_plotting.py::test_plot_frames_3d_no_modifica_datos_entrada PASSED [ 17%]
tests/test_plotting.py::test_plot_frames_3d_sin_eslabon_en_rotacion_pura_y_ax_existente PASSED [ 23%]
tests/test_smoke.py::test_rotaciones_identidad PASSED                    [ 29%]
tests/test_smoke.py::test_traslacion_identidad PASSED                    [ 35%]
tests/test_smoke.py::test_traslacion PASSED                              [ 41%]
tests/test_smoke.py::test_rz_90_grados PASSED                            [ 47%]
tests/test_smoke.py::test_rx_ry_90_grados PASSED                         [ 52%]
tests/test_smoke.py::test_forma_y_ultima_fila_homogenea PASSED           [ 58%]
tests/test_smoke.py::test_ortogonalidad_y_determinante_rotaciones[-3.141592653589793] PASSED [ 64%]
tests/test_smoke.py::test_ortogonalidad_y_determinante_rotaciones[-0.85] PASSED [ 70%]
tests/test_smoke.py::test_ortogonalidad_y_determinante_rotaciones[0.0] PASSED [ 76%]
tests/test_smoke.py::test_ortogonalidad_y_determinante_rotaciones[0.42] PASSED [ 82%]
tests/test_smoke.py::test_ortogonalidad_y_determinante_rotaciones[1.0471975511965976] PASSED [ 88%]
tests/test_smoke.py::test_ortogonalidad_y_determinante_rotaciones[3.141592653589793] PASSED [ 94%]
tests/test_smoke.py::test_validacion_entradas_invalidas PASSED           [100%]

============================= 17 passed in 1.36s ==============================
```

---

## 12. Historial de Commits

Commits registrados en el repositorio (rama `feature/melfa-project-completion` sobre `main`):

```text
* 955dbe0 (feature/melfa-project-completion) feat: implement homogeneous transforms and smoke tests
* df687fa docs: establish project guidelines and repository audit
*   b518f1b (origin/main, main) Merge pull request #1 from DCDC-afk/codex/extraer-plot-frames-3d
|\  
| * 3f750d8 (origin/codex/extraer-plot-frames-3d, codex/extraer-plot-frames-3d) Extraer plot_frames_3d a módulo de visualización
|/  
* 6b0f6ce Agregar ambiente y pruebas de cinemática
* bae7e3e Agregar notebook original y documentacion MELFA
* e1bb7f0 Estructura inicial del proyecto MELFA
```
*(Más el commit de cierre de la Etapa 3 con `plotting.py`, `test_plotting.py`, `bitacora_ia.md` e `informe_final.md`).*

---

## 13. Pull Request

* **Pull Request existente y verificado en el historial:**
  * **PR #1:** `Merge pull request #1 from DCDC-afk/codex/extraer-plot-frames-3d` (`Extraer plot_frames_3d a módulo de visualización`)
  * **URL:** `https://github.com/DCDC-afk/MELFA-kinematics/pull/1`
  * **Rama origen:** `codex/extraer-plot-frames-3d` (`3f750d8`) -> **Rama destino:** `main` (`b518f1b`).
* **Pull Request / Commit de consolidación final:**
  * Preparado localmente con todas las verificaciones aprobadas para que el estudiante ejecute el commit y push hacia GitHub bajo su autorización.

---

## 14. Uso de Inteligencia Artificial

Se documentó con total honestidad en `docs/bitacora_ia.md`:
1. **Codex** fue utilizado en el commit `3f750d8` (rama `codex/extraer-plot-frames-3d`, PR #1) para extraer inicialmente `plot_frames_3d` hacia `src/melfa_kinematics/plotting.py`.
2. **Google Antigravity (Gemini)** fue utilizado para la auditoría de Fase Cero (`docs/auditoria_inicial.md`), la creación de `AGENTS.md`, la corrección de `requirements.txt` (a UTF-8) y `.gitignore`, la configuración de `pyproject.toml`, la ampliación de pruebas unitarias (`tests/test_smoke.py` y `tests/test_plotting.py`) y la documentación final.

---

## 15. Limitaciones Pendientes

1. **Modularización futura de cinemática completa (DH modificada e IK):** Las funciones `make_chain_MELFA` y `cinematica_inversa_MELFA` permanecen en `notebooks/00_mini_taller_original.ipynb`. El alcance de modularización de las Etapas 2 y 3 se centró en `transforms.py` y `plotting.py`, respetando la restricción de cambios pequeños y delimitados.
2. **Inconsistencia documental menor dentro del notebook original:** En `notebooks/00_mini_taller_original.ipynb` (Celda 6 vs. Celda 7), la tabla Markdown muestra signos de $\alpha_{i-1}$ en las filas 4, 5 y 6 opuestos a los del arreglo `alphas` del código, y el docstring menciona `(5, 4, 4)` en vez de `(8, 4, 4)`. Por la regla obligatoria de protección del notebook original (Sección 3.2), dicho archivo no fue alterado y el hallazgo quedó registrado en la auditoría.

---

## 16. Matriz de Evaluación de los 15 Puntos

> *Nota: La asignación numérica definitiva corresponde exclusivamente al docente. Esta matriz refleja el estado técnico verificado de cada criterio.*

### ETAPA 1 — 5 puntos

| Criterio | Estado | Evidencia Verificada |
| :--- | :--- | :--- |
| **Git instalado y configurado** | **CUMPLIDO** | `git version 2.55.0.windows.5`, `user.name = DCDC`, `user.email = danicartagena1208@gmail.com`, `init.defaultBranch = main`. |
| **Repositorio local y remoto** | **CUMPLIDO** | `git remote -v` apunta a `https://github.com/DCDC-afk/MELFA-kinematics.git`. |
| **Estructura organizada** | **CUMPLIDO** | Separación verificada en `docs/`, `notebooks/`, `src/melfa_kinematics/` y `tests/`, más `AGENTS.md` y `pyproject.toml`. |
| **README y documentación** | **CUMPLIDO** | `README.md`, `AGENTS.md`, `docs/caso_de_estudio.md` y `docs/auditoria_inicial.md` completos y sincronizados con el repositorio real. |
| **Primer versionamiento** | **CUMPLIDO** | Commits iniciales `e1bb7f0` y `bae7e3e` preservados en el historial de Git; `notebooks/00_mini_taller_original.ipynb` intacto. |

### ETAPA 2 — 5 puntos

| Criterio | Estado | Evidencia Verificada |
| :--- | :--- | :--- |
| **Ambiente virtual** | **CUMPLIDO** | `.venv` funcional con `Python 3.12.10` y `pip 25.0.1`, excluido de Git. |
| **Dependencias** | **CUMPLIDO** | `requirements.txt` en UTF-8 con `numpy==2.5.3`, `matplotlib==3.11.2`, `pytest==9.1.1` verificados en `.venv`. |
| **`.gitignore`** | **CUMPLIDO** | Excluye `.venv/`, `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/`, `.pytest_cache/`, `*.egg-info/`, `build/`, `dist/`. |
| **Modularización (`transforms.py`)** | **CUMPLIDO** | `src/melfa_kinematics/transforms.py` implementa `Rx`, `Ry`, `Rz`, `Trans` en $SE(3)$ ($4 \times 4$), exportadas en `__init__.py`. |
| **Pruebas (`test_smoke.py`)** | **CUMPLIDO** | 13 pruebas unitarias en `tests/test_smoke.py` aprobadas al 100% con `python -m pytest -v`. |

### ETAPA 3 — 5 puntos

| Criterio | Estado | Evidencia Verificada |
| :--- | :--- | :--- |
| **Preparación de IA** | **CUMPLIDO** | `AGENTS.md` en la raíz con las 9 restricciones obligatorias y `docs/bitacora_ia.md` con registro honesto de herramientas. |
| **Tarea delimitada** | **CUMPLIDO** | Extracción acotada de `plot_frames_3d` sin alterar la matemática central ni el notebook original. |
| **Modularización (`plotting.py`)** | **CUMPLIDO** | `src/melfa_kinematics/plotting.py` implementado, documentado, tipado y exportado en `__init__.py`. |
| **Revisión humana y pruebas** | **CUMPLIDO** | `git diff` inspeccionado y 4 pruebas automatizadas en `tests/test_plotting.py` (backend `Agg`) pasando junto con las 13 de `test_smoke.py` (**17 passed**). |
| **Pull Request** | **CUMPLIDO** | PR #1 real (`codex/extraer-plot-frames-3d` -> `main`, commit `b518f1b`) en GitHub + cambios de consolidación listos para commit/push/PR. |

---

## 17. Evidencias que Debe Presentar el Estudiante

Para sustentar los 15 puntos ante el docente, el estudiante cuenta con las siguientes evidencias verificables:

1. **Enlace al repositorio en GitHub:** `https://github.com/DCDC-afk/MELFA-kinematics` y al Pull Request #1 (`https://github.com/DCDC-afk/MELFA-kinematics/pull/1`) más el PR de consolidación final.
2. **Integridad del notebook original:** Demostrar con `git log -p notebooks/00_mini_taller_original.ipynb` y `git diff notebooks/00_mini_taller_original.ipynb` que el cuaderno no sufrió ninguna alteración desde su incorporación en el commit `bae7e3e`.
3. **Ejecución en vivo de la suite de pruebas (`17 passed`):**
   ```powershell
   .\.venv\Scripts\python.exe -m pytest -v
   ```
4. **Demostración de importación del paquete `melfa_kinematics`:**
   ```powershell
   .\.venv\Scripts\python.exe -c "import numpy as np; from melfa_kinematics import Rx, Ry, Rz, Trans, plot_frames_3d; print(Rz(np.pi/2)); print(Trans(1,2,3))"
   ```
5. **Documentación técnica y de auditoría en `docs/` y raíz:**
   * `AGENTS.md`
   * `README.md`
   * `docs/auditoria_inicial.md`
   * `docs/caso_de_estudio.md`
   * `docs/bitacora_ia.md`
   * `docs/informe_final.md`
