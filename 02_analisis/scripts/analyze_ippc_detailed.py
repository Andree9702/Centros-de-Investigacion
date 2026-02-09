
import pandas as pd
import os

base_path = r"c:\Users\andre\Mi unidad\DIRECCIÓN DE INVESTIGACIÓN\Centros de Investigación\01_datos\raw"
output_path = r"c:\Users\andre\Mi unidad\DIRECCIÓN DE INVESTIGACIÓN\Centros de Investigación\02_analisis\resultados"

files = {
    "1_año": "IPPC ultimo año 2025.xlsx",
    "2_años": "IPPC ultimos 2 años.xlsx",
    "3_años": "IPPC ultimos 3 años.xlsx"
}

log_file = open(os.path.join(output_path, "ippc_detailed_report.txt"), "w", encoding="utf-8")

def log(msg):
    print(msg)
    log_file.write(str(msg) + "\n")

log("="*70)
log("INFORME DETALLADO DE ANÁLISIS IPPC - UTMACH")
log("Fecha de generación: 2026-02-09")
log("="*70)

dataframes = {}

for key, filename in files.items():
    filepath = os.path.join(base_path, filename)
    # Leer con header en fila 2 (índice 2)
    df = pd.read_excel(filepath, header=2)
    # Eliminar filas con todos NaN (encabezados y pie de página)
    df = df.dropna(how='all')
    # Eliminar última fila si contiene "Generado por"
    if df.iloc[-1, 0] is not None and "Generado por" in str(df.iloc[-1, 0]):
        df = df.iloc[:-1]
    # Renombrar columnas
    df.columns = ['Nro', 'FACULTAD', 'DOCUMENTO', 'NOMBRES', 'CARGO', 'DEDICACIÓN', 
                  'IPPC_PROD_CIENT', 'IPPC_PROD_ART', 'IPPC_PROP_INT', 'VALOR_IPPC']
    # Convertir IPPC a numérico
    for col in ['IPPC_PROD_CIENT', 'IPPC_PROD_ART', 'IPPC_PROP_INT', 'VALOR_IPPC']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    dataframes[key] = df

# ANÁLISIS 1: Comparación general entre períodos
log("\n" + "="*70)
log("1. RESUMEN COMPARATIVO POR PERÍODO")
log("="*70)

for key, df in dataframes.items():
    log(f"\n--- {key.upper()} ---")
    log(f"  Total docentes: {len(df)}")
    log(f"  Docentes con IPPC > 0: {(df['VALOR_IPPC'] > 0).sum()}")
    log(f"  Docentes con IPPC = 0: {(df['VALOR_IPPC'] == 0).sum()}")
    log(f"  IPPC Promedio (global): {df['VALOR_IPPC'].mean():.4f}")
    log(f"  IPPC Promedio (solo > 0): {df[df['VALOR_IPPC'] > 0]['VALOR_IPPC'].mean():.4f}")
    log(f"  IPPC Máximo: {df['VALOR_IPPC'].max():.2f}")
    log(f"  IPPC Mediana: {df['VALOR_IPPC'].median():.4f}")

# ANÁLISIS 2: Distribución por Facultad (usando 3 años como principal)
log("\n" + "="*70)
log("2. DISTRIBUCIÓN POR FACULTAD (IPPC 3 AÑOS)")
log("="*70)

df_3años = dataframes['3_años']

facultad_stats = df_3años.groupby('FACULTAD').agg(
    Total_Docentes=('NOMBRES', 'count'),
    Docentes_Activos=('VALOR_IPPC', lambda x: (x > 0).sum()),
    IPPC_Promedio=('VALOR_IPPC', 'mean'),
    IPPC_Suma=('VALOR_IPPC', 'sum'),
    IPPC_Max=('VALOR_IPPC', 'max'),
    IPPC_Mediana=('VALOR_IPPC', 'median')
).round(4)

facultad_stats['Pct_Activos'] = (facultad_stats['Docentes_Activos'] / facultad_stats['Total_Docentes'] * 100).round(1)
facultad_stats = facultad_stats.sort_values('IPPC_Suma', ascending=False)

log("\n" + facultad_stats.to_string())

# ANÁLISIS 3: Top 10 docentes por IPPC (3 años)
log("\n" + "="*70)
log("3. TOP 10 DOCENTES POR IPPC (3 AÑOS)")
log("="*70)

top10 = df_3años.nlargest(10, 'VALOR_IPPC')[['NOMBRES', 'FACULTAD', 'VALOR_IPPC', 'CARGO']]
log("\n" + top10.to_string(index=False))

# ANÁLISIS 4: Clustering por percentiles (como en decisiones.md)
log("\n" + "="*70)
log("4. CLUSTERING POR PERCENTILES (3 AÑOS)")
log("="*70)

# Solo docentes con IPPC > 0 para el clustering
df_activos = df_3años[df_3años['VALOR_IPPC'] > 0].copy()
p90 = df_activos['VALOR_IPPC'].quantile(0.90)
p50 = df_activos['VALOR_IPPC'].quantile(0.50)
p25 = df_activos['VALOR_IPPC'].quantile(0.25)

log(f"\nPercentiles (solo docentes con IPPC > 0, n={len(df_activos)}):")
log(f"  P90 (Élite): >= {p90:.4f}")
log(f"  P50 (Consolidados): {p50:.4f} - {p90:.4f}")
log(f"  P25 (En Desarrollo): {p25:.4f} - {p50:.4f}")
log(f"  <P25 (Sin Actividad Significativa): < {p25:.4f}")

def clasificar(ippc):
    if ippc >= p90:
        return 'A - Élite'
    elif ippc >= p50:
        return 'B - Consolidados'
    elif ippc >= p25:
        return 'C - En Desarrollo'
    else:
        return 'D - Sin Actividad Significativa'

df_activos['Cluster'] = df_activos['VALOR_IPPC'].apply(clasificar)

cluster_by_facultad = pd.crosstab(df_activos['FACULTAD'], df_activos['Cluster'])
log("\n--- Distribución de Clusters por Facultad ---")
log(cluster_by_facultad.to_string())

# ANÁLISIS 5: Masa crítica por facultad
log("\n" + "="*70)
log("5. MASA CRÍTICA POR FACULTAD (Clusters A + B)")
log("="*70)

masa_critica = df_activos[df_activos['Cluster'].isin(['A - Élite', 'B - Consolidados'])]
masa_por_facultad = masa_critica.groupby('FACULTAD').size().sort_values(ascending=False)
log("\n" + masa_por_facultad.to_string())

# Guardar datos limpios para uso posterior
df_3años.to_csv(os.path.join(output_path, "ippc_3años_limpio.csv"), index=False, encoding='utf-8-sig')
df_activos.to_csv(os.path.join(output_path, "ippc_3años_activos_clustered.csv"), index=False, encoding='utf-8-sig')

log("\n" + "="*70)
log("ARCHIVOS GENERADOS:")
log(f"  - {output_path}\\ippc_detailed_report.txt")
log(f"  - {output_path}\\ippc_3años_limpio.csv")
log(f"  - {output_path}\\ippc_3años_activos_clustered.csv")
log("="*70)

log_file.close()
print("\n=== ANÁLISIS COMPLETADO ===")
