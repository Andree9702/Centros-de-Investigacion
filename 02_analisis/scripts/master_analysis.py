"""
==========================================================================
SCRIPT MAESTRO DEFINITIVO v2: Centros de Investigación UTMACH
==========================================================================
Directriz del Director (Reg. 008):
  "No es lo mismo tener 100 artículos Latindex sobre banano que
   50 Q1 sobre bioquímica."
  → La fortaleza temática PONDERADA revela capacidades reales.

Protocolo corregido:
  1. Filtrar producción (solo Artículos de revista)
  2. Clasificar por CAMPO_DETALLADO como filtro duro PRIMERO
     (si el campo pertenece a lista SOCIAL siempre va a Vía B)
  3. Para los no-sociales: revisar léxico de laboratorio para
     confirmar si son Experimentales o van a Vía B también
  4. Clustering semántico TF-IDF + K-Means FORZADO a K fijo para
     producir exactamente N centros/observatorios bien definidos
  5. Ponderación por impacto (Q1=1.0, Q2=0.9, Q3=0.8, Q4=0.7)
  6. Generar reportes y CSVs definitivos
==========================================================================
"""
import pandas as pd
import numpy as np
import os
import re
import warnings
warnings.filterwarnings('ignore')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import nltk
from nltk.corpus import stopwords
import string

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

# ===================== RUTAS =====================
BASE = r"c:\Users\andre\Mi unidad\DIRECCIÓN DE INVESTIGACIÓN\Centros de Investigación"
RAW  = os.path.join(BASE, "01_datos", "raw")
OUT  = os.path.join(BASE, "02_analisis", "resultados")
os.makedirs(OUT, exist_ok=True)

PRODUCCION_FILE = os.path.join(RAW, "2026-02-06_rpt_produccion_utmach_docentes (2).xlsx")

# ===================== LISTAS DURAS =====================
# Campos que SIEMPRE son Ciencias Sociales/Humanísticas (filtro duro)
CAMPOS_SOCIAL = [
    'economía', 'derecho', 'administración', 'mercadotecnia', 'contabilidad',
    'auditoría', 'periodismo', 'comunicación', 'comercio', 'turismo',
    'formación para docentes', 'estudios sociales', 'educación', 'pedagogía',
    'formación profesional', 'ciencias sociales', 'sociología', 'trabajo social',
    'gestión empresarial', 'desarrollo económico', 'finanzas', 'marketing',
    'política', 'gobernabilidad', 'jurídic', 'justicia', 'constitucional', 'penal',
    'psicología social', 'historia', 'filosofía', 'literatura', 'lingüística',
]

# Campos que SIEMPRE son Experimentales (filtro duro positivo)
CAMPOS_EXPERIMENTAL = [
    'química', 'bioquímica', 'farmacología', 'microbiología', 'biotecnología',
    'biología', 'genética', 'biofísica', 'inmunología', 'medicina', 'enfermería',
    'agropecuaria', 'agronomía', 'veterinaria', 'zootecnia', 'acuacultura',
    'física', 'ingeniería química', 'ingeniería ambiental', 'materiales',
    'geología', 'ecología', 'ciencias ambientales', 'medio ambiente',
    'odontología', 'laboratorio', 'clínic', 'salud pública', 'epidemiología',
    'nutrición', 'alimentación', 'dietética', 'tecnología de alimentos',
]

# Léxico de laboratorio REAL (palabras que solo aparecen en experimental puro)
LEXICO_LAB = [
    'in vitro', 'in vivo', 'reactivo', 'espectroscopía', 'espectrofotometría',
    'cromatografía', 'microscopía', 'cepa', 'cultivo microbiano', 'inoculación',
    'biopsia', 'suero sanguíneo', 'hemograma', 'bioterio', 'parcela experimental',
    'ensayo clínico', 'grupo control', 'doble ciego', 'placebo', 'muestra sanguínea',
    'germinación', 'purificación', 'síntesis química', 'extracción adn',
    'secuenciación', 'fermentación', 'biomasa', 'anova', 'diseño experimental',
]

