# 📊 Módulo de Análisis - Guía de Uso

Este directorio contiene todos los análisis estadísticos del proyecto de Centros de Investigación.

---

## 📁 Estructura

```
02_analisis/
├── notebooks/      # Jupyter notebooks de análisis
├── scripts/        # Scripts Python reutilizables
├── resultados/     # Gráficos, tablas e informes generados
└── README.md       # Esta guía
```

---

## 🚀 Cómo Ejecutar el Análisis

### Requisitos Previos
```bash
pip install pandas matplotlib seaborn scikit-learn openpyxl jupyter
```

### Flujo de Trabajo

1. **Colocar datos** en `01_datos/raw/`
2. **Ejecutar notebook** de limpieza → genera datos en `01_datos/clean/`
3. **Ejecutar notebook** de análisis → genera resultados en `02_analisis/resultados/`

---

## 📓 Notebooks Esperados

| Notebook | Descripción | Input | Output |
|----------|-------------|-------|--------|
| `01_limpieza_datos.ipynb` | Limpieza y validación de datos crudos | `01_datos/raw/*.xlsx` | `01_datos/clean/*.csv` |
| `02_analisis_descriptivo.ipynb` | Estadísticas por facultad | `01_datos/clean/*.csv` | Tablas resumen |
| `03_clustering_ippc.ipynb` | Clasificación en clusters A/B/C/D | `01_datos/clean/*.csv` | Rankings, gráficos |
| `04_viabilidad_centros.ipynb` | Evaluación de criterios mínimos | Resultados anteriores | Matriz de viabilidad |

---

## 📈 Outputs Esperados

### Gráficos (guardar en `resultados/`)
- `boxplot_ippc_por_facultad.png`
- `ranking_imc_facultades.png`
- `distribucion_clusters.png`
- `heatmap_correlaciones.png`

### Tablas (guardar en `resultados/`)
- `ranking_facultades_ippc.csv`
- `ranking_facultades_imc.csv`
- `investigadores_cluster_a.csv`
- `matriz_viabilidad.csv`

### Informes
- `informe_viabilidad_fca.pdf`
- `informe_viabilidad_fcqs.pdf`

---

## 🔧 Scripts Útiles

Los scripts en `scripts/` pueden importarse en los notebooks:

```python
from scripts.utils_ippc import calcular_clusters, calcular_imc
```

---

## 📞 Soporte

Para dudas sobre el análisis, contactar a la Dirección de Investigación.
