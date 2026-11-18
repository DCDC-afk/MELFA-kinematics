# Auditoría Inicial del Repositorio — `MELFA-kinematics` (Fase Cero / Bloque 0)

**Fecha de auditoría:** 2026-11-18  
**Repositorio:** `https://github.com/DCDC-afk/MELFA-kinematics`  
**Directorio local:** `c:\Users\danie\MELFA-kinematics`  
**Plataforma / Agente:** Google Antigravity (Gemini)

---

## 1. Estado Inicial del Repositorio

El repositorio local `MELFA-kinematics` no parte de cero: cuenta con un historial real de 5 commits distribuidos entre la rama principal `main` (HEAD en `b518f1b`) y la rama `codex/extraer-plot-frames-3d` (HEAD en `3f750d8`), ambas sincronizadas con el remoto `origin` y con el mismo árbol de archivos.

En su estado inicial ya se habían adelantado piezas clave de las tres etapas:
* **Etapa 1:** Creación del repositorio local y remoto, incorporación del notebook original (`notebooks/00_mini_taller_original.ipynb`), redacción inicial de `README.md` y `docs/caso_de_estudio.md`.
* **Etapa 2:** Creación del ambiente virtual local `.venv/` (Python 3.12.10), `.gitignore` básico, `requirements.txt`, módulo `src/melfa_kinematics/transforms.py` (`Rx`, `Ry`, `Rz`, `Trans`) y pruebas iniciales en `tests/test_smoke.py`.
* **Etapa 3:** Extracción de `plot_frames_3d` hacia `src/melfa_kinematics/plotting.py` mediante la rama `codex/extraer-plot-frames-3d` e integración a `main` mediante el Pull Request #1 (`b518f1b`).

Sin embargo, la inspección técnica revela **archivos faltantes obligatorios**, **desfases en la documentación**, **problemas de codificación y configuración de paquetes/pruebas**, y **ausencia de pruebas automatizadas para visualización y de trazabilidad formal de IA**, que impiden alcanzar todavía el 100% de los criterios de los 15 puntos.

---

## 2. Estructura Encontrada

Árbol real del repositorio al iniciar la Fase Cero (excluyendo `.git`, `.venv` y `__pycache__`):

```text
MELFA-kinematics/
├── .gitignore
├── README.md
├── requirements.txt
├── .pytest_cache/                           # Directorio local no ignorado (con error de permisos de lectura/escritura)
├── docs/
│   ├── auditoria_inicial.md                 # Generado en esta Fase Cero
│   └── caso_de_estudio.md
├── notebooks/
│   └── 00_mini_taller_original.ipynb
├── src/
│   └── melfa_kinematics/
│       ├── __init__.py
│       ├── plotting.py
│       └── transforms.py
└── tests/
    └── test_smoke.py
```

*(Nota: Existe localmente el entorno virtual `.venv/`, correctamente ignorado por Git).*

---

## 3. Archivos Existentes (Inspección de Contenido Real)

1. **`README.md` (112 líneas):**
   * Contiene título, propósito, origen del proyecto, árbol de estructura inicial (Etapa 1), flujo de trabajo conceptual, distinción entre Git y GitHub, estado actual (detenido en Etapa 1), alcance futuro y sección breve sobre uso responsable de IA.
2. **`docs/caso_de_estudio.md` (119 líneas):**
   * Describe contexto, punto de partida, problema de organización, objetivo, evolución prevista en las Etapas 1, 2 y 3, principios de trabajo y estado actual (detenido antes de cerrar la Etapa 1).
