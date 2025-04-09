import streamlit as st
from PIL import Image
from graphviz import Digraph
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Fluxograma Administrativo - TJMA", layout="wide")

# Exibe a imagem de fundo (layout institucional)
image = Image.open("TITULO DO PROCESSO.png")
st.image(image, use_column_width=True)

st.markdown("## 📜 Fluxograma Administrativo - Provimento nº 33/2024")

# Dados do processo
entrada = [
    "Estudo interno da Corregedoria",
    "Relatórios de fiscalização",
    "Solicitação normativa"
]

processamento = [
    "Redação da minuta",
    "Análise jurídica",
    "Consulta a precedentes CNJ",
    "Aprovação final COGEX"
]

output = [
    "Publicação oficial",
    "Vinculação às serventias",
    "Cumprimento obrigatório"
]

# Geração do fluxograma com Graphviz
dot = Digraph()
dot.attr(rankdir='TB', size='10')

dot.node("start", "📥 Entrada", shape="ellipse", style="filled", fillcolor="lightblue")

for i, e in enumerate(entrada):
    dot.node(f"entrada_{i}", e, shape="box", style="filled", fillcolor="lightyellow")
    dot.edge("start", f"entrada_{i}")

dot.node("proc", "⚙️ Processamento", shape="ellipse", style="filled", fillcolor="lightgreen")
dot.edge("entrada_2", "proc")

for i, p in enumerate(processamento):
    dot.node(f"proc_{i}", p, shape="box", style="filled", fillcolor="khaki")
    if i == 0:
        dot.edge("proc", f"proc_{i}")
    else:
        dot.edge(f"proc_{i-1}", f"proc_{i}")

dot.node("decision", "Consulta CNJ?", shape="diamond", style="filled", fillcolor="lightpink")
dot.edge("proc_1", "decision")
dot.edge("decision", "proc_2", label="Sim")
dot.edge("decision", "proc_3", label="Não")

dot.node("end", "📤 Output", shape="ellipse", style="filled", fillcolor="lightblue")
for i, o in enumerate(output):
    dot.node(f"saida_{i}", o, shape="box", style="filled", fillcolor="lightcyan")
    dot.edge("proc_3", f"saida_{i}")
    dot.edge("proc_2", f"saida_{i}")
    dot.edge(f"saida_{i}", "end")

st.graphviz_chart(dot, use_container_width=True)

# Rodapé com legenda simbólica
st.markdown("""
---

### 📌 Simbologia:
- 🟦 Elipse: Início/Fim
- 🟨 Retângulo: Etapas processuais
- 🔶 Losango: Decisão/Condição
- 🔷 Caixas: Saídas/Resultados

### 📘 Legenda:
Representação do ciclo normativo institucional automatizado via lógica fuzzy α → θ.

---
""")
