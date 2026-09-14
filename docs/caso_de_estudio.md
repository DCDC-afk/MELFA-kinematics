# Caso de estudio: cinemática de un robot MELFA

## 1. Contexto

Este proyecto parte de un taller académico de cinemática directa en 3D aplicado a un robot industrial MELFA de 6 grados de libertad (GDL).

El material original está contenido en un notebook de Jupyter y constituye el punto de partida para organizar el trabajo como un repositorio técnico versionado con Git y GitHub.

## 2. Punto de partida

El notebook original reúne diferentes elementos relacionados con el estudio de la cinemática del robot.

Entre los elementos trabajados se encuentran:

* transformaciones homogéneas;
* representación y visualización de marcos de referencia en 3D;
* cinemática del robot;
* ejemplos numéricos;
* procedimientos relacionados con la posición y orientación del manipulador.

El notebook original se conserva sin modificar en:

```text id="4l6qvs"
notebooks/00_mini_taller_original.ipynb
```

Este archivo funciona como referencia para las siguientes etapas del proyecto.

## 3. Problema de organización

El material de un taller académico puede ser útil para aprender y experimentar, pero no necesariamente está organizado como una biblioteca de código reusable.

Por esta razón, el proyecto busca separar progresivamente:

1. el material original del taller;
2. la documentación del caso;
3. las funciones reutilizables;
4. las pruebas;
5. las visualizaciones.

La separación será progresiva y se realizará conservando como referencia el notebook original.

## 4. Objetivo del proyecto

El objetivo es convertir el material del taller en una estructura de proyecto que permita:

* estudiar la cinemática del robot;
* reutilizar funciones matemáticas;
* comprobar comportamientos mediante pruebas;
* documentar las decisiones tomadas;
* mantener una historia de cambios mediante Git;
* trabajar colaborativamente mediante GitHub.

## 5. Evolución prevista

El proyecto se desarrollará por etapas.

### Etapa 1 — Organización y Git

En la primera etapa se crea el repositorio local, se establece su estructura inicial, se incorpora el notebook original y se publica el proyecto en GitHub.

La estructura inicial es:

```text id="9h6zmx"
MELFA-kinematics/
├── README.md
├── docs/
│   └── caso_de_estudio.md
├── notebooks/
│   └── 00_mini_taller_original.ipynb
└── src/
```

### Etapa 2 — Modularización y pruebas

Posteriormente se creará un ambiente virtual y se registrarán las dependencias del proyecto.

Una primera pieza de código reutilizable será la correspondiente a las transformaciones:

* `Rx`;
* `Ry`;
* `Rz`;
* `Trans`.

Estas funciones se incorporarán progresivamente a:

```text id="6v0qkp"
src/melfa_kinematics/
```

También se crearán pruebas básicas para verificar identidades, traslaciones y una rotación conocida.

### Etapa 3 — Modularización guiada con Codex

Una vez comprendidos el repositorio, los commits, el ambiente virtual y las pruebas, se podrá utilizar Codex para tareas pequeñas y delimitadas.

Una primera tarea propuesta será extraer la función de visualización de marcos 3D a un módulo separado, sin modificar la matemática central del proyecto.

Los cambios generados por IA deberán revisarse mediante el diff y verificarse antes de integrarse.

## 6. Principios de trabajo

El proyecto seguirá estos principios:

* conservar el material original como referencia;
* realizar cambios pequeños y comprensibles;
* revisar los cambios antes de hacer commits;
* probar el código antes de integrarlo;
* documentar las decisiones relevantes;
* evitar modificaciones innecesarias;
* utilizar IA como apoyo y no como sustituto de la revisión técnica.

## 7. Estado actual

En la primera etapa ya se creó el repositorio local y se publicó su primer commit en GitHub.

El notebook original fue incorporado posteriormente a `notebooks/00_mini_taller_original.ipynb`.

El siguiente paso es revisar y versionar estos cambios para dejar completa la primera entrega.