# Léxico de revisión bibliográfica (excluir de clusters)
LEXICO_REVISION = [
    'revisión sistemática', 'systematic review', 'meta-análisis', 'meta-analysis',
    'estado del arte', 'revisión bibliográfica', 'literature review',
    'análisis documental', 'scoping review', 'bibliometría', 'bibliometric',
    'revisión narrativa', 'mapeo sistemático',
]

# ===================== CENTROS/OBSERVATORIOS FIJOS =====================
# Via A: 4 centros con keywords específicas de su campo
VIA_A_CENTROS = [
    {
        'nombre': 'Centro de Investigación en Ciencias Agropecuarias y Bioeconomía',
        'keywords': [
            'agropecuario', 'agrícola', 'agroalimentar', 'banano', 'cacao',
            'ganader', 'bovino', 'porcino', 'camarón', 'pesca', 'acuacult',
            'riego', 'fertiliz', 'plaguicida', 'fitosanit', 'producción vegetal',
            'producción animal', 'bioeconom', 'cosecha', 'siembra', 'semilla',
            'abono', 'agroquímic', 'agroindustria', 'producción de banano',
        ],
    },
    {
        'nombre': 'Centro de Investigación en Salud Integral y Biociencias Clínicas',
        'keywords': [
            'salud', 'enferm', 'medici', 'clínic', 'paciente', 'farmac', 'bioquím',
            'microbiolog', 'inmunolog', 'epidemiolog', 'odontolog', 'nutric',
            'alimentac', 'dietétic', 'biotecno', 'genétic', 'hospital',
            'terapéutic', 'diagnóstic', 'patolog', 'cirugía', 'pediatr',
            'enfermería', 'prevención', 'atención primaria',
        ],
    },
    {
        'nombre': 'Centro de Investigación en Ciencias Ambientales y Gestión del Territorio',
        'keywords': [
            'ambient', 'ecosistem', 'contaminac', 'biodiversid', 'manglar',
            'deforestac', 'cambio climátic', 'recurso natural', 'gestión territorial',
            'ordenamiento', 'hidráulic', 'planificación territorial', 'riesgo ambiental',
            'reforestac', 'conservac', 'humedal', 'cuenca hidrográfica',
            'calidad del agua', 'microplástico', 'cobertura vegetal',
        ],
    },
    {
        'nombre': 'Centro de Investigación en Ingeniería, Tecnología y Ciencias Exactas',
        'keywords': [
            'algoritmo', 'machine learning', 'inteligencia artificial',
            'software', 'sistema informátic', 'red neuronal', 'modelado',
            'simulación', 'optimizac', 'informátic', 'computac', 'programac',
            'ingeniería civil', 'ingeniería eléctric', 'ingeniería industr',
            'ingeniería mecánic', 'robótic', 'electrónic', 'telecomunicac',
            'sistema de información geográfica', 'procesos químicos', 'proceso industrial',
            'energía renovable', 'destilación', 'reacción química', 'polímero',
            'materiales', 'construcción', 'geotecnia', 'escrum', 'framework',
        ],
    },
]

