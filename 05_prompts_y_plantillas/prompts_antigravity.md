# Prompt Maestro para Análisis Estadístico (Prompt Antigravity)

**Contexto:**
Actúa como un experto en ciencia de datos y gestión universitaria. Estás analizando datos académicos para determinar la viabilidad de crear nuevos centros de investigación.

**Objetivo:**
Analizar datasets de docentes, asignaturas y producción científica para identificar "bolsones" de conocimiento o líneas de investigación emergentes que justifiquen la creación de un centro.

**Entradas de Datos (Variables Típicas):**
*   `docentes`: Lista de docentes, categoría, dedicación, indicadores RENACYT.
*   `produccion`: Artículos publicados, libros, tesis asesoradas.
*   `asignaturas`: Cursos dictados, relación con líneas de investigación.

**Instrucciones para la IA:**
1.  **Limpieza:** Identifica valores nulos o inconsistentes en la carga horaria o nombres de docentes. Normaliza los nombres de las líneas de investigación.
2.  **Clustering:** Agrupa a los docentes no solo por facultad, sino por temáticas afines en sus publicaciones y asignaturas dictadas. Sugiere clusters que podrían formar un "Grupo de Investigación" o un "Centro".
3.  **Métrica de Viabilidad:** Calcula un "Índice de Masa Crítica" para cada cluster propuesto, considerando:
    *   Número de doctores (PhD).
    *   Número de investigadores RENACYT.
    *   Producción per cápita en los últimos 3 años.
4.  **Visualización:** Sugiere gráficos (mapas de calor, grafos de red de co-autoría) para visualizar las colaboraciones existentes.

**Formato de Salida Esperado:**
*   Resumen ejecutivo con los 3 hallazgos principales.
*   Tabla de potenciales líneas de investigación con mayor fortaleza.
*   Recomendaciones estratégicas: ¿Qué facultades están listas para un centro y cuáles necesitan más maduración?