3. **`notebooks/00_mini_taller_original.ipynb` (2719 líneas, 45 celdas):**
   * Validado como JSON íntegro (`45` celdas, índices `0` a `44`).
   * Autores registrados en celda 0: *Daniel Cartagena, Julian Zambrano, Edwin Vela*.
   * Incluye: `plot_frames_xy` (2D), utilidades $SE(3)$ (`Rx`, `Ry`, `Rz`, `Trans`), `plot_frames_3d` (3D), teoría $\text{DH}_{\text{mod}}$ (Craig) y función `make_chain_MELFA`, teoría de cinemática inversa de 6 GDL con muñeca esférica, enunciados del Mini-taller 2, cinemática simbólica (`sympy`) y numérica de robots RR, PR, RP, RPR y MELFA, e implementación analítica de cinemática inversa del MELFA (`matriz_rotacion_ABC`, `calcular_centro_muneca`, `resolver_posicion`, `resolver_orientacion`, `cinematica_inversa_MELFA`) evaluada en 4 objetivos de laboratorio (`Ls = [150, 300, 250, 80]` mm) y en postura cero (`ag0 = [0, 0, 0, 0, 0, 0]`).
4. **`.gitignore` (3 líneas):**
   * Contiene únicamente `.venv/`, `__pycache__/` y `*.pyc`.
5. **`requirements.txt` (270 bytes, 8 líneas):**
   * Registra `colorama==0.4.6`, `iniconfig==2.3.0`, `matplotlib==3.11.2`, `numpy==2.5.3`, `packaging==26.3`, `pluggy==1.6.0`, `Pygments==2.21.0`, `pytest==9.1.1`.
   * Codificado en **UTF-16 LE con BOM (`\xff\xfe`)**, por lo que Git lo marca como binario (`Binary files differ`).
6. **`src/melfa_kinematics/__init__.py` (0 bytes):**
   * Archivo vacío; no exporta símbolos del paquete.
7. **`src/melfa_kinematics/transforms.py` (50 líneas):**
   * Implementa `Rx(theta)`, `Ry(theta)`, `Rz(theta)` y `Trans(x, y, z)` con NumPy y docstrings básicos.
8. **`src/melfa_kinematics/plotting.py` (85 líneas):**
   * Implementa `plot_frames_3d(T_list, axis_length=0.1, link_tol=1e-12, ax=None, show=True, title=None)` fiel al notebook original.
9. **`tests/test_smoke.py` (33 líneas):**
   * Implementa 3 pruebas: `test_rotaciones_identidad`, `test_traslacion` y `test_rz_90_grados`.

---

## 4. Archivos Faltantes

De acuerdo con la Instrucción Maestra (Secciones 4 a 12), faltan los siguientes archivos en el repositorio:

| Archivo faltante | Etapa / Sección | Propósito |
| :--- | :--- | :--- |
| `AGENTS.md` | Etapa 1 (Sección 5.3) | Reglas de arquitectura, convenciones matemáticas/Python, protección del notebook original y restricciones obligatorias para agentes de IA. |
| `tests/test_plotting.py` | Etapa 3 (Secciones 7.3, 7.5, 9) | Pruebas automatizadas y verificación sin interfaz bloqueante (backend no interactivo / `show=False`) para `plot_frames_3d`. |
| `docs/bitacora_ia.md` | Etapa 3 (Sección 8) | Registro transparente y trazable de las interacciones con herramientas de IA (diferenciando Codex y Google Antigravity/Gemini) y reflexión académica. |
| `docs/informe_final.md` | Cierre (Sección 12) | Informe ejecutivo final con comparación Antes/Después, resultados reales, matriz de evaluación de los 15 puntos y guía de evidencias para el estudiante. |
| `pyproject.toml` (o configuración de paquete/pytest) | Etapa 2 (Sección 6.9) | Permitir importación limpia desde `melfa_kinematics` (instalación editable en `.venv`) y ejecución estándar de `pytest` sin manipulaciones improvisadas de `sys.path`. |

---

## 5. Archivos que Necesitan Corrección

1. **`README.md`:**
   * Su árbol de proyecto solo muestra el estado de la Etapa 1 (omite `AGENTS.md`, `.gitignore`, `requirements.txt`, `src/melfa_kinematics/*`, `tests/*` y nuevos documentos en `docs/`).
   * La sección *Estado actual* afirma erróneamente que apenas se terminó la Etapa 1.
   * Carece de instrucciones prácticas de instalación de Python/Git, creación y activación de `.venv`, instalación de `requirements.txt`, ejecución de `pytest`, explicación de matrices homogéneas, ejemplo de código de transformaciones y uso de visualización 3D, limitaciones conocidas y autores.
