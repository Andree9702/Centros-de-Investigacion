
import pandas as pd
import os

base_path = r"c:\Users\andre\Mi unidad\DIRECCIÓN DE INVESTIGACIÓN\Centros de Investigación\01_datos\raw"
output_path = r"c:\Users\andre\Mi unidad\DIRECCIÓN DE INVESTIGACIÓN\Centros de Investigación\02_analisis\resultados"

filename = "2026-02-06_rpt_produccion_utmach_docentes (2).xlsx"
filepath = os.path.join(base_path, filename)

log_file = open(os.path.join(output_path, "produccion_analysis_report.txt"), "w", encoding="utf-8")

def log(msg):
    print(msg)
    log_file.write(str(msg) + "\n")

log("="*70)
log("ANÁLISIS EXHAUSTIVO: PRODUCCIÓN CIENTÍFICA UTMACH")
log("Archivo: " + filename)
log("="*70)

# Leer con header en fila 2 (donde están los nombres reales de columnas)
df = pd.read_excel(filepath, header=2)

# Mostrar todas las columnas
log("\n--- COLUMNAS ENCONTRADAS ---")
for i, col in enumerate(df.columns):
    log(f"  {i+1}. '{col}'")

# Limpiar: eliminar filas donde Nro es NaN o contiene texto de pie de página
df = df.dropna(subset=[df.columns[0]])
df = df[~df[df.columns[0]].astype(str).str.contains("Generado por", na=False)]

log(f"\n--- DIMENSIONES DESPUÉS DE LIMPIEZA ---")
log(f"Total de registros (artículos): {len(df)}")

# Renombrar columnas para facilitar análisis
column_names = ['Nro', 'TITULO', 'CODIGO', 'TIPO_PRODUCCION', 'FECHA_PUBLICACION', 
                'ESTADO', 'ABSTRACT', 'EDITORIAL', 'ENLACE', 'ESTADO_REVISION',
                'CAMPO_DETALLADO', 'LINEA_INVESTIGACION', 'CUARTIL', 'PONDERACION', 
                'AUTORES_UTMACH', 'COL15', 'AUTORES']

if len(df.columns) >= len(column_names):
    df.columns = column_names[:len(df.columns)]
else:
    df.columns = column_names[:len(df.columns)]

log("\n--- COLUMNAS RENOMBRADAS ---")
for col in df.columns:
    log(f"  - {col}")

# Análisis de CUARTIL
log("\n" + "="*70)
log("ANÁLISIS DE CUARTILES")
log("="*70)

if 'CUARTIL' in df.columns:
    cuartil_dist = df['CUARTIL'].value_counts(dropna=False)
    log("\nDistribución de Cuartiles:")
    log(cuartil_dist.to_string())
    
    # Contar por categoría
    total = len(df)
    q1 = df['CUARTIL'].str.contains('Q1', case=False, na=False).sum()
    q2 = df['CUARTIL'].str.contains('Q2', case=False, na=False).sum()
    q3 = df['CUARTIL'].str.contains('Q3', case=False, na=False).sum()
    q4 = df['CUARTIL'].str.contains('Q4', case=False, na=False).sum()
    no_aplica = df['CUARTIL'].str.contains('NO APLICA|N/A|NaN', case=False, na=True).sum()
    
    log(f"\n--- RESUMEN CUARTILES ---")
    log(f"  Q1 (Alto Impacto): {q1} ({100*q1/total:.1f}%)")
    log(f"  Q2: {q2} ({100*q2/total:.1f}%)")
    log(f"  Q3: {q3} ({100*q3/total:.1f}%)")
    log(f"  Q4: {q4} ({100*q4/total:.1f}%)")
    log(f"  Sin Cuartil/No Aplica: {no_aplica} ({100*no_aplica/total:.1f}%)")

# Análisis de TIPO DE PRODUCCIÓN
log("\n" + "="*70)
log("ANÁLISIS DE TIPO DE PRODUCCIÓN")
log("="*70)

if 'TIPO_PRODUCCION' in df.columns:
    tipo_dist = df['TIPO_PRODUCCION'].value_counts()
    log("\nDistribución por Tipo:")
    log(tipo_dist.to_string())

# Análisis de LÍNEA DE INVESTIGACIÓN
log("\n" + "="*70)
log("ANÁLISIS DE LÍNEAS DE INVESTIGACIÓN")
log("="*70)

if 'LINEA_INVESTIGACION' in df.columns:
    linea_dist = df['LINEA_INVESTIGACION'].value_counts().head(20)
    log("\nTop 20 Líneas de Investigación:")
    log(linea_dist.to_string())

# Análisis de PONDERACIÓN
log("\n" + "="*70)
log("ANÁLISIS DE PONDERACIÓN")
log("="*70)

if 'PONDERACION' in df.columns:
    df['PONDERACION'] = pd.to_numeric(df['PONDERACION'], errors='coerce')
    log(f"\nEstadísticas de Ponderación:")
    log(f"  Suma Total: {df['PONDERACION'].sum():.2f}")
    log(f"  Promedio: {df['PONDERACION'].mean():.4f}")
    log(f"  Mediana: {df['PONDERACION'].median():.4f}")
    log(f"  Máximo: {df['PONDERACION'].max():.2f}")
    log(f"  Mínimo: {df['PONDERACION'].min():.2f}")
    
    # Ponderación por cuartil
    log("\n--- Ponderación Promedio por Cuartil ---")
    pond_cuartil = df.groupby('CUARTIL')['PONDERACION'].agg(['mean', 'sum', 'count'])
    log(pond_cuartil.to_string())

# Muestra de TÍTULOS
log("\n" + "="*70)
log("MUESTRA DE TÍTULOS DE ARTÍCULOS")
log("="*70)

if 'TITULO' in df.columns:
    log("\nPrimeros 10 títulos:")
    for i, titulo in enumerate(df['TITULO'].head(10)):
        log(f"  {i+1}. {titulo[:100]}...")

# Exportar datos limpios para clustering temático
df_export = df[['TITULO', 'TIPO_PRODUCCION', 'LINEA_INVESTIGACION', 'CUARTIL', 'PONDERACION', 'AUTORES_UTMACH']].copy()
df_export.to_csv(os.path.join(output_path, "articulos_para_clustering.csv"), index=False, encoding='utf-8-sig')

log("\n" + "="*70)
log("ARCHIVO EXPORTADO")
log(f"  - {output_path}\\articulos_para_clustering.csv")
log("="*70)

log_file.close()
print("\n=== ANÁLISIS COMPLETADO ===")