# Via B: 4 observatorios con keywords específicas
VIA_B_OBSERVATORIOS = [
    {
        'nombre': 'Observatorio de Economía, Empresa e Innovación Productiva',
        'keywords': [
            'gestión empresarial', 'negoci', 'financ', 'contab',
            'emprendimient', 'inversión', 'exportac', 'importac',
            'auditoría', 'tributar', 'pyme', 'cadena de valor', 'logístic',
            'competitividad', 'blockchain', 'fintech', 'turismo', 'hostelería',
            'marketing', 'mercadotecnia', 'sector productiv', 'economía',
        ],
    },
    {
        'nombre': 'Observatorio de Educación, Tecnología y Desarrollo Humano',
        'keywords': [
            'educac', 'enseñanza', 'aprendizaje', 'docente', 'pedagog',
            'currícul', 'didáctic', 'escuel', 'universitari',
            'inclusión educativ', 'gamificac', 'e-learning',
            'tecnología educativ', 'habilidades blandas',
            'rendimiento académic', 'bienestar estudiantil',
            'ingeniería de software', 'plataform', 'aplicación web',
        ],
    },
    {
        'nombre': 'Observatorio de Derecho, Justicia Social y Políticas Públicas',
        'keywords': ['derecho', 'jurídic', 'penal', 'constitucional', 'justicia', 'legal',
                     'normativ', 'regulac', 'legislac', 'política pública', 'gobernanza',
                     'institucional', 'administración pública', 'corrupción', 'derechos humanos',
                     'género', 'equidad', 'inclusión social', 'vulnerabilidad social',
                     'participación ciudadana', 'democracia'],
    },
    {
        'nombre': 'Observatorio de Sociedad, Cultura y Comunicación',
        'keywords': ['comunicac', 'periodism', 'mediátic', 'redes sociales', 'cultura',
                     'identidad cultural', 'sociedad', 'psicología social', 'bienestar social',
                     'salud mental', 'ansiedad', 'depresión', 'violencia', 'familia',
                     'comunidad', 'desarrollo social', 'trabajo social', 'antropolog',
                     'sociolog', 'historiografía', 'lingüístic', 'género y sociedad'],
    },
]

# ===================== FUNCIONES =====================

def load_and_clean():
    print("=" * 70)
    print("FASE 1: CARGA Y FILTRADO DE PRODUCCIÓN")
    print("=" * 70)

    df = pd.read_excel(PRODUCCION_FILE, header=2)
    df = df.dropna(subset=[df.columns[0]])
    df = df[~df[df.columns[0]].astype(str).str.contains("Generado por", na=False)]

    cols = ['Nro', 'TITULO', 'CODIGO', 'TIPO_PRODUCCION', 'FECHA_PUBLICACION',
            'ESTADO', 'ABSTRACT', 'EDITORIAL', 'ENLACE', 'ESTADO_REVISION',
            'CAMPO_DETALLADO', 'LINEA_INVESTIGACION', 'CUARTIL', 'PONDERACION',
            'AUTORES_UTMACH', 'COL15', 'AUTORES']
    df.columns = cols[:len(df.columns)]

    total_original = len(df)
    df = df.dropna(subset=['TIPO_PRODUCCION'])
    df = df[df['TIPO_PRODUCCION'].str.contains('Artículo', case=False, na=False)]
    df = df[~df['TIPO_PRODUCCION'].str.contains('Libro|Capítulo', case=False, na=False)]

    df['PONDERACION'] = pd.to_numeric(df['PONDERACION'], errors='coerce').fillna(0)

    # ── Filtro temporal: solo artículos desde 01/01/2022 ──
    df['FECHA_PUBLICACION'] = pd.to_datetime(df['FECHA_PUBLICACION'], errors='coerce')
    antes_filtro = len(df)
    df = df[df['FECHA_PUBLICACION'] >= '2022-01-01']
    print(f"  Filtro temporal (>= 2022): {antes_filtro - len(df)} artículos anteriores excluidos")

    print(f"  Total registros originales: {total_original}")
    print(f"  Eliminados (Libros/Capítulos/vacíos): {total_original - antes_filtro}")
    print(f"  ✅ Artículos válidos (2022–2026): {len(df)}")

    return df



