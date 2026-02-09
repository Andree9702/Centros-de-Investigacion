# 📝 Bitácora de Decisiones

Este documento registra las decisiones clave tomadas durante el desarrollo del proyecto para asegurar la **trazabilidad** y la **justificación técnica**.

---

## Cómo Registrar una Decisión

Copie la siguiente plantilla y complete los campos:

```markdown
## Registro XXX: [Título de la Decisión]
- **Fecha:** AAAA-MM-DD
- **Estado:** 🟡 Propuesta | 🟢 Aprobada | 🔴 Rechazada | 🔵 Revisión
- **Decisión:** [Descripción clara de lo que se decidió]
- **Justificación:** [Por qué se tomó esta decisión]
- **Alternativas Consideradas:** [Opciones que se descartaron]
- **Responsable:** [Quién tomó o aprobó la decisión]
- **Impacto:** [Áreas o documentos afectados]

---
```

---

## Registro 001: Estructura de Datos Estandarizada
- **Fecha:** 2026-02-08
- **Estado:** 🟢 Aprobada
- **Decisión:** Se utilizará un formato estandarizado CSV/Excel para la ingesta de datos de docentes e IPPC.
- **Justificación:** Facilitar la lectura por scripts de Python y mantener interoperabilidad entre sistemas. Permite versionamiento en Git.
- **Alternativas Consideradas:** Base de datos SQL (descartada por complejidad), JSON (descartada por legibilidad).
- **Responsable:** Dirección de Investigación
- **Impacto:** `01_datos/`, `02_analisis/`

---

## Registro 002: Uso del Sistema SENESCYT
- **Fecha:** 2026-02-08
- **Estado:** 🟢 Aprobada
- **Decisión:** Toda referencia a acreditación de investigadores utilizará el sistema ecuatoriano SENESCYT, no RENACYT (Perú).
- **Justificación:** El proyecto se desarrolla en Ecuador bajo normativa de la Secretaría de Educación Superior, Ciencia, Tecnología e Innovación (SENESCYT).
- **Alternativas Consideradas:** Ninguna (requisito normativo).
- **Responsable:** Dirección de Investigación
- **Impacto:** Todos los documentos del proyecto.

---

## Registro 003: Metodología de Clustering por IPPC
- **Fecha:** 2026-02-08
- **Estado:** 🟢 Aprobada
- **Decisión:** Los docentes se clasificarán en 4 clusters según su IPPC: Élite (≥P90), Consolidados (P50-P89), En Desarrollo (P25-P49), Sin Actividad Significativa (<P25).
- **Justificación:** Permite identificar masa crítica de investigadores y priorizar recursos. Metodología basada en percentiles para adaptarse a cualquier distribución de datos.
- **Alternativas Consideradas:** Clasificación por número absoluto de publicaciones (descartada por no considerar contexto).
- **Responsable:** Dirección de Investigación
- **Impacto:** `02_analisis/`, `03_centros_propuestos/`

---

## Registro 004: Índice de Masa Crítica (IMC)
- **Fecha:** 2026-02-08
- **Estado:** 🟢 Aprobada
- **Decisión:** Se calculará un Índice de Masa Crítica por facultad usando la fórmula: `IMC = (N_cluster_A × 3) + (N_cluster_B × 2) + (N_cluster_C × 1)`
- **Justificación:** Pondera la calidad sobre la cantidad, dando mayor peso a investigadores de alto rendimiento.
- **Alternativas Consideradas:** Promedio simple de IPPC (descartado por no reflejar estructura de grupos).
- **Responsable:** Dirección de Investigación
- **Impacto:** `02_analisis/`, informes de viabilidad.

---
