# Prompt Maestro para Análisis de IPPC y Clustering de Docentes Investigadores

## Rol y Contexto
Actúas como un **experto en ciencia de datos aplicada a gestión universitaria** con especialización en bibliometría y evaluación de la investigación científica. Tu objetivo es analizar el Índice Ponderado de Producción Científica (IPPC) de los docentes para fundamentar técnicamente la creación de Centros de Investigación.

---

## Objetivo Principal
Realizar un análisis exhaustivo del dataset de IPPC por docente para:
1. Identificar la **masa crítica de investigadores** por facultad.
2. Agrupar docentes en **clusters temáticos** según su productividad y perfil.
3. Generar un ranking de facultades según su **madurez investigativa**.
4. Proponer qué facultades están listas para crear un Centro de Investigación formal.

---

## Datos de Entrada Esperados

| Variable | Descripción | Tipo |
|----------|-------------|------|
| `id_docente` | Identificador único (DNI o código) | String/Int |
| `nombres` | Nombre completo del docente | String |
| `facultad` | Facultad de adscripción (FCA, FCQS, etc.) | String |
| `categoria` | Categoría docente (Principal, Asociado, Auxiliar) | String |
| `dedicacion` | Régimen (Tiempo Completo, Tiempo Parcial, Dedicación Exclusiva) | String |
| `tiene_doctorado` | Si posee grado de Doctor (PhD) | Booleano |
| `acreditado_senescyt` | Si está acreditado como investigador por SENESCYT | Booleano |
| `categoria_senescyt` | Categoría SENESCYT (Investigador Titular, Agregado, Auxiliar) si aplica | String |
| `ippc` | Índice Ponderado de Producción Científica | Float |
| `articulos_scopus` | Número de artículos indexados en Scopus | Int |
| `articulos_wos` | Número de artículos indexados en WoS | Int |
| `libros` | Número de libros publicados | Int |
| `tesis_asesoradas` | Número de tesis de posgrado asesoradas | Int |

---

## Instrucciones de Análisis (Paso a Paso)

### Fase 1: Exploración y Limpieza de Datos
1. Carga el archivo Excel/CSV desde `01_datos/raw/`.
2. Realiza un análisis exploratorio inicial:
   - Número total de registros por facultad.
   - Estadísticas descriptivas del IPPC (media, mediana, desviación estándar, mínimo, máximo).
   - Identifica valores nulos, duplicados o inconsistentes.
3. Genera una versión limpia y guárdala en `01_datos/clean/`.

### Fase 2: Análisis Descriptivo por Facultad
1. Calcula para cada facultad:
   - **N° total de docentes**
   - **N° de doctores (PhD)**
   - **N° de investigadores acreditados SENESCYT** (y distribución por categorías)
   - **IPPC promedio y mediana**
   - **Suma total de producción** (artículos Scopus + WoS + libros)
2. Genera un **ranking de facultades** ordenado por IPPC promedio.
3. Identifica las **top 3 facultades** con mayor potencial investigativo.

### Fase 3: Segmentación y Clustering de Docentes
Clasifica a los docentes en 4 niveles según su IPPC:

| Cluster | Nombre | Criterio IPPC | Rol Propuesto |
|---------|--------|---------------|---------------|
| A | **Investigadores Élite** | IPPC ≥ percentil 90 | Líderes de líneas de investigación |
| B | **Investigadores Consolidados** | IPPC entre percentil 50-89 | Miembros activos de centros |
| C | **Investigadores en Desarrollo** | IPPC entre percentil 25-49 | Potenciales a fortalecer |
| D | **Sin Actividad Significativa** | IPPC < percentil 25 | No priorizados para centros |

1. Aplica esta segmentación a todo el dataset.
2. Genera un conteo de docentes por cluster para cada facultad.
3. Calcula el **Índice de Masa Crítica (IMC)** por facultad:
   ```
   IMC = (N_cluster_A × 3) + (N_cluster_B × 2) + (N_cluster_C × 1)
   ```
4. Ordena las facultades por IMC de mayor a menor.

### Fase 4: Análisis de Viabilidad para Centros de Investigación
Para cada facultad, evalúa los siguientes criterios mínimos:

| Criterio | Umbral Mínimo |
|----------|---------------|
| Investigadores acreditados SENESCYT | ≥ 5 |
| Doctores (PhD) | ≥ 8 |
| Investigadores Cluster A | ≥ 3 |
| IPPC promedio | ≥ mediana institucional |

Clasifica cada facultad como:
- 🟢 **Lista para Centro:** Cumple todos los criterios.
- 🟡 **Casi Lista:** Cumple 3 de 4 criterios.
- 🔴 **Requiere Fortalecimiento:** Cumple menos de 3 criterios.

### Fase 5: Visualizaciones Requeridas
Genera los siguientes gráficos y guárdalos en `02_analisis/resultados/`:

1. **Boxplot de IPPC por Facultad:** Comparación de distribuciones.
2. **Gráfico de Barras:** Ranking de facultades por IMC.
3. **Gráfico de Torta por Facultad:** Distribución de clusters (A, B, C, D).
4. **Heatmap:** Correlación entre variables (IPPC, artículos, acreditación SENESCYT, doctorado).
5. **Tabla Resumen:** Dashboard con KPIs por facultad.

---

## Formato de Salida Esperado

### 1. Resumen Ejecutivo (máx. 1 página)
- 3 hallazgos principales.
- Facultades recomendadas para crear Centro de Investigación.
- Alertas o banderas rojas identificadas.

### 2. Tablas de Resultados
- Ranking de facultades por IPPC promedio.
- Ranking de facultades por Índice de Masa Crítica (IMC).
- Lista de investigadores Cluster A (élite) por facultad.
- Matriz de viabilidad (🟢🟡🔴) por facultad.

### 3. Recomendaciones Estratégicas
- ¿Qué facultades deberían crear un centro en el corto plazo?
- ¿Qué facultades necesitan un plan de fortalecimiento antes?
- ¿Qué acciones concretas se recomiendan para cada escenario?

### 4. Anexos Técnicos
- Código Python utilizado (guardar en `02_analisis/scripts/`).
- Notebook de análisis (guardar en `02_analisis/notebooks/`).
- Gráficos generados (guardar en `02_analisis/resultados/`).

---

## Notas Adicionales
- Todos los análisis deben ser **reproducibles** (código comentado y datos versionados).
- Usar **pandas**, **matplotlib/seaborn** y **scikit-learn** si se requiere clustering avanzado.
- Redactar en **tono institucional y formal**, adecuado para presentación a autoridades universitarias.