def classify_v2(df):
    """
    Clasificación en Dos Vías usando CAMPO_DETALLADO como filtro duro
    y léxico de laboratorio como confirmación.
    """
    print("\n" + "=" * 70)
    print("FASE 2: CLASIFICACIÓN EN DOS VÍAS (CAMPO_DETALLADO + LÉXICO)")
    print("=" * 70)

    def text_lower(row):
        abstract = str(row.get('ABSTRACT', '') or '').lower()
        titulo   = str(row.get('TITULO', '') or '').lower()
        campo    = str(row.get('CAMPO_DETALLADO', '') or '').lower()
        linea    = str(row.get('LINEA_INVESTIGACION', '') or '').lower()
        return abstract + ' ' + titulo + ' ' + campo + ' ' + linea

    def clasificar(row):
        txt = text_lower(row)
        campo = str(row.get('CAMPO_DETALLADO', '') or '').lower()

        # ── Paso 0: ¿es revisión bibliográfica? ──
        for kw in LEXICO_REVISION:
            if kw in txt:
                return 'BIBLIOGRÁFICA/REVISIÓN'

        # ── Paso 1: Campo duro → Social ──
        for kw in CAMPOS_SOCIAL:
            if kw in campo:
                return 'CIENCIAS_SOCIALES'

        # ── Paso 2: Campo duro → Experimental ──
        for kw in CAMPOS_EXPERIMENTAL:
            if kw in campo:
                return 'EXPERIMENTAL'

        # ── Paso 3: Léxico laboratorio en texto completo ──
        lab_score = sum(1 for kw in LEXICO_LAB if kw in txt)
        if lab_score >= 1:
            return 'EXPERIMENTAL'

        # ── Paso 4: Por defecto → Social/Humanístico ──
        return 'CIENCIAS_SOCIALES'

    df['TIPO_INVESTIGACION'] = df.apply(clasificar, axis=1)

    counts = df['TIPO_INVESTIGACION'].value_counts()
    for tipo, count in counts.items():
        print(f"  {tipo}: {count} ({count/len(df)*100:.1f}%)")

    return df


def build_context(df):
    stop_es = set(stopwords.words('spanish'))
    stop_en = set(stopwords.words('english'))
    custom  = {'estudio', 'objetivo', 'resultados', 'conclusiones', 'metodologia',
                'presente', 'trabajo', 'artículo', 'investigación', 'paper', 'research',
                'study', 'análisis', 'objetivo', 'método', 'muestra', 'datos'}
    stops   = stop_es | stop_en | custom

    def preprocess(text):
        if pd.isna(text): return ""
        text = str(text).lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = re.sub(r'\d+', '', text)
        return " ".join(w for w in text.split() if w not in stops and len(w) > 2)

    # Abstract (x2 peso) + Línea (x2) + Campo (x2) + Título (x1)
    df['contexto'] = (
        df['ABSTRACT'].fillna('')   + ' ' + df['ABSTRACT'].fillna('') + ' ' +
        df['TITULO'].fillna('')     + ' ' +
        df['LINEA_INVESTIGACION'].fillna('') + ' ' +
        df['LINEA_INVESTIGACION'].fillna('') + ' ' +
        df['CAMPO_DETALLADO'].fillna('')     + ' ' +
        df['CAMPO_DETALLADO'].fillna('')
    )
    df['contexto_limpio'] = df['contexto'].apply(preprocess)
    return df


def assign_fixed_cluster(row, centros_list, default_name):
    """
    Asigna cada artículo al centro/observatorio cuyas keywords
    tienen mayor coincidencia en el texto del artículo.
    Si empata o no hay coincidencia, va al grupo con más masa.
    """
    txt = (str(row.get('ABSTRACT', '') or '') + ' ' +
           str(row.get('TITULO', '') or '') + ' ' +
           str(row.get('LINEA_INVESTIGACION', '') or '') + ' ' +
           str(row.get('CAMPO_DETALLADO', '') or '')).lower()

    best_score = -1
    best_name  = default_name

    for centro in centros_list:
        score = sum(1 for kw in centro['keywords'] if kw in txt)
        if score > best_score:
            best_score = score
            best_name  = centro['nombre']

    return best_name


