# 📊 Diccionario de Datos

Este documento define la estructura esperada para los conjuntos de datos utilizados en el análisis de viabilidad de Centros de Investigación.

---

## Fuentes de Datos

| Fuente | Descripción | Formato | Ubicación |
|--------|-------------|---------|-----------|
| Nómina Docente | Lista oficial de docentes por facultad | Excel/CSV | `01_datos/raw/` |
| Registro SENESCYT | Investigadores acreditados | Excel/CSV | `01_datos/raw/` |
| IPPC Institucional | Índice Ponderado de Producción Científica | Excel | `01_datos/raw/` |

---

## Tabla Principal: Docentes con IPPC

**Archivo:** `docentes_ippc.xlsx` o `docentes_ippc.csv`

| Campo | Tipo | Descripción | Ejemplo | Obligatorio | Valores Permitidos |
|-------|------|-------------|---------|-------------|-------------------|
| `id_docente` | String/Int | Identificador único (cédula o código) | `0912345678` | ✅ Sí | Cédula ecuatoriana (10 dígitos) |
| `nombres` | String | Nombres completos del docente | `Juan Carlos Pérez López` | ✅ Sí | Texto libre |
| `facultad` | String | Facultad de adscripción | `FCA` | ✅ Sí | `FCA`, `FCQS`, `FCI`, `FCE`, `FCS`, etc. |
| `carrera` | String | Carrera donde dicta | `Contabilidad` | ❌ No | Texto libre |
| `categoria` | String | Categoría docente | `Principal` | ✅ Sí | `Principal`, `Agregado`, `Auxiliar`, `Ocasional` |
| `dedicacion` | String | Régimen de dedicación | `Tiempo Completo` | ✅ Sí | `Tiempo Completo`, `Medio Tiempo`, `Tiempo Parcial` |
| `tiene_doctorado` | Booleano | Si posee grado de Doctor (PhD) | `Sí` | ✅ Sí | `Sí`, `No` |
| `acreditado_senescyt` | Booleano | Si está acreditado como investigador SENESCYT | `Sí` | ✅ Sí | `Sí`, `No` |
| `categoria_senescyt` | String | Categoría de investigador SENESCYT | `Titular` | ❌ No | `Titular`, `Agregado`, `Auxiliar`, `No aplica` |
| `ippc` | Float | Índice Ponderado de Producción Científica | `3.75` | ✅ Sí | Número decimal ≥ 0 |
| `articulos_scopus` | Int | Artículos indexados en Scopus | `5` | ❌ No | Entero ≥ 0 |
| `articulos_wos` | Int | Artículos indexados en Web of Science | `3` | ❌ No | Entero ≥ 0 |
| `articulos_latindex` | Int | Artículos en revistas Latindex | `8` | ❌ No | Entero ≥ 0 |
| `libros` | Int | Libros publicados con ISBN | `2` | ❌ No | Entero ≥ 0 |
| `capitulos_libro` | Int | Capítulos de libro publicados | `4` | ❌ No | Entero ≥ 0 |
| `tesis_maestria` | Int | Tesis de maestría dirigidas | `6` | ❌ No | Entero ≥ 0 |
| `tesis_doctorado` | Int | Tesis doctorales dirigidas | `1` | ❌ No | Entero ≥ 0 |
| `proyectos_investigacion` | Int | Proyectos de investigación liderados | `3` | ❌ No | Entero ≥ 0 |
| `grupo_investigacion` | String | Nombre del grupo al que pertenece | `GI-Finanzas Sostenibles` | ❌ No | Texto libre |
| `linea_investigacion` | String | Línea principal de investigación | `Contabilidad Ambiental` | ❌ No | Texto libre |
| `email` | String | Correo electrónico institucional | `jperez@universidad.edu.ec` | ❌ No | Email válido |

---

## Tabla Secundaria: Asignaturas

**Archivo:** `asignaturas.xlsx` o `asignaturas.csv`

| Campo | Tipo | Descripción | Ejemplo | Obligatorio |
|-------|------|-------------|---------|-------------|
| `codigo_asignatura` | String | Código único de la asignatura | `CONT-101` | ✅ Sí |
| `nombre` | String | Nombre de la asignatura | `Contabilidad General I` | ✅ Sí |
| `id_docente` | String/Int | Cédula del docente (FK) | `0912345678` | ✅ Sí |
| `periodo` | String | Período académico | `2025-2S` | ✅ Sí |
| `horas_teoria` | Int | Horas de teoría semanales | `2` | ✅ Sí |
| `horas_practica` | Int | Horas de práctica semanales | `2` | ✅ Sí |
| `paralelos` | Int | Número de paralelos asignados | `3` | ❌ No |

---

## Reglas de Validación

1. **Cédula ecuatoriana:** Debe tener exactamente 10 dígitos numéricos.
2. **IPPC:** No puede ser negativo. Valor típico entre 0 y 20.
3. **Booleanos:** Solo aceptan `Sí`/`No` o `1`/`0` o `TRUE`/`FALSE`.
4. **Facultad:** Debe coincidir con las siglas oficiales de la institución.
5. **Sin duplicados:** `id_docente` debe ser único en cada archivo.

---

## Campos Calculados (generados en análisis)

| Campo | Fórmula | Descripción |
|-------|---------|-------------|
| `cluster` | Percentil de IPPC | Clasificación: A(≥P90), B(P50-89), C(P25-49), D(<P25) |
| `produccion_total` | Scopus + WoS + Latindex + Libros | Suma de toda la producción indexada |
| `es_masa_critica` | cluster IN (A, B) | Indica si cuenta como masa crítica |

---

## Ejemplo de Registro

```csv
id_docente,nombres,facultad,categoria,dedicacion,tiene_doctorado,acreditado_senescyt,categoria_senescyt,ippc,articulos_scopus,articulos_wos
0912345678,Juan Carlos Pérez López,FCA,Principal,Tiempo Completo,Sí,Sí,Titular,4.25,6,3
```