2. **`docs/caso_de_estudio.md`:**
   * Presenta etiquetas residuales no estándar en bloques de código: ```` ```text id="4l6qvs" ```` (línea 23), ```` ```text id="9h6zmx" ```` (línea 64) y ```` ```text id="6v0qkp" ```` (línea 87).
   * La sección `## 7. Estado actual` sigue redactada como si el primer commit aún estuviera pendiente.
   * Falta documentar en detalle qué se modularizó en las Etapas 2 y 3, por qué se eligieron las transformaciones, qué representa cada función, cómo se probaron y qué limitaciones permanecen (Sección 6.10).
3. **`.gitignore`:**
   * Faltan las exclusiones `.ipynb_checkpoints/` y `.pytest_cache/` exigidas en la Sección 6.3 (además de artefactos de construcción como `*.egg-info/`, `build/`, `dist/`).
4. **`requirements.txt`:**
   * Está codificado en **UTF-16 LE con BOM** (`\xff\xfe`), lo que provoca que Git lo trate como archivo binario (`Binary files a/requirements.txt and b/requirements.txt differ`). Debe convertirse a **UTF-8**.
   * En `.venv` están instaladas 16 librerías (incluyendo las subdependencias obligatorias de `matplotlib` como `contourpy`, `cycler`, `fonttools`, `kiwisolver`, `pillow`, `pyparsing`, `python-dateutil`, `six`), mientras que `requirements.txt` solo tenía 8 líneas. Debe actualizarse de forma coherente y limpia en UTF-8.
5. **`src/melfa_kinematics/__init__.py`:**
   * Está vacío (`0` bytes). Debe exponer las funciones públicas (`Rx`, `Ry`, `Rz`, `Trans` en Etapa 2 y `plot_frames_3d` cuando corresponda, sin efectos secundarios al importar).
6. **`src/melfa_kinematics/transforms.py`:**
   * Funcionalmente correcto, pero conviene enriquecer docstrings especificando unidades (radianes para ángulos, unidades consistentes con el modelo para traslación, convención $SE(3)$ de 4x4 y tipo `float`), además de permitir valores por defecto `Trans(x=0.0, y=0.0, z=0.0)` compatibles tanto con el notebook original como con llamadas posicionales `Trans(1, 2, 3)`.
7. **`tests/test_smoke.py`:**
   * Importa mediante `from src.melfa_kinematics.transforms import ...`, lo que falla al invocar `pytest` directamente (`ModuleNotFoundError: No module named 'src'`) si no se usa `python -m pytest` o instalación editable.
   * Faltan pruebas obligatorias de la Sección 6.7: `Trans(0, 0, 0) == I_4`, `Trans(1, 2, 3)`, forma `(4, 4)`, última fila `[0, 0, 0, 1]`, ortogonalidad ($R^T R = I_3$) y determinante ($\det(R) \approx 1$).

---

## 6. Estado de Git

Resultados reales verificados por línea de comandos:

* **Versión de Git:** `git version 2.55.0.windows.5`
* **Identidad configurada:**
  * `user.name`: `DCDC`
  * `user.email`: `danicartagena1208@gmail.com`
  * `init.defaultBranch`: `main`
* **Remoto configurado (`git remote -v`):**
  * `origin  https://github.com/DCDC-afk/MELFA-kinematics.git (fetch)`
  * `origin  https://github.com/DCDC-afk/MELFA-kinematics.git (push)`
* **Ramas existentes (`git branch -a`):**
  * `main` -> `b518f1b` (`[origin/main] Merge pull request #1 from DCDC-afk/codex/extraer-plot-frames-3d`)
  * `codex/extraer-plot-frames-3d` -> `3f750d8` (`[origin/codex/extraer-plot-frames-3d] Extraer plot_frames_3d a módulo de visualización`) — *rama actualmente activa (`HEAD`), con contenido de archivos idéntico a `main`*.
