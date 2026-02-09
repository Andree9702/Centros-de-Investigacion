# 🏛️ Proyecto: Creación y Reglamentación de Centros de Investigación

![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![Fase](https://img.shields.io/badge/Fase-A%20Diagnóstico-blue)
![Institución](https://img.shields.io/badge/País-Ecuador-red)

---

## 📋 Objetivo

Centralizar y gestionar la información, datos, análisis y documentación necesaria para la **creación, formalización y reglamentación** de los nuevos Centros de Investigación de la institución, inicialmente enfocados en:

- **FCA** - Facultad de Ciencias Administrativas
- **FCQS** - Facultad de Ciencias Químicas y de la Salud

---

## 🎯 Alcance

| Fase | Descripción | Estado |
|------|-------------|--------|
| **A. Datos** | Recopilación, limpieza y análisis de carga académica, líneas de investigación y producción científica | 🔄 En curso |
| **B. Análisis** | Evaluación de viabilidad, pertinencia y masa crítica (IPPC, clustering) | ⏳ Pendiente |
| **C. Propuestas** | Elaboración de expedientes técnicos para creación de centros | ⏳ Pendiente |
| **D. Normativa** | Redacción del Reglamento General de Centros de Investigación | ⏳ Pendiente |

---

## 📦 Entregables

1. ✅ Base de datos consolidada y limpia de docentes (IPPC por facultad)
2. 📊 Informes de análisis de pertinencia y viabilidad con clustering
3. 📄 Expedientes de creación para los Centros FCA y FCQS
4. 📜 Borrador final del Reglamento General de Centros de Investigación

---

## 📁 Estructura del Repositorio

```
📂 Centros de Investigación/
├── 📁 00_admin/              # Gestión del proyecto
│   ├── roadmap.md            # Hoja de ruta con fechas
│   └── decisiones.md         # Bitácora de decisiones
│
├── 📁 01_datos/              # Datos del proyecto
│   ├── raw/                  # Datos originales (Excel, CSV)
│   ├── clean/                # Datos procesados
│   └── diccionario_datos.md  # Definición de campos
│
├── 📁 02_analisis/           # Análisis estadístico
│   ├── notebooks/            # Jupyter notebooks
│   ├── scripts/              # Scripts Python
│   └── resultados/           # Gráficos e informes
│
├── 📁 03_centros_propuestos/ # Propuestas por facultad
│   ├── FCA/                  # Centro de Investigación FCA
│   ├── FCQS/                 # Centro de Investigación FCQS
│   └── plantilla_centro.md   # Plantilla base
│
├── 📁 04_reglamentos/        # Marco normativo
│   ├── borradores/           # Versiones de trabajo
│   └── plantillas/           # Esquemas y formatos
│
├── 📁 05_prompts_y_plantillas/
│   └── prompts_antigravity.md # Prompt maestro para análisis IA
│
├── .gitignore
└── README.md                  # Este archivo
```

---

## 🚀 Cómo Contribuir

1. **Lea el roadmap** en `00_admin/roadmap.md` para conocer prioridades actuales.
2. **Datos crudos** → `01_datos/raw/` (nunca modificar originales).
3. **Datos limpios** → `01_datos/clean/` (versiones procesadas).
4. **Análisis** → Documente sus notebooks en `02_analisis/`.
5. **Tono institucional** en toda la documentación.

---

## 👥 Equipo Responsable

| Rol | Área |
|-----|------|
| Dirección de Investigación | Coordinación general del proyecto |
| Facultades (FCA, FCQS) | Provisión de datos y validación |

---

## 📞 Contacto

Para consultas sobre este proyecto, contactar a la **Dirección de Investigación**.

---

*Última actualización: Febrero 2026*
