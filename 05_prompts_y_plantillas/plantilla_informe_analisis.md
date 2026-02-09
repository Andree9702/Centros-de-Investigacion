# 📊 Plantilla de Informe de Análisis de Viabilidad

> **Instrucciones:** Complete este informe tras ejecutar el análisis de IPPC. Incluya gráficos y tablas generados.

---

**FACULTAD ANALIZADA:** [Nombre de la Facultad]  
**FECHA DE ANÁLISIS:** [Fecha]  
**ANALISTA:** [Nombre del responsable]  
**VERSIÓN:** 1.0

---

## 1. RESUMEN EJECUTIVO

### Hallazgos Principales

1. [Hallazgo 1 - ej. "La FCA cuenta con masa crítica suficiente para un Centro"]
2. [Hallazgo 2]
3. [Hallazgo 3]

### Recomendación

🟢 **Viable para creación inmediata**  
🟡 **Viable con fortalecimiento previo**  
🔴 **No viable actualmente**

---

## 2. DATOS ANALIZADOS

| Parámetro | Valor |
|-----------|-------|
| Archivo fuente | `01_datos/raw/[nombre_archivo].xlsx` |
| Registros totales | [N] |
| Registros válidos | [N] |
| Registros excluidos | [N] |
| Fecha de corte de datos | [Fecha] |

---

## 3. ESTADÍSTICAS DESCRIPTIVAS

### 3.1. Resumen General de la Facultad

| Indicador | Valor |
|-----------|-------|
| Total de docentes | [N] |
| Docentes tiempo completo | [N] |
| Docentes con PhD | [N] |
| Investigadores acreditados SENESCYT | [N] |
| IPPC promedio | [X.XX] |
| IPPC mediana | [X.XX] |
| Desviación estándar IPPC | [X.XX] |
| IPPC mínimo | [X.XX] |
| IPPC máximo | [X.XX] |

### 3.2. Comparación con Promedio Institucional

| Facultad | IPPC Promedio | vs. Promedio Institucional |
|----------|---------------|----------------------------|
| [Facultad analizada] | [X.XX] | +/- [X]% |
| Promedio Institucional | [X.XX] | — |

---

## 4. CLUSTERING DE DOCENTES

### 4.1. Distribución por Clusters

| Cluster | Criterio IPPC | N° Docentes | % del Total |
|---------|---------------|-------------|-------------|
| A - Élite | ≥ Percentil 90 | [N] | [%] |
| B - Consolidados | P50 - P89 | [N] | [%] |
| C - En Desarrollo | P25 - P49 | [N] | [%] |
| D - Sin Actividad | < P25 | [N] | [%] |

### 4.2. Índice de Masa Crítica (IMC)

**Fórmula:** `IMC = (N_A × 3) + (N_B × 2) + (N_C × 1)`

| Componente | Valor | Ponderación | Subtotal |
|------------|-------|-------------|----------|
| Cluster A | [N] | × 3 | [N×3] |
| Cluster B | [N] | × 2 | [N×2] |
| Cluster C | [N] | × 1 | [N×1] |
| **IMC Total** | | | **[SUMA]** |

---

## 5. EVALUACIÓN DE CRITERIOS MÍNIMOS

| Criterio | Umbral | Valor Real | Cumple |
|----------|--------|------------|--------|
| Investigadores acreditados SENESCYT | ≥ 5 | [N] | ✅ / ❌ |
| Doctores (PhD) | ≥ 8 | [N] | ✅ / ❌ |
| Investigadores Cluster A | ≥ 3 | [N] | ✅ / ❌ |
| IPPC promedio ≥ mediana institucional | [X.XX] | [Y.YY] | ✅ / ❌ |

**Criterios cumplidos:** [X] de 4

**Clasificación:**
- 🟢 **Lista para Centro** (4/4 criterios)
- 🟡 **Casi Lista** (3/4 criterios)
- 🔴 **Requiere Fortalecimiento** (<3 criterios)

---

## 6. INVESTIGADORES DESTACADOS (Cluster A)

| # | Nombre | Categoría SENESCYT | IPPC | Scopus | WoS |
|---|--------|-------------------|------|--------|-----|
| 1 | [Nombre] | [Categoría] | [IPPC] | [N] | [N] |
| 2 | [Nombre] | [Categoría] | [IPPC] | [N] | [N] |
| 3 | [Nombre] | [Categoría] | [IPPC] | [N] | [N] |

---

## 7. VISUALIZACIONES

*Incluir los gráficos generados (pegar imágenes o referenciar archivos)*

### 7.1. Boxplot de IPPC
![Boxplot IPPC](../02_analisis/resultados/boxplot_ippc_[facultad].png)

### 7.2. Distribución de Clusters
![Distribución Clusters](../02_analisis/resultados/clusters_[facultad].png)

---

## 8. LÍNEAS DE INVESTIGACIÓN IDENTIFICADAS

*Basado en la producción de los investigadores Cluster A y B*

| # | Línea Propuesta | Docentes Vinculados | Publicaciones |
|---|-----------------|---------------------|---------------|
| 1 | [Línea] | [N] | [N] |
| 2 | [Línea] | [N] | [N] |
| 3 | [Línea] | [N] | [N] |

---

## 9. RECOMENDACIONES

### Si la facultad es 🟢 Viable:
1. Proceder con la elaboración del expediente técnico
2. Convocar a investigadores Cluster A y B
3. Definir líneas de investigación prioritarias

### Si la facultad es 🟡 Casi Viable:
1. Identificar brechas específicas
2. Plan de fortalecimiento (6-12 meses)
3. Re-evaluar tras cumplir criterios

### Si la facultad es 🔴 No Viable:
1. Documentar razones
2. Proponer alternativas (grupos de investigación, alianzas)
3. Establecer plan de desarrollo a mediano plazo

---

## 10. ANEXOS

- [ ] Datos procesados (`01_datos/clean/[archivo].csv`)
- [ ] Código de análisis (`02_analisis/notebooks/[notebook].ipynb`)
- [ ] Lista completa de docentes con IPPC
- [ ] Gráficos adicionales

---

*Informe generado según metodología del proyecto Centros de Investigación*