* **Historial de commits (`git log --oneline --all`):**
  ```text
  b518f1b (origin/main, main) Merge pull request #1 from DCDC-afk/codex/extraer-plot-frames-3d
  3f750d8 (HEAD -> codex/extraer-plot-frames-3d, origin/codex/extraer-plot-frames-3d) Extraer plot_frames_3d a módulo de visualización
  6b0f6ce Agregar ambiente y pruebas de cinemática
  bae7e3e Agregar notebook original y documentacion MELFA
  e1bb7f0 Estructura inicial del proyecto MELFA
  ```

---

## 7. Estado de las Pruebas y del Ambiente Python

* **Entorno virtual `.venv`:** Existe localmente con **Python 3.12.10** y **pip 25.0.1**.
* **Paquetes clave verificados en `.venv`:**
  * `numpy==2.5.3`
  * `matplotlib==3.11.2`
  * `pytest==9.1.1`
* **Ejecución con `.\.venv\Scripts\pytest.exe`:**
  * **Falla** en recolección (`1 error`): `ModuleNotFoundError: No module named 'src'` en `tests/test_smoke.py:3`.
* **Ejecución con `.\.venv\Scripts\python.exe -m pytest -p no:cacheprovider`:**
  * **Pasa** (`3 passed in 0.17s`), ejecutando las 3 pruebas actuales de `tests/test_smoke.py`.
* **Advertencia detectada:** El directorio `.pytest_cache` existente en la raíz tiene permisos restringidos en Windows (`[WinError 5] Acceso denegado`), generando 2 `PytestCacheWarning` y el mensaje `warning: could not open directory '.pytest_cache/': Permission denied` al ejecutar `git status`.
* **Cobertura actual:**
  * `transforms.py`: cubierta parcialmente (3 pruebas básicas).
  * `plotting.py`: **0 pruebas automatizadas**.

---

## 8. Riesgos Detectados