def cluster_via_a(df_exp):
    print("\n" + "=" * 70)
    print("FASE 3A: ASIGNACIÓN VÍA A – CENTROS EXPERIMENTALES (K fijo=4)")
    print("=" * 70)

    df_exp = df_exp.copy()
    df_exp['centro_propuesto'] = df_exp.apply(
        assign_fixed_cluster,
        axis=1,
        centros_list=VIA_A_CENTROS,
        default_name=VIA_A_CENTROS[2]['nombre']  # Default: Ambiental (grupo más amplio)
    )
    df_exp['via'] = 'A – Ciencias Experimentales'

    for name, grp in df_exp.groupby('centro_propuesto'):
        print(f"  {name}: {len(grp)} artículos")

    return df_exp


def cluster_via_b(df_social):
    print("\n" + "=" * 70)
    print("FASE 3B: ASIGNACIÓN VÍA B – OBSERVATORIOS SOCIALES (K fijo=4)")
    print("=" * 70)

    df_social = df_social.copy()
    df_social['centro_propuesto'] = df_social.apply(
        assign_fixed_cluster,
        axis=1,
        centros_list=VIA_B_OBSERVATORIOS,
        default_name=VIA_B_OBSERVATORIOS[0]['nombre']  # Default: Economía (grupo más grande)
    )
    df_social['via'] = 'B – Ciencias Sociales y Humanísticas'

    for name, grp in df_social.groupby('centro_propuesto'):
        print(f"  {name}: {len(grp)} artículos")

    return df_social


def handle_bibliographic(df_biblio):
    df_biblio = df_biblio.copy()
    df_biblio['cluster_id'] = -1
    df_biblio['centro_propuesto'] = '(Revisiones Bibliográficas – No asignadas a Centro)'
    df_biblio['via'] = 'Revisión Bibliográfica'
    return df_biblio


def generate_impact_report(df_final):
    print("\n" + "=" * 70)
    print("FASE 4: IMPACTO PONDERADO POR CENTRO/OBSERVATORIO")
    print("=" * 70)

    impacto = df_final.groupby(['via', 'centro_propuesto']).agg(
        total_articulos   = ('TITULO', 'count'),
        suma_ponderada    = ('PONDERACION', 'sum'),
        promedio_pond     = ('PONDERACION', 'mean'),
        articulos_Q1 = ('CUARTIL', lambda x: (x == 'Q1').sum()),
        articulos_Q2 = ('CUARTIL', lambda x: (x == 'Q2').sum()),
        articulos_Q3 = ('CUARTIL', lambda x: (x == 'Q3').sum()),
        articulos_Q4 = ('CUARTIL', lambda x: (x == 'Q4').sum()),
    ).reset_index()

    impacto = impacto.sort_values(['via', 'suma_ponderada'], ascending=[True, False])
    print(impacto[['via','centro_propuesto','total_articulos','suma_ponderada','articulos_Q1']].to_string(index=False))
    return impacto


