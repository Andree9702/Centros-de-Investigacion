# 📊 Diccionario de Datos - UTMACH

Este documento define la estructura esperada para los conjuntos de datos de IPPC de la Universidad Técnica de Machala.

---

## Fuentes de Datos

| Fuente | Descripción | Formato | Proveedor |
|--------|-------------|---------|-----------|
| Excel IPPC | Índice Ponderado de Producción Científica de todos los docentes | Excel | DIDI |
| Nómina Docente | Lista oficial de docentes por facultad | Excel/CSV | Talento Humano |
| Registro SENESCYT | Investigadores acreditados | Excel/CSV | DIDI |

---

## Facultades de la UTMACH

| Código | Nombre Completo |
|--------|-----------------|
| `FCA` | Facultad de Ciencias Agropecuarias |
| `FCQS` | Facultad de Ciencias Químicas y de la Salud |
| `FCE` | Facultad de Ciencias Empresariales |
| `FIC` | Facultad de Ingeniería Civil |
| `FCS` | Facultad de Ciencias Sociales |

---

## Tabla Principal: Docentes con IPPC

**Archivo esperado:** `ippc_docentes_utmach.xlsx` o similar

| Campo | Tipo | Descripción | Ejemplo | Obligatorio | Valores Permitidos |
|-------|------|-------------|---------|-------------|-------------------|
| `id_docente` | String/Int | Identificador único (cédula o código) | `0912345678` | ✅ Sí | Cédula ecuatoriana (10 dígitos) |
| `nombres` | String | Nombres completos del docente | `Juan Carlos Pérez López` | ✅ Sí | Texto libre |
| `facultad` | String | Facultad de adscripción | `FCA` | ✅ Sí | `FCA`, `FCQS`, `FCE`, `FIC`, `FCS` |
| `carrera` | String | Carrera donde dicta | `Agronomía` | ❌ No | Texto libre |
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
| `grupo_investigacion` | String | Nombre del grupo al que pertenece | `GI-Agricultura Sostenible` | ❌ No | Texto libre |
| `linea_investigacion` | String | Línea principal de investigación | `Producción Agrícola` | ❌ No | Texto libre |
| `email` | String | Correo electrónico institucional | `jperez@utmachala.edu.ec` | ❌ No | Email válido |

---

## Reglas de Validación

1. **Cédula ecuatoriana:** Exactamente 10 dígitos numéricos.
2. **IPPC:** No puede ser negativo. Valor típico entre 0 y 20.
3. **Facultad:** Solo valores: `FCA`, `FCQS`, `FCE`, `FIC`, `FCS`.
4. **Sin duplicados:** `id_docente` debe ser único.

---

## Campos Calculados (generados en análisis)

| Campo | Fórmula | Descripción |
|-------|---------|-------------|
| `cluster` | Percentil de IPPC | A(≥P90), B(P50-89), C(P25-49), D(<P25) |
| `produccion_total` | Scopus + WoS + Latindex + Libros | Suma de producción indexada |
| `es_masa_critica` | cluster IN (A, B) | Si cuenta como masa crítica |

---

## Ejemplo de Registro

```csv
id_docente,nombres,facultad,categoria,dedicacion,tiene_doctorado,acreditado_senescyt,ippc
0912345678,Juan Carlos Pérez López,FCA,Principal,Tiempo Completo,Sí,Sí,4.25
```
