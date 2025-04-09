
import streamlit as st
from PIL import Image
import graphviz

# Configuração da página
st.set_page_config(layout="wide")
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<div class='title'>Provimento nº 27/2024</div>", unsafe_allow_html=True)

# Imagem de fundo do template
st.subheader("Template Institucional")
background = Image.open("TITULO DO PROCESSO.png")
st.image(background, use_column_width=True)

# Geração do fluxograma com Graphviz
st.subheader("Fluxograma Gerado")
dot = graphviz.Digraph()

dot.attr(rankdir='TB', size='8,10')
dot.attr('node', shape='circle', style='filled', fillcolor='lightgray')

dot.node("start", "🟠 Início", shape='ellipse', fillcolor='lightgreen')
dot.node("erro", "▭ Denúncia sobre erro registral", shape='box', fillcolor='white')
dot.node("decisao_pacto", "◇ Ausência de pacto antenupcial?", shape='diamond', fillcolor='lightblue')
dot.node("levantamento", "▭ Levantar registros afetados", shape='box')
dot.node("sumula", "◇ Aplicar Súmula 377 do STF", shape='diamond')
dot.node("retificacao", "▭ Determinar retificação de ofício", shape='box')
dot.node("normativa", "🗎 Emitir determinação normativa", shape='note')
dot.node("notificar", "🗎 Notificar os cartórios", shape='note')
dot.node("regularizar", "▭ Regularizar o registro", shape='box')
dot.node("arquivo", "🔽 Arquivamento", shape='box', fillcolor='lightyellow')
dot.node("fim", "🟠 Fim", shape='ellipse', fillcolor='lightgreen')

dot.edge("start", "erro")
dot.edge("erro", "decisao_pacto")
dot.edge("decisao_pacto", "levantamento", label="Sim")
dot.edge("levantamento", "sumula")
dot.edge("sumula", "retificacao")
dot.edge("retificacao", "normativa")
dot.edge("normativa", "notificar")
dot.edge("notificar", "regularizar")
dot.edge("regularizar", "arquivo")
dot.edge("arquivo", "fim")

st.graphviz_chart(dot, use_container_width=True)

# Simbologia e legenda
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Simbologia:**")
    st.markdown("""
    - ▭ Processo
    - ◇ Decisão
    - 🗎 Documento
    - 🔽 Arquivamento
    - 🟠 Início/Fim
    """)

with col2:
    st.markdown("**Legenda:**")
    st.markdown("""
    Este fluxograma representa o procedimento de retificação administrativa de ofício com base no Provimento nº 27/2024,
    envolvendo etapas de análise, aplicação da Súmula 377 do STF, e comunicação aos cartórios.
    """)

# Rodapé
st.markdown("---")
st.caption("Sistema de Mapeamento Automatizado - COGEX/TJMA")
