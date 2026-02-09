
import pandas as pd
import os

base_path = r"c:\Users\andre\Mi unidad\DIRECCIÓN DE INVESTIGACIÓN\Centros de Investigación\01_datos\raw"
files = [
    "IPPC ultimo año 2025.xlsx",
    "IPPC ultimos 2 años.xlsx",
    "IPPC ultimos 3 años.xlsx"
]

log_file = open("ippc_analysis_results.txt", "w", encoding="utf-8")

def log(msg):
    print(msg)
    log_file.write(str(msg) + "\n")

def analyze_ippc_file(filename):
    filepath = os.path.join(base_path, filename)
    log(f"\n{'='*60}")
    log(f"ARCHIVO: {filename}")
    log(f"{'='*60}")
    
    try:
        df = pd.read_excel(filepath)
        
        log(f"\n--- DIMENSIONES ---")
        log(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
        
        log(f"\n--- COLUMNAS ---")
        for i, col in enumerate(df.columns):
            log(f"  {i+1}. {col}")
            
        log(f"\n--- TIPOS DE DATOS ---")
        for col in df.columns:
            log(f"  {col}: {df[col].dtype}")
        
        log(f"\n--- PRIMERAS 5 FILAS ---")
        log(df.head(5).to_string())
        
        log(f"\n--- ÚLTIMAS 3 FILAS ---")
        log(df.tail(3).to_string())
        
        log(f"\n--- VALORES NULOS POR COLUMNA ---")
        nulls = df.isnull().sum()
        for col in df.columns:
            if nulls[col] > 0:
                log(f"  {col}: {nulls[col]} nulos ({100*nulls[col]/len(df):.1f}%)")
        if nulls.sum() == 0:
            log("  (Sin valores nulos)")
        
        # Buscar columnas clave
        cols_lower = [str(c).lower() for c in df.columns]
        
        # Análisis de Facultad
        for key in ['facultad', 'unidad']:
            matches = [c for c, l in zip(df.columns, cols_lower) if key in l]
            if matches:
                log(f"\n--- DISTRIBUCIÓN DE '{matches[0]}' ---")
                log(df[matches[0]].value_counts().to_string())
        
        # Análisis de IPPC
        for key in ['ippc', 'ponderación', 'ponderacion', 'índice', 'indice']:
            matches = [c for c, l in zip(df.columns, cols_lower) if key in l]
            if matches:
                col = matches[0]
                log(f"\n--- ESTADÍSTICAS DE '{col}' ---")
                numeric_col = pd.to_numeric(df[col], errors='coerce')
                log(f"  Min: {numeric_col.min()}")
                log(f"  Max: {numeric_col.max()}")
                log(f"  Media: {numeric_col.mean():.4f}")
                log(f"  Mediana: {numeric_col.median():.4f}")
                log(f"  Desv. Est.: {numeric_col.std():.4f}")
                break
        
        # Análisis de docentes
        for key in ['docente', 'nombre', 'autor']:
            matches = [c for c, l in zip(df.columns, cols_lower) if key in l]
            if matches:
                log(f"\n--- DOCENTES ÚNICOS ('{matches[0]}') ---")
                log(f"  Total: {df[matches[0]].nunique()}")
                break
                
    except Exception as e:
        log(f"ERROR: {e}")

for f in files:
    analyze_ippc_file(f)

log_file.close()
print("\n\n=== ANÁLISIS COMPLETADO ===")
print("Resultados guardados en: ippc_analysis_results.txt")
