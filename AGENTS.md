# AGENTS.md — Guía y Reglas de Trabajo para Agentes de IA

## 1. Descripción del Proyecto

**MELFA-kinematics** es un repositorio académico y técnico en Python dedicado al modelado, organización, visualización 3D y verificación de la cinemática de un robot manipulador industrial **Mitsubishi MELFA de 6 grados de libertad (GDL)**.

El proyecto parte de un cuaderno de Jupyter desarrollado en un taller académico (`notebooks/00_mini_taller_original.ipynb`) y extrae progresivamente sus componentes reutilizables hacia un paquete Python estructurado (`src/melfa_kinematics/`), respaldado por pruebas automatizadas (`tests/`) y documentación técnica (`docs/`).

## 2. Objetivo Técnico

Transformar material exploratorio de un notebook académico en un repositorio de software científico reproducible, modular, probado con `pytest` y versionado con Git y GitHub, preservando intacta la referencia original del taller.

## 3. Estructura de Carpetas

```text
MELFA-kinematics/
├── README.md
├── AGENTS.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── docs/
│   ├── auditoria_inicial.md
│   ├── caso_de_estudio.md
│   ├── bitacora_ia.md
│   └── informe_final.md
├── notebooks/
│   └── 00_mini_taller_original.ipynb
├── src/
│   └── melfa_kinematics/
│       ├── __init__.py
│       ├── transforms.py
│       └── plotting.py
└── tests/
    ├── test_smoke.py
    └── test_plotting.py
```

* **`notebooks/`**: Material original de referencia académica (solo lectura).
* **`src/melfa_kinematics/`**: Código Python modular y reutilizable (transformaciones homogéneas y visualización 3D).
* **`tests/`**: Pruebas unitarias y de humo ejecutables con `pytest`.
* **`docs/`**: Documentación del caso de estudio, auditoría, bitácora de IA e informe final.

## 4. Convenciones de Python

* **Versión de Python:** Python 3.10 o superior (verificado en entorno local con Python 3.12).
* **Estilo de código:** Cumplir con PEP 8, nombres descriptivos, funciones cohesivas y docstrings claros en español.
* **Tipado:** Utilizar anotaciones de tipos (`type hints`) cuando aporten claridad sin afectar la compatibilidad con NumPy y Matplotlib.
* **Codificación de archivos:** Todos los archivos de texto y configuración (`.py`, `.md`, `requirements.txt`, `.toml`, `.gitignore`) deben guardarse en **UTF-8 sin BOM**.
* **Importaciones:** No introducir efectos secundarios (como abrir ventanas gráficas o ejecutar scripts) al importar módulos del paquete `melfa_kinematics`.

## 5. Reglas para Modificar el Notebook Original

El archivo `notebooks/00_mini_taller_original.ipynb` es **material académico histórico y de referencia**.

**Está estrictamente prohibido:**
* Eliminarlo o renombrarlo.
* Reescribir, limpiar o alterar sus celdas de código o Markdown.
* Cambiar sus cálculos, parámetros o salidas almacenadas.
* Reemplazarlo por un notebook generado automáticamente.

Cualquier mejora, corrección o nueva funcionalidad debe implementarse en módulos dentro de `src/melfa_kinematics/` o en pruebas dentro de `tests/`.

## 6. Reglas de Modularización

* Extraer funciones de manera incremental y delimitada, manteniendo la firma y el contrato del notebook original siempre que sea posible.
* Evitar la duplicación de lógica matemática entre módulos.
* Mantener separadas las responsabilidades:
  * `transforms.py`: álgebra de matrices de transformación homogénea en $SE(3)$.
  * `plotting.py`: representación visual 3D de tramas y eslabones con Matplotlib.
* Exponer únicamente la interfaz pública estable en `src/melfa_kinematics/__init__.py`.

## 7. Convenciones Matemáticas

* **Grupo espacial $SE(3)$:** Todas las transformaciones homogéneas se representan mediante matrices reales de dimensión $4 \times 4$ (`dtype=float`):
  $$T = \begin{bmatrix} R & p \\ 0_{1 \times 3} & 1 \end{bmatrix}$$
  donde $R \in SO(3)$ es una matriz de rotación ortogonal ($R^T R = I_3$, $\det(R) = 1$) y $p \in \mathbb{R}^3$ es el vector de traslación.
