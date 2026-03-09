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
- **Decisión:** El equipo principal está conformado por PhD. Ivan Ramirez (Director DIDI), MSc. Andreé Vitonera y MSc. Luiggi Solano como colaboradores en GitHub.
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

## Registro 007: Eliminación de Prioridades A Priori
- **Fecha:** 2026-02-09
- **Estado:** 🟢 Aprobada
- **Decisión:** Se eliminan las prioridades predefinidas (FCA Alta, FCE Media, etc.). Los datos determinarán qué facultades tienen mayor potencial.
- **Justificación:** Director indica que establecer prioridades antes del análisis sesga los resultados.
- **Responsable:** PhD. Ivan Ramirez

---

## Registro 008: Metodología de Dos Clusters
- **Fecha:** 2026-02-09
- **Estado:** 🟢 Aprobada
- **Decisión:** Se implementarán **dos enfoques de clustering**:
  1. **Cluster IPPC:** Por percentiles de productividad individual (A-Élite, B-Consolidados, C-En Desarrollo, D-Sin Actividad)
  2. **Cluster Temático:** Agrupación de artículos por afinidad en títulos, ponderado por nivel de impacto (Q1 > Q2 > Q3 > Q4 > Sin Cuartil)
- **Justificación:** Director: "No es lo mismo tener 100 artículos Latindex sobre banano que 50 Q1 sobre bioquímica". La fortaleza temática ponderada revela capacidades reales.
- **Responsable:** PhD. Ivan Ramirez + Equipo

---

## Registro 009: Metodología de Clustering Temático
- **Fecha:** 2026-02-20
- **Estado:** 🟢 Implementada
- **Decisión:** Se implementó el clustering temático usando:
  - **Vectorización:** TF-IDF con stopwords en español + términos académicos genéricos, bigramas, `max_features=500`
  - **Algoritmo:** K-Means con selección automática de K por Silhouette Score (K=20 óptimo)
  - **Ponderación aprobada:** Q1=1.0, Q2=0.9, Q3=0.8, Q4=0.7, NO APLICA/Latindex 2.0=0.2
  - **Resultado:** 20 clusters temáticos, 3,262 artículos analizados
- **Hallazgos clave:**
  - Cluster con mayor promedio de impacto: artículos en inglés (promedio 0.623, 83 Q1)
  - Áreas temáticas diferenciadas: Banano/Agroalimentario, Gestión Empresarial, Educación Superior, Enfermería, Salud Pública
  - 87.3% de artículos sin cuartil Scopus/WoS
- **Archivos generados:** `clusters_tematicos.csv`, `resumen_clusters.csv`, `clusters_por_linea.csv`, visualizaciones en `figuras/`
- **Responsable:** PhD. Ivan Ramirez + Equipo

---

## Registro 010: Clasificación Experimental vs Bibliográfica
- **Fecha:** 2026-03-09
- **Estado:** 🟢 Implementada
- **Decisión:** Se implementó un **clasificador léxico NLP** que separa los 2,919 artículos en:
  1. **Experimental (47.0%):** Investigaciones con trabajo de laboratorio, campo o clínico.
  2. **Ciencias Sociales/Humanísticas (41.4%):** Investigaciones teóricas, documentales, socioeconómicas.
  3. **Revisiones Bibliográficas (11.6%):** Meta-análisis, revisiones sistemáticas, estados del arte.
- **Justificación:** La investigación experimental requiere presupuestos exponencialmente mayores (laboratorios, reactivos, equipos). Agruparla permite justificar asignaciones presupuestarias diferenciadas.
- **Responsable:** PhD. Ivan Ramirez + Equipo

---

## Registro 011: Sistema de Dos Vías (Centros + Observatorios)
- **Fecha:** 2026-03-09
- **Estado:** 🟢 Implementada
- **Decisión:** Se creó un **sistema de dos vías** para la propuesta de Centros:
  - **Vía A - Centros de Investigación Científico-Experimentales:** Para artículos experimentales. Alto presupuesto (laboratorios, reactivos, equipos).
  - **Vía B - Observatorios de Ciencias Sociales y Humanísticas:** Para artículos sociales/teóricos. Gestión ágil (software, encuestas, bases de datos).
- **Archivos generados:** `produccion_clasificada_definitiva.csv`, `impacto_por_centro_definitivo.csv`, `REPORTE_FINAL_CENTROS.txt`
- **Responsable:** PhD. Ivan Ramirez + Equipo

---
