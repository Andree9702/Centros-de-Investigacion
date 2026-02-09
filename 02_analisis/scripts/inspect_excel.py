
import pandas as pd
import os

base_path = r"c:\Users\andre\Mi unidad\DIRECCIÓN DE INVESTIGACIÓN\Centros de Investigación\01_datos\raw"
files = [
    "2026-02-06_rpt_produccion_utmach_docentes (2).xlsx",
    "GRUPOS DE INVESTIGACIÓN UTMACH.xlsx"
]


# Redirect print to a file
import sys

# Open file with utf-8 encoding
log_file = open("analysis_results.txt", "w", encoding="utf-8")

def log(msg):
    print(msg)
    log_file.write(str(msg) + "\n")

def analyze_file(filename):
    filepath = os.path.join(base_path, filename)
    log(f"\n{'='*50}")
    log(f"ANALYZING: {filename}")
    log(f"{'='*50}")
    
    try:
        # Read the first few rows to infer header, sometimes headers are not on row 0
        # But let's verify row 0 first.
        df = pd.read_excel(filepath)
        
        log("\n--- SHAPE ---")
        log(df.shape)
        
        log("\n--- COLUMNS ---")
        for col in df.columns:
            log(f"- {col}")
            
        log("\n--- INFO ---")
        # capturing info() is tricky as it prints to sys.stdout by default
        # we can skip info() or redirect sys.stdout temporarily, but shape and columns are most critical
        # log(df.info()) 
        
        log("\n--- HEAD (First 3 rows) ---")
        log(df.head(3).to_string())
        
        # specific checks for potential key columns if they exist (case insensitive)
        cols_lower = [str(c).lower() for c in df.columns]
        
        for key in ['facultad', 'unidad', 'docente', 'ippc', 'produccion', 'linea', 'grupo']:
            matches = [c for c, l in zip(df.columns, cols_lower) if key in l]
            if matches:
                log(f"\n--- SAMPLE VALUES FOR '{matches[0]}' ---")
                log(df[matches[0]].unique()[:10])
                
    except Exception as e:
        log(f"ERROR reading {filename}: {e}")

for f in files:
    analyze_file(f)

log_file.close()
