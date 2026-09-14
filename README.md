# MELFA Kinematics

Proyecto de estudio y organización de un taller académico de cinemática de un robot industrial MELFA de 6 grados de libertad (GDL).

## Propósito

Este repositorio toma como punto de partida un notebook académico de cinemática y lo organiza como un proyecto técnico versionado con Git y GitHub.

El objetivo no es solamente conservar el notebook, sino establecer una base que pueda evolucionar hacia una estructura más organizada, reutilizable y verificable.

El caso de estudio permite practicar:

* Git y GitHub.
* Organización de proyectos técnicos.
* Documentación.
* Separación entre material exploratorio y código reusable.
* Ambientes virtuales.
* Dependencias.
* Pruebas básicas.
* Modularización progresiva.

## Origen del proyecto

El punto de partida es un taller académico de cinemática directa en 3D de un robot tipo MELFA.

El notebook original reúne diferentes elementos relacionados con la cinemática, entre ellos transformaciones homogéneas, visualización 3D, cinemática directa, cinemática inversa y ejemplos numéricos.

El archivo original se conserva en:

```text
notebooks/00_mini_taller_original.ipynb
```

La intención es mantenerlo como referencia mientras las partes reutilizables se separan progresivamente en módulos.

## Estructura

```text
MELFA-kinematics/
│
├── README.md
│
├── docs/
│   └── caso_de_estudio.md
│
├── notebooks/
│   └── 00_mini_taller_original.ipynb
│
└── src/
```

### `README.md`

Presenta el propósito, origen y organización general del proyecto.

### `docs/`

Contiene la documentación del caso de estudio y las decisiones de organización del proyecto.

### `notebooks/`

Conserva el material original utilizado como punto de partida.

### `src/`

Está reservado para el código reusable que se irá extrayendo del notebook durante las siguientes etapas.

## Flujo de trabajo

El proyecto se desarrolla progresivamente:

1. Crear y organizar el repositorio local.
2. Versionar los cambios mediante commits.
3. Publicar los avances en GitHub mediante `push`.
4. Crear un ambiente virtual para el proyecto.
5. Registrar las dependencias.
6. Extraer pequeñas piezas reutilizables del notebook.
7. Verificar esas piezas mediante pruebas simples.
8. Incorporar Codex posteriormente para tareas pequeñas y revisables.

## Git y GitHub

En este proyecto se distingue entre:

* **Repositorio local:** la carpeta del proyecto en el computador.
* **Repositorio remoto:** la copia del proyecto alojada en GitHub.
* **Commit:** una versión registrada localmente.
* **Push:** publicación de los commits locales en el repositorio remoto.

## Estado actual

En esta primera etapa se creó el repositorio local, se organizó la estructura inicial, se incorporó el notebook original y se publicó el primer avance en GitHub.

La siguiente etapa estará enfocada en el ambiente virtual, las dependencias, la primera modularización y las pruebas básicas.

## Alcance futuro

La estructura podrá crecer posteriormente hacia temas como:

* visualización y animación,
* validación de resultados,
* control cinemático,
* planificación de trayectorias,
* dinámica.

## Uso responsable de IA

La IA, incluyendo Codex, se utilizará como herramienta de apoyo para tareas pequeñas y delimitadas.

Los cambios generados por IA deberán revisarse mediante el diff correspondiente y verificarse antes de integrarse al proyecto.

La responsabilidad final sobre el código y las decisiones del proyecto corresponde al estudiante.
