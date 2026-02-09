# 🏛️ Proyecto: Creación y Reglamentación de Centros de Investigación - UTMACH

![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![Fase](https://img.shields.io/badge/Fase-A%20Diagnóstico-blue)
![Institución](https://img.shields.io/badge/Universidad-UTMACH-darkgreen)
![País](https://img.shields.io/badge/País-Ecuador-red)

---

## 📋 Objetivo

Centralizar y gestionar la información, datos, análisis y documentación necesaria para la **creación, formalización y reglamentación** de los nuevos Centros de Investigación de la **Universidad Técnica de Machala (UTMACH)**.

El proyecto busca analizar el IPPC (Índice Ponderado de Producción Científica) de **todos los docentes** para tomar decisiones basadas en datos sobre la creación de centros de investigación piloto.

### Centros Piloto Propuestos

| Centro | Facultad | Justificación |
|--------|----------|---------------|
| 🌱 **Centro FCA** | Facultad de Ciencias Agropecuarias | Mayor producción científica y actividad investigadora |
| 🔬 **Centro FCQS** | Facultad de Ciencias Químicas y de la Salud | Alta concentración de investigadores acreditados |

---

## 🎓 Facultades de la UTMACH

| Sigla | Nombre Completo |
|-------|-----------------|
| **FCA** | Facultad de Ciencias Agropecuarias |
| **FCQS** | Facultad de Ciencias Químicas y de la Salud |
| **FCE** | Facultad de Ciencias Empresariales |
| **FIC** | Facultad de Ingeniería Civil |
| **FCS** | Facultad de Ciencias Sociales |

---

## 🎯 Alcance del Proyecto

| Fase | Descripción | Estado |
|------|-------------|--------|
| **A. Datos** | Recopilación del Excel IPPC de todos los docentes, limpieza y estructuración | 🔄 En curso |
| **B. Análisis** | Clustering por IPPC, ranking de facultades, identificación de masa crítica | ⏳ Pendiente |
| **C. Propuestas** | Elaboración de expedientes técnicos para centros FCA y FCQS | ⏳ Pendiente |
| **D. Normativa** | Redacción del Reglamento General de Centros de Investigación | ⏳ Pendiente |

---

## 📦 Entregables

1. ✅ Base de datos consolidada y limpia de docentes (IPPC por facultad)
2. 📊 Informes de análisis con clustering (Élite, Consolidados, En Desarrollo)
3. 📄 Expedientes de creación para los Centros FCA y FCQS
4. 📜 Reglamento General de Centros de Investigación

---

## 📁 Estructura del Repositorio

```
📂 Centros de Investigación/
├── 📁 00_admin/              # Gestión del proyecto
│   ├── roadmap.md            # Hoja de ruta con fechas
│   └── decisiones.md         # Bitácora de decisiones
│
├── 📁 01_datos/              # Datos del proyecto
│   ├── raw/                  # Excel original del DIDI
│   ├── clean/                # Datos procesados
│   └── diccionario_datos.md  # Definición de campos IPPC
│
├── 📁 02_analisis/           # Análisis estadístico
│   ├── notebooks/            # Jupyter notebooks
│   ├── scripts/              # Scripts Python
│   └── resultados/           # Gráficos e informes
│
├── 📁 03_centros_propuestos/ # Propuestas por facultad
│   ├── FCA/                  # Centro de Ciencias Agropecuarias
│   ├── FCQS/                 # Centro de Ciencias Químicas y de la Salud
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

## 👥 Equipo del Proyecto

| Rol | Nombre | Contacto |
|-----|--------|----------|
| **Director DIDI** | PhD. Ivan Ramirez | Dirección de Investigación, Desarrollo e Innovación |
| **Colaborador** | MSc. Luiggi Solano | DIDI |
| **Coordinación** | Dirección de Investigación | UTMACH |

---

## 🚀 Cómo Contribuir

1. **Lea el roadmap** en `00_admin/roadmap.md` para conocer prioridades actuales.
2. **Datos crudos** → `01_datos/raw/` (Excel del DIDI).
3. **Datos limpios** → `01_datos/clean/` (versiones procesadas).
4. **Análisis** → Documente sus notebooks en `02_analisis/`.
5. **Use el prompt maestro** en `05_prompts_y_plantillas/prompts_antigravity.md` para análisis con IA.

---

## 📞 Contacto

Para consultas sobre este proyecto, contactar al **Departamento de Investigación, Desarrollo e Innovación (DIDI)** de la UTMACH.

---

*Universidad Técnica de Machala - Febrero 2026*
