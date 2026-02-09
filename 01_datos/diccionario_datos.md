# Diccionario de Datos

Este documento define la estructura esperada para los conjuntos de datos de docentes y asignaturas.

## Tabla: Docentes (`docentes.csv` / `docentes.xlsx`)

| Campo | Tipo de Dato | Descripción | Ejemplo | Obligatorio |
|-------|--------------|-------------|---------|-------------|
| `id_docente` | String/Int | Identificador único del docente (DNI o Código) | `12345678` | Sí |
| `nombres` | String | Nombres completos del docente | `Juan Pérez` | Sí |
| `facultad` | String | Facultad de adscripción | `FCA` | Sí |
| `categoria` | String | Categoría docente (Principal, Asociado, Auxiliar) | `Principal` | Sí |
| `dedicacion` | String | Régimen de dedicación (TC, TP, DE) | `Tiempo Completo` | Sí |
| `es_renacyt` | Booleano | Si el docente está calificado en RENACYT | `Sí`/`No` | Sí |
| `grupo_investigacion`| String | Nombre del grupo de investigación al que pertenece | `GI-Finanzas` | No |

## Tabla: Asignaturas (`asignaturas.csv` / `asignaturas.xlsx`)

| Campo | Tipo de Dato | Descripción | Ejemplo | Obligatorio |
|-------|--------------|-------------|---------|-------------|
| `codigo_asignatura` | String | Código único de la asignatura | `CONT-101` | Sí |
| `nombre` | String | Nombre de la asignatura | `Contabilidad I` | Sí |
| `id_docente` | String/Int | ID del docente que dicta la asignatura (FK) | `12345678` | Sí |
| `semestre` | String | Semestre académico | `2024-I` | Sí |
| `horas_teoria` | Int | Horas de teoría semanales | `2` | Sí |
| `horas_practica` | Int | Horas de práctica semanales | `2` | Sí |