1. **Riesgo de trazabilidad de IA (Codex vs. Antigravity/Gemini):**
   * En el repositorio ya existe un commit/PR real creado previamente en la rama `codex/extraer-plot-frames-3d` (`3f750d8` / PR #1 `b518f1b`). Las mejoras, pruebas, auditoría y documentación posteriores realizadas en esta sesión se ejecutan con **Google Antigravity (Gemini)**. En `docs/bitacora_ia.md` e `informe_final.md` se debe distinguir con total honestidad el trabajo previo en la rama `codex/extraer-plot-frames-3d` del trabajo de finalización realizado con Antigravity/Gemini.
2. **Riesgo por archivo binario `requirements.txt`:**
   * Al estar en UTF-16 LE, cualquier `git diff` muestra `Binary files differ`, impidiendo auditar cambios de dependencias en un Pull Request.
3. **Riesgo de bloqueo de permisos en `.pytest_cache/`:**
   * La carpeta local `.pytest_cache/` tiene bloqueo de permisos de Windows. Se debe ignorar en `.gitignore` y configurar `pytest` (o limpiar/redirigir `cache_dir` en configuración) para eliminar las advertencias sin usar comandos destructivos prohibidos.
4. **Riesgo de alteración accidental del notebook original:**
   * `notebooks/00_mini_taller_original.ipynb` no debe abrirse en modo escritura ni ejecutarse sobrescribiendo metadatos. Se verificará con `git diff notebooks/00_mini_taller_original.ipynb` antes de cada commit.
5. **Inconsistencias internas documentadas en el notebook original (solo para conocimiento técnico, sin modificar el notebook):**
   * En `notebooks/00_mini_taller_original.ipynb`, la tabla Markdown de la Celda 6 tiene signos de $\alpha_{i-1}$ en las filas 4, 5 y 6 ($\pi/2, -\pi/2, \pi/2$) opuestos a los del código de `make_chain_MELFA` ($-\pi/2, \pi/2, -\pi/2$), y el docstring de `make_chain_MELFA` indica forma `(5, 4, 4)` cuando realmente devuelve `(8, 4, 4)`. Como el notebook está protegido, esto solo se documenta como observación técnica sin tocar el archivo `.ipynb`.

---

## 9. Comparación entre Requisitos y Estado Actual (Matriz de Cumplimiento)

### 9.1 Evaluación por Criterios de las Tres Etapas (`CUMPLE` / `PARCIALMENTE CUMPLE` / `NO CUMPLE`)

| Etapa | Requisito / Criterio | Estado Actual | Qué existe | Qué funciona | Qué falta | Qué debe corregirse | Qué debe conservarse | Qué pruebas faltan | Qué evidencias se necesitan |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Etapa 1** (5 pts) | **5.1 & 5.2 Git y GitHub configurados** | **CUMPLE** | Git 2.55.0, `user.name` (`DCDC`), `user.email`, remoto `origin` hacia `DCDC-afk/MELFA-kinematics`, rama `main`. | Comandos `git`, sincronización con `origin/main` y historial de 5 commits. | Cambiar de `codex/extraer-plot-frames-3d` a `main` y crear rama de trabajo controlada (`feature/melfa-project-completion`). | Nada en la configuración de Git/remoto. | Todos los commits existentes (`e1bb7f0` a `b518f1b`) y el remoto `origin`. | N/A | Salida de `git --version`, `git config`, `git remote -v` y `git log`. |
| **Etapa 1** (5 pts) | **5.3 Archivo `AGENTS.md`** | **NO CUMPLE** | No existe `AGENTS.md` en la raíz. | N/A | Crear `AGENTS.md` con las 12 secciones y las 9 reglas obligatorias para agentes de IA. | N/A | N/A | Verificación de existencia y contenido completo de `AGENTS.md`. | Archivo `AGENTS.md` en la raíz y su `git diff`. |
| **Etapa 1** (5 pts) | **5.4 & 5.5 `README.md` completo y árbol real** | **PARCIALMENTE CUMPLE** | `README.md` de 112 líneas con propósito y contexto básico. | Describe la filosofía de separación entre notebook y código. | Ampliar con los 19 puntos de la Sección 5.4 (contexto 6 GDL, guía de Python/Git/`.venv`/dependencias/`pytest`, explicación y ejemplo de matrices $4 \times 4$, visualización 3D, limitaciones, bitácora IA, autores). | Actualizar el árbol de directorios y la sección *Estado actual* (hoy desactualizados en Etapa 1). | Propósito original y tono académico del documento. | Verificar que los fragmentos de código de ejemplo del `README.md` sean ejecutables en `.venv`. | `README.md` actualizado y verificado. |
| **Etapa 1** (5 pts) | **3.2 & 5.6 Protección del notebook original** | **CUMPLE** | `notebooks/00_mini_taller_original.ipynb` (2719 líneas, 45 celdas JSON válidas). | El archivo es JSON válido y conserva todas las celdas y salidas originales. | Mantener monitoreo de integridad en cada bloque. | **Nada** (prohibido modificarlo). | `notebooks/00_mini_taller_original.ipynb` **100% intacto**. | Comprobación de `git diff` vacío sobre `notebooks/00_mini_taller_original.ipynb`. | Hash / `git status` confirmando cero cambios en el notebook. |
| **Etapa 2** (5 pts) | **6.1 & 6.2 Ambiente `.venv` y `requirements.txt`** | **PARCIALMENTE CUMPLE** | `.venv/` con Python 3.12.10 (`numpy`, `matplotlib`, `pytest` instalados) y `requirements.txt`. | El intérprete `.venv\Scripts\python.exe` ejecuta correctamente y tiene los paquetes requeridos. | Convertir `requirements.txt` a texto plano UTF-8 y asegurar reproducibilidad con `pip install -r requirements.txt`. | `requirements.txt` está en **UTF-16 LE con BOM** (tratado como binario en Git). | Entorno `.venv` local (fuera de Git) y paquetes `numpy`, `matplotlib`, `pytest`. | `python -m pip show numpy matplotlib pytest`. | `requirements.txt` legible en `git diff` y salida de `pip show`. |
| **Etapa 2** (5 pts) | **6.3 `.gitignore` completo** | **PARCIALMENTE CUMPLE** | `.gitignore` con `.venv/`, `__pycache__/`, `*.pyc`. | Excluye `.venv/` y `__pycache__/`. | Añadir `.ipynb_checkpoints/`, `.pytest_cache/` y artefactos de empaquetado (`*.egg-info/`, `build/`, `dist/`). | Agregar las reglas faltantes para evitar que `.pytest_cache/` contamine el árbol. | Las 3 reglas actuales. | `git status --short` confirmando que `.venv/` y `.pytest_cache/` no se versionan. | Contenido de `.gitignore` y `git status --short`. |
| **Etapa 2** (5 pts) | **6.4, 6.5 & 6.6 Paquete `melfa_kinematics`, `transforms.py` e `__init__.py`** | **PARCIALMENTE CUMPLE** | `src/melfa_kinematics/transforms.py` (`Rx`, `Ry`, `Rz`, `Trans`) y `__init__.py` vacío. | `Rx`, `Ry`, `Rz`, `Trans` retornan las matrices $4 \times 4$ con la convención exacta del notebook. | Completar `__init__.py` con las exportaciones públicas; añadir docstrings detallados (unidades, radianes, $SE(3)$) y valores por defecto en `Trans(x=0.0, y=0.0, z=0.0)`; configurar `pyproject.toml` para importación limpia `from melfa_kinematics.transforms import ...`. | `__init__.py` está vacío (`0` bytes) y el paquete no es importable como `melfa_kinematics` sin prefijo `src.`. | Las 4 funciones `Rx`, `Ry`, `Rz`, `Trans` y sus fórmulas matemáticas exactas. | Prueba de importación directa `from melfa_kinematics import Rx, Ry, Rz, Trans`. | Código de `transforms.py`, `__init__.py` y ejecución del script de ejemplo (Sección 6.9). |
| **Etapa 2** (5 pts) | **6.7, 6.8 & 6.10 `tests/test_smoke.py` y actualización de `docs/caso_de_estudio.md`** | **PARCIALMENTE CUMPLE** | `tests/test_smoke.py` con 3 pruebas y `docs/caso_de_estudio.md`. | Las 3 pruebas existentes pasan con `python -m pytest`. | Añadir pruebas obligatorias en `test_smoke.py`: `Trans(0,0,0) = I`, `Trans(1,2,3)`, forma `(4,4)`, fila `[0,0,0,1]`, ortogonalidad y $\det(R)=1$. Actualizar `docs/caso_de_estudio.md` con lo modularizado, justificación, pruebas y limitaciones. | Limpiar `id="..."` en `docs/caso_de_estudio.md` y actualizar su sección *Estado actual*. | Las 3 pruebas originales de `test_smoke.py` y la estructura base de `docs/caso_de_estudio.md`. | Las nuevas pruebas geométricas de $SE(3)$ en `tests/test_smoke.py`. | Salida de `python -m pytest -v` con todos los tests aprobados y `docs/caso_de_estudio.md` actualizado. |
| **Etapa 3** (5 pts) | **7.3, 7.4, 7.5 & 7.6 Módulo `plotting.py` y verificación/pruebas 3D** | **PARCIALMENTE CUMPLE** | `src/melfa_kinematics/plotting.py` con `plot_frames_3d` extraído en el commit `3f750d8` y fusionado en PR #1 (`b518f1b`). | `plot_frames_3d` respeta el comportamiento matemático y visual del notebook original. | Añadir anotaciones de tipos/docstring ampliado si aporta claridad, crear pruebas automatizadas en `tests/test_plotting.py` (con backend `Agg` no interactivo y `show=False`) y verificar que no muta los datos de entrada. | Falta cobertura de pruebas automatizadas y verificación visual documentada para `plot_frames_3d`. | Función `plot_frames_3d` y su compatibilidad con arreglos `(N, 4, 4)`. | `tests/test_plotting.py`: validación de forma `(N, 4, 4)`, error `ValueError`, creación de ejes/etiquetas/eslabones, inmutabilidad de entrada. | Salida de `python -m pytest -v` incluyendo `test_plotting.py`. |
| **Etapa 3** (5 pts) | **7.7, 8 & 12 Pull Request, `docs/bitacora_ia.md` y `docs/informe_final.md`** | **PARCIALMENTE CUMPLE** | Existe en el historial el PR #1 (`codex/extraer-plot-frames-3d` -> `main`, commit `b518f1b`). No existen `docs/bitacora_ia.md` ni `docs/informe_final.md`. | El merge commit `b518f1b` evidencia un flujo previo de rama + PR en GitHub. | Crear `docs/bitacora_ia.md` (registrando honestamente Codex y Antigravity/Gemini), `docs/informe_final.md` (con la matriz de 15 puntos y tabla Antes/Después) y preparar la rama/PR de completitud para revisión del usuario. | N/A | Historial del PR #1 (`b518f1b`) y rama `codex/extraer-plot-frames-3d`. | Revisión integral de calidad (Sección 10). | `docs/bitacora_ia.md`, `docs/informe_final.md`, diff revisado y PR en GitHub tras autorización. |

### 9.2 Comparación Sintética: Estado Actual vs. Estado Objetivo

| Aspecto | Estado Actual (Antes) | Estado Objetivo (Después — Meta 15 Puntos) |
| :--- | :--- | :--- |
| **Organización** | Estructura parcial; sin `AGENTS.md`, `bitacora_ia.md` ni `informe_final.md`. | Estructura completa, limpia y alineada con la Sección 9 de la Instrucción Maestra. |
| **Código reusable** | `transforms.py` y `plotting.py` existen, pero `__init__.py` está vacío y el paquete no está configurado como instalable (`melfa_kinematics`). | Paquete `melfa_kinematics` instalable en modo editable, con `__init__.py`, `transforms.py` y `plotting.py` documentados. |
| **Ambiente y dependencias** | `.venv` funcional con Python 3.12.10, pero `requirements.txt` está en UTF-16 LE (binario en Git). | `.venv` verificado y `requirements.txt` en UTF-8 limpio y reproducible. |
| **Pruebas automatizadas** | 3 tests básicos en `test_smoke.py`; falla si se invoca `pytest` sin `python -m`; 0 tests para `plotting.py`. | Suite completa en `tests/test_smoke.py` y `tests/test_plotting.py` pasando al 100% con `python -m pytest -v` y `pytest`. |
| **Documentación** | `README.md` y `docs/caso_de_estudio.md` desactualizados en Etapa 1; etiquetas `id="..."` residuales. | `README.md`, `AGENTS.md`, `docs/caso_de_estudio.md`, `docs/auditoria_inicial.md`, `docs/bitacora_ia.md` y `docs/informe_final.md` completos y coherentes. |
| **Trazabilidad IA y GitHub** | PR #1 fusionado (`codex/extraer-plot-frames-3d`), sin bitácora de IA ni informe de verificación de diff/pruebas. | Uso de IA (Codex y Antigravity/Gemini) documentado con transparencia, cambios en rama dedicada y PR revisable. |

---

## 10. Plan de Ejecución Recomendado (Por Bloques Controlados)

Siguiendo la **Sección 3.5** y la **Sección 13** de la Instrucción Maestra, el trabajo se ejecutará sobre una rama de trabajo dedicada (sin modificar `main` directamente, sin tocar `notebooks/00_mini_taller_original.ipynb` y sin hacer `push` ni `merge` sin autorización explícita):

* **Bloque 0 — Auditoría (COMPLETADO):**
  * Inspección total del repositorio, historial Git, ambiente `.venv`, pruebas y generación de `docs/auditoria_inicial.md`.
* **Bloque 1 — Preparación de Rama, Documentación de Etapa 1 y `AGENTS.md`:**
  * Cambiar a `main` y crear la rama de trabajo `feature/melfa-project-completion` (Sección 3.5).
  * Crear `AGENTS.md` con todos los lineamientos obligatorios (Sección 5.3).
  * Actualizar `README.md` con la estructura real y los 19 puntos requeridos (Secciones 5.4 y 5.5).
  * *Archivos afectados:* `AGENTS.md`, `README.md`, `docs/auditoria_inicial.md`.
* **Bloque 2 — Ambiente Virtual, Dependencias (`requirements.txt`) y `.gitignore`:**
  * Verificar intérprete `.venv` (`python --version`, `pip show numpy matplotlib pytest`).
  * Convertir y normalizar `requirements.txt` en codificación **UTF-8** estándar.
  * Completar `.gitignore` (incluyendo `.ipynb_checkpoints/`, `.pytest_cache/`, `*.egg-info/`, `build/`, `dist/`) y configurar `pyproject.toml` para que el paquete `melfa_kinematics` sea importable limpiamente y `pytest` no tenga conflictos con `.pytest_cache`.
  * *Archivos afectados:* `.gitignore`, `requirements.txt`, `pyproject.toml`.
* **Bloque 3 — Consolidación de `transforms.py`, `__init__.py` y `docs/caso_de_estudio.md`:**
  * Completar docstrings y convenciones matemáticas en `src/melfa_kinematics/transforms.py` (manteniendo intacta la matemática del notebook y soportando `Trans(x=0.0, y=0.0, z=0.0)`).
  * Exportar la API pública en `src/melfa_kinematics/__init__.py`.
  * Actualizar `docs/caso_de_estudio.md` (limpiando etiquetas `id="..."` y documentando las Etapas 2 y 3 según la Sección 6.10).
  * *Archivos afectados:* `src/melfa_kinematics/transforms.py`, `src/melfa_kinematics/__init__.py`, `docs/caso_de_estudio.md`.
* **Bloque 4 — Pruebas Automatizadas de Transformaciones (`tests/test_smoke.py`) y Ejemplo de Uso:**
  * Ampliar `tests/test_smoke.py` con todas las pruebas obligatorias y complementarias de la Sección 6.7 (`Rx(0)`, `Ry(0)`, `Rz(0)`, `Trans(0,0,0)`, `Trans(1,2,3)`, `Rz(pi/2)`, `Rx(pi/2)`, `Ry(pi/2)`, forma `4x4`, última fila `[0,0,0,1]`, ortogonalidad $R^T R = I$ y $\det(R) = 1$).
  * Ejecutar `python -m pytest -v` y verificar el ejemplo de importación de la Sección 6.9.
  * *Archivos afectados:* `tests/test_smoke.py`.
* **Bloque 5 y Bloque 6 — Revisión y Mejora del Módulo de Visualización 3D (`plotting.py`):**
  * Inspeccionar `src/melfa_kinematics/plotting.py` (ya extraído en el commit `3f750d8` / PR #1), enriquecer docstrings/anotaciones de tipos sin cambiar su comportamiento visual ni matemático, y exportarlo limpiamente.
  * *Archivos afectados:* `src/melfa_kinematics/plotting.py`, `src/melfa_kinematics/__init__.py`.
* **Bloque 7 — Pruebas Automatizadas de Visualización (`tests/test_plotting.py`) y Revisión de Diffs:**
  * Crear `tests/test_plotting.py` usando backend no interactivo (`Agg`) y `show=False` para verificar: generación de sistemas de coordenadas 3D con datos de transformación conocidos, etiquetas `Xi, Yi, Zi`, segmentos de eslabones, inmutabilidad del arreglo de entrada y validación `ValueError` ante formas inválidas.
  * Ejecutar `python -m pytest -v` y revisar `git diff` completo.
  * *Archivos afectados:* `tests/test_plotting.py`.
* **Bloque 8 y Bloque 9 — Trazabilidad de IA (`docs/bitacora_ia.md`), Commits Autorizados y Flujo de Pull Request:**
  * Crear `docs/bitacora_ia.md` documentando con total transparencia el historial previo (rama `codex/extraer-plot-frames-3d`, PR #1) y las interacciones con Google Antigravity (Gemini) en esta sesión.
  * Presentar `git status` y `git diff` al usuario para solicitar autorización de commits, push y Pull Request.
  * *Archivos afectados:* `docs/bitacora_ia.md`.
* **Bloque 10 — Control de Calidad Global e Informe Final (`docs/informe_final.md`):**
  * Ejecutar todas las comprobaciones de la Sección 10 (Git, Python, `pytest -v`, integridad intacta de `notebooks/00_mini_taller_original.ipynb`).
  * Generar `docs/informe_final.md` con los 17 puntos obligatorios, la tabla comparativa Antes/Después y la Matriz de Evaluación de los 15 puntos.
  * *Archivos afectados:* `docs/informe_final.md`.