* **Unidades angulares:** Todas las funciones trigonométricas y de rotación (`Rx`, `Ry`, `Rz`) reciben ángulos **en radianes**.
* **Unidades de longitud:** Las traslaciones (`Trans(x, y, z)`) utilizan unidades consistentes con el modelo geométrico evaluado (metros o milímetros según la parametrización del robot).
* **Composición:** Las transformaciones se componen mediante multiplicación matricial estándar (`@` en NumPy), respetando la convención de post-multiplicación respecto al marco móvil o Denavit–Hartenberg modificada ($\text{DH}_{\text{mod}}$, convención de Craig) empleada en el notebook original.
* **Invarianza matemática:** No alterar signos, órdenes de ejes ni fórmulas de rotación o traslación respecto al notebook original.

## 8. Reglas para Pruebas

* Utilizar `pytest` junto con `numpy.allclose` o `numpy.testing.assert_allclose`.
* Verificar casos base (identidad en ángulo cero y traslación nula), rotaciones conocidas ($90^\circ = \pi/2\text{ rad}$) e invariantes geométricos de $SE(3)$ (forma `(4, 4)`, fila homogénea `[0, 0, 0, 1]`, ortogonalidad $R^T R = I_3$ y $\det(R) = 1$).
* Para pruebas de visualización (`plotting.py`), utilizar un backend no interactivo de Matplotlib (`Agg`) y `show=False` para evitar bloqueos en ejecución automatizada, comprobando además que la función no mute los arreglos de entrada.
* Nunca modificar una fórmula matemática correcta para forzar que pase una prueba mal planteada.

## 9. Reglas de Documentación

* Mantener `README.md`, `docs/caso_de_estudio.md`, `docs/auditoria_inicial.md`, `docs/bitacora_ia.md` y `docs/informe_final.md` sincronizados con el estado real del repositorio.
* No documentar módulos, scripts o funciones que no existan realmente en el árbol de archivos.
* Registrar con transparencia qué herramienta de IA (Codex, Google Antigravity / Gemini, etc.) intervino en cada tarea.

## 10. Reglas de Git

* No trabajar directamente sobre la rama `main` para nuevos desarrollos; utilizar ramas descriptivas (`feature/...` o `codex/...`).
* Realizar commits atómicos, con mensajes claros y descriptivos.
* Antes de cada commit: revisar `git status`, inspeccionar `git diff`, ejecutar `python -m pytest -v` y comprobar que `notebooks/00_mini_taller_original.ipynb` no presenta modificaciones.
* Prohibido ejecutar comandos destructivos (`git reset --hard`, `git clean -fd`, `git push --force`).

## 11. Reglas de Seguridad

* No almacenar, leer ni publicar contraseñas, tokens, claves API, archivos `.env` ni información personal sensible.
* Nunca versionar la carpeta del entorno virtual (`.venv/`) ni cachés locales (`__pycache__/`, `.pytest_cache/`).

## 12. Restricciones Obligatorias para Agentes de IA

Todo agente de programación que opere sobre este repositorio debe cumplir estrictamente estas 9 reglas:

1. **Inspeccionar antes de modificar:** Leer los archivos existentes, el estado de Git y las pruebas antes de proponer cualquier cambio.
2. **Hacer cambios pequeños:** Aplicar modificaciones puntuales, atómicas y fáciles de auditar por un revisor humano.
3. **No modificar matemáticas centrales sin autorización:** Respetar íntegramente las definiciones matriciales en $SE(3)$ y la cinemática del notebook original.
4. **No duplicar código:** Reutilizar las funciones del paquete `src/melfa_kinematics/` en lugar de copiar definiciones.
5. **Ejecutar pruebas:** Correr `python -m pytest -v` tras cada cambio y reportar únicamente resultados reales.
6. **Revisar los diffs:** Inspeccionar `git diff` para asegurar que no se introdujeron cambios colaterales ni archivos binarios accidentales.
7. **Documentar decisiones:** Registrar el propósito, alcance y verificación de cada cambio en la documentación del proyecto y en `docs/bitacora_ia.md`.
8. **No hacer commits o pushes sin autorización:** Detenerse y solicitar confirmación explícita del usuario antes de registrar commits o publicar ramas en GitHub.
9. **No integrar cambios sin revisión humana:** Ninguna rama o Pull Request debe fusionarse (`merge`) hacia `main` sin validación y aprobación humana previa.