def save_all(df_final, impacto):
    print("\n" + "=" * 70)
    print("FASE 5: GUARDANDO ARCHIVOS DEFINITIVOS")
    print("=" * 70)

    export_cols = ['TITULO', 'ABSTRACT', 'TIPO_PRODUCCION', 'LINEA_INVESTIGACION',
                   'CAMPO_DETALLADO', 'CUARTIL', 'PONDERACION', 'AUTORES_UTMACH',
                   'TIPO_INVESTIGACION', 'via', 'centro_propuesto']
    df_final[export_cols].to_csv(
        os.path.join(OUT, "produccion_clasificada_definitiva.csv"),
        index=False, encoding='utf-8-sig'
    )

    impacto.to_csv(
        os.path.join(OUT, "impacto_por_centro_definitivo.csv"),
        index=False, encoding='utf-8-sig'
    )

    report_path = os.path.join(OUT, "REPORTE_FINAL_CENTROS.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("REPORTE FINAL: CENTROS DE INVESTIGACIÓN UTMACH\n")
        f.write("Metodología: Clasificación por CAMPO_DETALLADO + Léxico LAB\n")
        f.write("Ponderación: Q1=1.0 · Q2=0.9 · Q3=0.8 · Q4=0.7 · Sin Q=0.2\n")
        f.write("Fecha: Marzo 2026\n")
        f.write("=" * 70 + "\n\n")

        counts = df_final['TIPO_INVESTIGACION'].value_counts()
        f.write("CLASIFICACIÓN DE LA PRODUCCIÓN CIENTÍFICA\n")
        f.write("-" * 40 + "\n")
        for tipo, c in counts.items():
            f.write(f"  {tipo}: {c} ({c/len(df_final)*100:.1f}%)\n")
        f.write(f"  TOTAL: {len(df_final)}\n\n")

        for via_label in ['A – Ciencias Experimentales', 'B – Ciencias Sociales y Humanísticas']:
            etiqueta = "VÍA A: CENTROS DE INVESTIGACIÓN CIENTÍFICO-EXPERIMENTALES" \
                if via_label.startswith("A") else \
                "VÍA B: OBSERVATORIOS DE CIENCIAS SOCIALES Y HUMANÍSTICAS"
            f.write("=" * 70 + "\n")
            f.write(etiqueta + "\n")
            f.write("=" * 70 + "\n\n")

            via_data = impacto[impacto['via'] == via_label]
            for _, row in via_data.iterrows():
                f.write(f"--- {row['centro_propuesto']} ---\n")
                f.write(f"  Artículos:           {row['total_articulos']}\n")
                f.write(f"  Impacto Ponderado:   {row['suma_ponderada']:.1f}\n")
                f.write(f"  Promedio Ponderación:{row['promedio_pond']:.3f}\n")
                f.write(f"  Q1:{row['articulos_Q1']}  Q2:{row['articulos_Q2']}  Q3:{row['articulos_Q3']}  Q4:{row['articulos_Q4']}\n")

                sample = df_final[
                    (df_final['centro_propuesto'] == row['centro_propuesto']) &
                    (df_final['via'] == via_label)
                ][['TITULO', 'LINEA_INVESTIGACION', 'CUARTIL']].head(4)
                f.write("  Muestra:\n")
                for _, s in sample.iterrows():
                    f.write(f"    • [{s['CUARTIL']}][{str(s['LINEA_INVESTIGACION'])[:40]}] {str(s['TITULO'])[:80]}...\n")
                f.write("\n")

        biblio = df_final[df_final['via'] == 'Revisión Bibliográfica']
        f.write("=" * 70 + "\n")
        f.write(f"REVISIONES BIBLIOGRÁFICAS (no asignadas): {len(biblio)} artículos\n")
        f.write("=" * 70 + "\n")

    print(f"  ✅ produccion_clasificada_definitiva.csv")
    print(f"  ✅ impacto_por_centro_definitivo.csv")
    print(f"  ✅ REPORTE_FINAL_CENTROS.txt")


# ===================== EJECUCIÓN PRINCIPAL =====================
if __name__ == "__main__":
    df = load_and_clean()
    df = classify_v2(df)
    df = build_context(df)

    df_exp    = df[df['TIPO_INVESTIGACION'] == 'EXPERIMENTAL'].copy()
    df_social = df[df['TIPO_INVESTIGACION'] == 'CIENCIAS_SOCIALES'].copy()
    df_biblio = df[df['TIPO_INVESTIGACION'] == 'BIBLIOGRÁFICA/REVISIÓN'].copy()

    print(f"\n  📊 Artículos Experimentales:    {len(df_exp)}")
    print(f"  📊 Artículos Ciencias Sociales: {len(df_social)}")
    print(f"  📊 Revisiones Bibliográficas:   {len(df_biblio)}")

    df_exp    = cluster_via_a(df_exp)
    df_social = cluster_via_b(df_social)
    df_biblio = handle_bibliographic(df_biblio)

    df_final = pd.concat([df_exp, df_social, df_biblio], ignore_index=True)

    impacto = generate_impact_report(df_final)
    save_all(df_final, impacto)

    print("\n" + "=" * 70)
    print("✅ PROTOCOLO COMPLETO EJECUTADO CON ÉXITO")
    print("=" * 70)
