"""
==========================================================================
GENERADOR DE FIGURAS DEFINITIVAS v3
Centros de Investigación UTMACH - Sistema de Dos Vías
Corpus: Artículos 2022–2026
==========================================================================
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUT = r"c:\Users\andre\Mi unidad\DIRECCIÓN DE INVESTIGACIÓN\Centros de Investigación\02_analisis\resultados"
FIG = os.path.join(OUT, "figuras")
os.makedirs(FIG, exist_ok=True)

# ── Cargar datos definitivos (filtrados 2022+) ──────────────────────────
df      = pd.read_csv(os.path.join(OUT, "produccion_clasificada_definitiva.csv"))
impacto = pd.read_csv(os.path.join(OUT, "impacto_por_centro_definitivo.csv"))

# Nombres reales de las vías en el CSV
VIA_A_LABEL = 'A – Ciencias Experimentales'
VIA_B_LABEL = 'B – Ciencias Sociales y Humanísticas'

# Colores institucionales
COLORS_VIA_A = ['#1a5276', '#2e86c1', '#5dade2', '#85c1e9']
COLORS_VIA_B = ['#6c3483', '#9b59b6', '#bb8fce', '#d7bde2']
COLOR_BIBLIO = '#bdc3c7'

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size']   = 11

TOTAL = len(df)
ANNO  = "2022–2026"

# ====================================================================
# FIGURA 1: PIE — Clasificación global de producción
# ====================================================================
fig, ax = plt.subplots(figsize=(10, 7))

counts = df['TIPO_INVESTIGACION'].value_counts()

label_map = {
    'EXPERIMENTAL':          f'Experimental\n(Laboratorio/Campo)',
    'CIENCIAS_SOCIALES':     f'Ciencias Sociales\ny Humanísticas',
    'BIBLIOGRÁFICA/REVISIÓN': 'Revisiones\nBibliográficas',
}
color_map = {
    'EXPERIMENTAL':          '#2e86c1',
    'CIENCIAS_SOCIALES':     '#8e44ad',
    'BIBLIOGRÁFICA/REVISIÓN': '#bdc3c7',
}

labels_pie = [label_map.get(t, t) for t in counts.index]
colors_pie = [color_map.get(t, '#95a5a6') for t in counts.index]

wedges, texts, autotexts = ax.pie(
    counts.values, labels=labels_pie, colors=colors_pie,
    autopct=lambda p: f'{p:.1f}%\n({int(round(p*TOTAL/100))})',
    startangle=140, explode=[0.03]*len(counts),
    textprops={'fontsize': 12, 'fontweight': 'bold'},
    pctdistance=0.75
)
for at in autotexts:
    at.set_fontsize(11)
    at.set_color('white')
    at.set_fontweight('bold')

ax.set_title(
    f'Clasificación de la Producción Científica UTMACH\n({TOTAL:,} Artículos · {ANNO})',
    fontsize=16, fontweight='bold', pad=20
)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "01_clasificacion_produccion.png"), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figura 1: Clasificación")

# ====================================================================
# FIGURA 2: BARRAS HORIZONTALES — Impacto ponderado por Centro/Observatorio
# ====================================================================
fig, ax = plt.subplots(figsize=(14, 8))

via_a = impacto[impacto['via'] == VIA_A_LABEL].sort_values('suma_ponderada')
via_b = impacto[impacto['via'] == VIA_B_LABEL].sort_values('suma_ponderada')

all_names, all_values, all_colors, all_articles = [], [], [], []

for _, row in via_b.iterrows():
    name = row['centro_propuesto'].replace('Observatorio de ', 'O. ').replace('Observatorio ', 'O. ')
    all_names.append(name);  all_values.append(row['suma_ponderada'])
    all_colors.append('#8e44ad'); all_articles.append(row['total_articulos'])

# Separador
all_names.append(''); all_values.append(0)
all_colors.append('white'); all_articles.append(0)

for _, row in via_a.iterrows():
    name = row['centro_propuesto'].replace('Centro de Investigación ', 'C. ').replace('Centro ', 'C. ')
    all_names.append(name);  all_values.append(row['suma_ponderada'])
    all_colors.append('#2e86c1'); all_articles.append(row['total_articulos'])

y_pos = range(len(all_names))
bars = ax.barh(y_pos, all_values, color=all_colors, edgecolor='white', height=0.7)

for i, (bar, arts) in enumerate(zip(bars, all_articles)):
    if all_values[i] > 0:
        ax.text(bar.get_width() + 3, bar.get_y() + bar.get_height()/2,
                f'{all_values[i]:.0f} pts ({arts} arts.)',
                va='center', fontsize=9, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(all_names, fontsize=10)
ax.set_xlabel('Impacto Ponderado (Q1=1.0, Q2=0.9, Q3=0.8, Q4=0.7)', fontsize=12)
ax.set_title(
    f'Impacto Ponderado por Centro / Observatorio\nSistema de Dos Vías — UTMACH ({ANNO})',
    fontsize=14, fontweight='bold'
)
legend_patches = [
    mpatches.Patch(color='#2e86c1', label='Vía A: Centros Experimentales'),
    mpatches.Patch(color='#8e44ad', label='Vía B: Observatorios Sociales'),
]
ax.legend(handles=legend_patches, loc='lower right', fontsize=11)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "02_impacto_por_centro.png"), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figura 2: Impacto por Centro/Observatorio")

# ====================================================================
# FIGURA 3: CUARTILES POR VÍA (Stacked Bar)
# ====================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

for idx, (via_label, color_base, ax_title) in enumerate([
    (VIA_A_LABEL, '#2e86c1', 'VÍA A: Centros Experimentales'),
    (VIA_B_LABEL, '#8e44ad', 'VÍA B: Observatorios Sociales'),
]):
    via_data = impacto[impacto['via'] == via_label]
    ax = axes[idx]
    names, q1s, q2s, q3s, q4s, otros = [], [], [], [], [], []

    for _, row in via_data.sort_values('total_articulos', ascending=True).iterrows():
        name = row['centro_propuesto']
        name = name.replace('Centro de Investigación ', 'C. ')
        name = name.replace('Observatorio de ', 'O. ')
        name = name.replace('Observatorio ', 'O. ')
        name = name.replace('Centro ', 'C. ')
        names.append(name)
        q1s.append(row['articulos_Q1']);  q2s.append(row['articulos_Q2'])
        q3s.append(row['articulos_Q3']);  q4s.append(row['articulos_Q4'])
        otros.append(row['total_articulos']
                     - row['articulos_Q1'] - row['articulos_Q2']
                     - row['articulos_Q3'] - row['articulos_Q4'])

    y = range(len(names))
    ax.barh(y, q1s, color='#e74c3c', label='Q1', height=0.6)
    ax.barh(y, q2s, left=q1s, color='#e67e22', label='Q2', height=0.6)
    left_q3 = [a+b for a,b in zip(q1s,q2s)]
    ax.barh(y, q3s, left=left_q3, color='#f1c40f', label='Q3', height=0.6)
    left_q4 = [a+b+c for a,b,c in zip(q1s,q2s,q3s)]
    ax.barh(y, q4s, left=left_q4, color='#27ae60', label='Q4', height=0.6)
    left_otros = [a+b+c+d for a,b,c,d in zip(q1s,q2s,q3s,q4s)]
    ax.barh(y, otros, left=left_otros, color='#bdc3c7', label='Sin Cuartil', height=0.6)

    ax.set_yticks(y); ax.set_yticklabels(names, fontsize=9)
    ax.set_title(ax_title, fontsize=13, fontweight='bold')
    ax.set_xlabel('Número de Artículos', fontsize=10)
    ax.legend(fontsize=8, loc='lower right')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

plt.suptitle(
    f'Distribución de Cuartiles por Centro/Observatorio ({ANNO})',
    fontsize=15, fontweight='bold', y=1.02
)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "03_cuartiles_por_centro.png"), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figura 3: Cuartiles por Centro")

# ====================================================================
# FIGURA 4: TOP LÍNEAS DE INVESTIGACIÓN (Experimental vs Social)
# ====================================================================
fig, axes = plt.subplots(1, 2, figsize=(18, 9))

for idx, (tipo, color, title) in enumerate([
    ('EXPERIMENTAL',   '#2e86c1', f'Top 10 Líneas — Experimental ({ANNO})'),
    ('CIENCIAS_SOCIALES', '#8e44ad', f'Top 10 Líneas — C. Sociales ({ANNO})'),
]):
    ax = axes[idx]
    sub = df[df['TIPO_INVESTIGACION'] == tipo]
    top = sub['LINEA_INVESTIGACION'].value_counts().head(10)
    names = [str(n)[:48]+'…' if len(str(n)) > 48 else str(n) for n in top.index]

    bars = ax.barh(range(len(names)), top.values, color=color, edgecolor='white', height=0.7)
    ax.set_yticks(range(len(names))); ax.set_yticklabels(names, fontsize=9)
    ax.invert_yaxis()
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.set_xlabel('Número de Artículos', fontsize=10)
    for bar, val in zip(bars, top.values):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                str(val), va='center', fontsize=10, fontweight='bold')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

plt.suptitle(
    f'Top Líneas de Investigación por Tipo de Producción ({ANNO})',
    fontsize=15, fontweight='bold', y=1.01
)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "04_top_lineas_por_tipo.png"), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figura 4: Top Líneas por Tipo")

# ====================================================================
# FIGURA 5: MASA CRÍTICA IPPC POR FACULTAD Y CLUSTER
# ====================================================================
ippc_file = os.path.join(OUT, "ippc_3años_activos_clustered.csv")
if os.path.exists(ippc_file):
    dfippc = pd.read_csv(ippc_file)
    fac_col = 'FACULTAD'
    cluster_col = 'Cluster'
    
    if fac_col in dfippc.columns and cluster_col in dfippc.columns:
        fig, ax = plt.subplots(figsize=(14, 8))
        
        pivot = dfippc.groupby([fac_col, cluster_col]).size().unstack(fill_value=0)
        
        colors_ippc = {
            'A - Élite': '#c0392b',
            'B - Consolidados': '#e67e22',
            'C - En Desarrollo': '#f1c40f',
            'D - Sin Actividad Significativa': '#bdc3c7'
        }
        
        for c in colors_ippc.keys():
            if c not in pivot.columns:
                pivot[c] = 0
                
        pivot_sorted = pivot.loc[pivot.sum(axis=1).sort_values(ascending=True).index]
        
        bottom = np.zeros(len(pivot_sorted))
        cluster_order = ['D - Sin Actividad Significativa', 'C - En Desarrollo', 'B - Consolidados', 'A - Élite']
        
        for cluster_name in cluster_order:
            vals = pivot_sorted[cluster_name].values
            color = colors_ippc.get(cluster_name, '#95a5a6')
            bars = ax.barh(range(len(pivot_sorted)), vals, left=bottom, label=cluster_name, color=color, height=0.6)
            bottom += vals
            
            for bar, val in zip(bars, vals):
                if val > 0:
                    ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + bar.get_height()/2,
                            str(int(val)), va='center', ha='center', color='white' if cluster_name in ['A - Élite', 'B - Consolidados'] else 'black', 
                            fontsize=9, fontweight='bold')
        
        ax.set_yticks(range(len(pivot_sorted)))
        short_facs = [f.replace('FACULTAD DE ', '').title() for f in pivot_sorted.index]
        ax.set_yticklabels(short_facs, fontsize=10)
        ax.set_xlabel('Número de Docentes Investigadores', fontsize=12)
        ax.set_title('Masa Crítica IPPC por Facultad y Cluster\nUTMACH', fontsize=15, fontweight='bold')
        
        textstr = '\n'.join((
            'Significado Estratégico del Talento Humano:',
            '■ Élite (Rojo): Líderes de impacto (Q1/Q2). Motores de los nuevos Centros.',
            '■ Consolidados (Naranja): Producción sólida que sostiene el Centro.',
            '■ En Desarrollo (Amarillo): Semillero e investigadores noveles.',
            '■ Sin Actividad (Gris): Potencial humano, reto clave de integración.'
        ))
        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        ax.text(0.50, 0.05, textstr, transform=ax.transAxes, fontsize=11,
                verticalalignment='bottom', bbox=props)
        
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1], fontsize=11, loc='upper left', bbox_to_anchor=(1, 1))
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.tight_layout()
        plt.savefig(os.path.join(FIG, "05_masa_critica_ippc.png"), dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ Figura 5: Masa Crítica IPPC")

# ====================================================================
# FIGURA 6: PROPORCIÓN DE CALIDAD (Q1+Q2 / Total por Centro)
# ====================================================================
fig, ax = plt.subplots(figsize=(13, 7))

impacto_act = impacto[impacto['via'].isin([VIA_A_LABEL, VIA_B_LABEL])].copy()
impacto_act['pct_calidad'] = (
    (impacto_act['articulos_Q1'] + impacto_act['articulos_Q2']) /
    impacto_act['total_articulos'].replace(0, np.nan) * 100
).fillna(0)

impacto_act = impacto_act.sort_values('pct_calidad', ascending=True)
colors_cal = ['#2e86c1' if v == VIA_A_LABEL else '#8e44ad' for v in impacto_act['via']]

short_names = []
for _, row in impacto_act.iterrows():
    n = row['centro_propuesto']
    n = n.replace('Centro de Investigación ', 'C. ').replace('Observatorio de ', 'O. ')
    short_names.append(n)

bars = ax.barh(range(len(short_names)), impacto_act['pct_calidad'].values,
               color=colors_cal, edgecolor='white', height=0.65)

for i, bar in enumerate(bars):
    row = impacto_act.iloc[i]
    pct = impacto_act['pct_calidad'].values[i]
    n_q12 = int(row['articulos_Q1'] + row['articulos_Q2'])
    label = f"  {pct:.1f}%  ({n_q12} arts. Q1+Q2)"
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            label, va='center', fontsize=9, fontweight='bold')

ax.set_yticks(range(len(short_names)))
ax.set_yticklabels(short_names, fontsize=9)
ax.set_xlabel('% Artículos en Q1 o Q2 (Alta Calidad)', fontsize=12)
ax.set_title(
    f'Proporción de Artículos de Alta Calidad (Q1+Q2) por Centro\nUTMACH {ANNO}',
    fontsize=14, fontweight='bold'
)
legend_patches = [
    mpatches.Patch(color='#2e86c1', label='Vía A: Centros Experimentales'),
    mpatches.Patch(color='#8e44ad', label='Vía B: Observatorios Sociales'),
]
ax.legend(handles=legend_patches, fontsize=10)
ax.set_xlim(0, max(impacto_act['pct_calidad'].values) * 1.5)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "06_proporcion_calidad_q1q2.png"), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figura 6: Proporción Q1+Q2 por Centro")

# ====================================================================
# FIGURA 7: DASHBOARD EJECUTIVO 2x2
# ====================================================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle(
    f'DASHBOARD EJECUTIVO: Centros de Investigación UTMACH\n{ANNO} — {TOTAL:,} artículos analizados',
    fontsize=16, fontweight='bold', y=0.99
)

# Panel 1: Clasificación Pie
ax1 = axes[0, 0]
counts2 = df['TIPO_INVESTIGACION'].value_counts()
label_map2 = {
    'EXPERIMENTAL':          'Experimental',
    'CIENCIAS_SOCIALES':     'C. Sociales',
    'BIBLIOGRÁFICA/REVISIÓN': 'Revisiones',
}
labels2 = [label_map2.get(t, t) for t in counts2.index]
colors2 = [color_map.get(t, '#95a5a6') for t in counts2.index]
ax1.pie(counts2.values, labels=labels2, colors=colors2,
        autopct='%1.1f%%', startangle=140,
        textprops={'fontsize': 11, 'fontweight': 'bold'})
ax1.set_title('Clasificación de Producción', fontsize=13, fontweight='bold')

# Panel 2: Distribución Cuartiles (barras)
ax2 = axes[0, 1]
cuartil_map = df['CUARTIL'].fillna('NO APLICA').replace({'': 'NO APLICA'})
q_order  = ['Q1', 'Q2', 'Q3', 'Q4', 'NO APLICA']
q_colors = ['#e74c3c', '#e67e22', '#f1c40f', '#27ae60', '#bdc3c7']
q_counts = [int((cuartil_map == q).sum()) for q in q_order]
bars2 = ax2.bar(q_order, q_counts, color=q_colors, edgecolor='white')
ax2.set_title(f'Distribución de Cuartiles ({ANNO})', fontsize=13, fontweight='bold')
ax2.set_ylabel('Artículos')
for bar, val in zip(bars2, q_counts):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
             str(val), ha='center', fontsize=11, fontweight='bold')
ax2.spines['top'].set_visible(False); ax2.spines['right'].set_visible(False)

# Panel 3: Vía A
ax3 = axes[1, 0]
va = impacto[impacto['via'] == VIA_A_LABEL].sort_values('suma_ponderada', ascending=True)
names_a = [r['centro_propuesto'].replace('Centro de Investigación ', '').replace('Centro ', '')[:35]
           for _, r in va.iterrows()]
ax3.barh(range(len(names_a)), va['suma_ponderada'].values, color=COLORS_VIA_A[:len(names_a)], height=0.6)
ax3.set_yticks(range(len(names_a))); ax3.set_yticklabels(names_a, fontsize=9)
for i, (v, n) in enumerate(zip(va['suma_ponderada'].values, va['total_articulos'].values)):
    ax3.text(v + 1, i, f'{v:.0f} pts · {n} arts', va='center', fontsize=8)
ax3.set_title('VÍA A — Centros Experimentales\n(Impacto Ponderado)', fontsize=12, fontweight='bold')
ax3.spines['top'].set_visible(False); ax3.spines['right'].set_visible(False)

# Panel 4: Vía B
ax4 = axes[1, 1]
vb = impacto[impacto['via'] == VIA_B_LABEL].sort_values('suma_ponderada', ascending=True)
names_b = [r['centro_propuesto'].replace('Observatorio de ', '').replace('Observatorio ', '')[:35]
           for _, r in vb.iterrows()]
ax4.barh(range(len(names_b)), vb['suma_ponderada'].values, color=COLORS_VIA_B[:len(names_b)], height=0.6)
ax4.set_yticks(range(len(names_b))); ax4.set_yticklabels(names_b, fontsize=9)
for i, (v, n) in enumerate(zip(vb['suma_ponderada'].values, vb['total_articulos'].values)):
    ax4.text(v + 1, i, f'{v:.0f} pts · {n} arts', va='center', fontsize=8)
ax4.set_title('VÍA B — Observatorios Sociales\n(Impacto Ponderado)', fontsize=12, fontweight='bold')
ax4.spines['top'].set_visible(False); ax4.spines['right'].set_visible(False)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(os.path.join(FIG, "07_dashboard_ejecutivo.png"), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figura 7: Dashboard Ejecutivo")

print("\n" + "="*60)
print("✅ TODAS LAS FIGURAS GENERADAS (corpus 2022–2026)")
print("="*60)
