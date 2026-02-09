# 📝 Bitácora de Decisiones - UTMACH

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
- **Responsable:** [Quién tomó o aprobó la decisión]

---
```

---

## Registro 001: Estructura de Datos Estandarizada
- **Fecha:** 2026-02-08
- **Estado:** 🟢 Aprobada
- **Decisión:** Se utilizará un formato estandarizado CSV/Excel para la ingesta de datos de docentes e IPPC.
- **Justificación:** Facilitar la lectura por scripts de Python y mantener interoperabilidad entre sistemas.
- **Responsable:** DIDI - PhD. Ivan Ramirez

---

## Registro 002: Uso del Sistema SENESCYT
- **Fecha:** 2026-02-08
- **Estado:** 🟢 Aprobada
- **Decisión:** Toda referencia a acreditación de investigadores utilizará el sistema ecuatoriano SENESCYT.
- **Justificación:** El proyecto se desarrolla en Ecuador bajo normativa de la Secretaría de Educación Superior, Ciencia, Tecnología e Innovación.
- **Responsable:** DIDI

---

## Registro 003: Centros de Investigación Piloto
- **Fecha:** 2026-02-08
- **Estado:** 🟢 Aprobada
- **Decisión:** Se crearán inicialmente **dos centros piloto**: uno en la **FCA (Ciencias Agropecuarias)** y otro en la **FCQS (Ciencias Químicas y de la Salud)**.
- **Justificación:** Datos preliminares indican que estas facultades tienen mayor producción científica y actividad investigadora. La decisión final se tomará tras el análisis de clustering del IPPC.
- **Responsable:** PhD. Ivan Ramirez (Director DIDI)

---

## Registro 004: Metodología de Clustering por IPPC
- **Fecha:** 2026-02-08
- **Estado:** 🟢 Aprobada
- **Decisión:** Los docentes se clasificarán en 4 clusters según su IPPC: Élite (≥P90), Consolidados (P50-P89), En Desarrollo (P25-P49), Sin Actividad Significativa (<P25).
- **Justificación:** Permite identificar masa crítica de investigadores y priorizar recursos.
- **Responsable:** Equipo de análisis

---

## Registro 005: Equipo del Proyecto
- **Fecha:** 2026-02-08
- **Estado:** 🟢 Aprobada
- **Decisión:** El equipo principal está conformado por PhD. Ivan Ramirez (Director DIDI) y MSc. Luiggi Solano como colaboradores en GitHub.
- **Justificación:** Garantizar supervisión técnica y académica del proyecto.
- **Responsable:** Dirección de Investigación UTMACH

---

## Registro 006: Análisis de las 5 Facultades
- **Fecha:** 2026-02-08
- **Estado:** 🟢 Aprobada
- **Decisión:** Se analizará el IPPC de **todas las 5 facultades** de la UTMACH (FCA, FCQS, FCE, FIC, FCS) para tomar decisiones basadas en datos.
- **Justificación:** Aunque FCA y FCQS son las prioridades, el análisis completo permitirá identificar potencial oculto en otras facultades.
- **Responsable:** Equipo de análisis + DIDI

---
