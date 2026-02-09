# 📅 Hoja de Ruta (Roadmap) - Centros de Investigación UTMACH

> **Última actualización:** 09 Febrero 2026  
> **Responsable:** DIDI - PhD. Ivan Ramirez  
> **Colaboradores:** MSc. Andreé Vitonera, MSc. Luiggi Solano

---

## 🎯 Objetivo del Proyecto

Analizar el IPPC y la **producción científica** de **todos los docentes de la UTMACH** para tomar decisiones basadas en datos sobre la creación de **Centros de Investigación**.

> [!IMPORTANT]
> **Directriz del Director (09-Feb-2026):** No establecer prioridades a priori. Los datos revelarán las fortalezas.

### Facultades a Analizar

| Sigla | Facultad |
|-------|----------|
| FCA | Facultad de Ciencias Agropecuarias |
| FCQS | Facultad de Ciencias Químicas y de la Salud |
| FCE | Facultad de Ciencias Empresariales |
| FIC | Facultad de Ingeniería Civil |
| FCS | Facultad de Ciencias Sociales |

---

## Fase A: Diagnóstico y Datos
**Fecha objetivo:** Febrero 2026

| # | Tarea | Estado |
|---|-------|--------|
| A.1 | Recepción de Excel IPPC (1, 2, 3 años) | ✅ Completo |
| A.2 | Recepción de Excel Producción Científica | ✅ Completo |
| A.3 | Recepción de Excel Grupos de Investigación | ✅ Completo |
| A.4 | Limpieza y estructuración de datos | ✅ Completo |
| A.5 | Validación de datos con DIDI | ⏳ Pendiente |

**Entregable:** `01_datos/clean/` ✅

---

## Fase B: Análisis de Viabilidad
**Fecha objetivo:** Febrero-Marzo 2026

| # | Tarea | Estado |
|---|-------|--------|
| B.1 | Análisis descriptivo IPPC por facultad | ✅ Completo |
| B.2 | **Clustering IPPC** (Élite, Consolidados, En Desarrollo) | ✅ Completo |
| B.3 | **🆕 Clustering Temático** por títulos de artículos | 🔄 En curso |
| B.4 | Ponderación de clusters por impacto (Q1-Q4) | 🔄 En curso |
| B.5 | Identificación de **Fortalezas Temáticas** | ⏳ Pendiente |
| B.6 | Cálculo del Índice de Masa Crítica (IMC) | ⏳ Pendiente |
| B.7 | Ranking de facultades por potencial | ⏳ Pendiente |

**Entregable:** Informe de viabilidad con matriz de decisión

---

## Fase C: Propuesta de Centros
**Fecha objetivo:** Marzo 2026

| # | Tarea | Estado |
|---|-------|--------|
| C.1 | Elaborar propuestas técnicas por facultad | ⏳ |
| C.2 | Definición de líneas de investigación | ⏳ |
| C.3 | Presentación a Consejo de Facultad | ⏳ |

---

## Fase D: Reglamentación
**Fecha objetivo:** Marzo-Abril 2026

| # | Tarea | Estado |
|---|-------|--------|
| D.1 | Revisión de normativa LOES, CES, Estatuto | ⏳ |
| D.2 | Redacción del Reglamento General | ⏳ |
| D.3 | Aprobación por Consejo Universitario | ⏳ |

---

## 📊 Datos Disponibles (Actualizado)

| Archivo | Registros | Descripción |
|---------|-----------|-------------|
| IPPC 3 años | 596 docentes | Índice ponderado por docente |
| Producción | 3,263 artículos | Títulos, cuartiles, líneas |
| Grupos | 65 grupos | Grupos de investigación activos |

### Distribución de Cuartiles
- **Q1:** 104 (3.2%)
- **Q2:** 85 (2.6%)
- **Q3:** 84 (2.6%)
- **Q4:** 128 (3.9%)
- **Sin Cuartil:** 2,847 (87.3%)

---

## ⚠️ Próxima Acción

> Ejecutar **Clustering Temático** usando NLP sobre los 3,263 títulos de artículos.
