import streamlit as st
from PIL import Image
import plotly.graph_objects as go

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(layout="wide", page_title="Provimento nº 27/2024")

# CSS CENTRALIZADO
st.markdown("""
    <style>
    .titulo-processo {
        font-size: 42px;
        font-weight: 900;
        text-align: center;
        padding: 20px 0 10px 0;
    }
    .container-imagem {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .bloco-inferior {
        display: flex;
        justify-content: space-around;
        background-color: #f9e2e2;
        padding: 15px;
        border-radius: 15px;
        font-size: 16px;
    }
    .bloco-inferior div {
        width: 45%;
    }
    </style>
""", unsafe_allow_html=True)

# TÍTULO
st.markdown("<div class='titulo-processo'>Provimento nº 27/2024</div>", unsafe_allow_html=True)

# IMAGEM DE CABEÇALHO INSTITUCIONAL
with st.container():
    img = Image.open("TITULO DO PROCESSO.png")
    st.image(img, use_column_width=True)

# DIAGRAMA FLUXOGRAMA - PLOTLY
st.subheader("Fluxograma Interativo")

fig = go.Figure()

# Coordenadas X/Y e blocos (representação simples interativa)
nodes = [
    ("Início", 0, 5),
    ("Denúncia sobre erro registral", 1, 5),
    ("Ausência de pacto antenupcial?", 2, 5),
    ("Levantar registros afetados", 3, 5),
    ("Aplicar Súmula 377", 4, 5),
    ("Determinar retificação", 5, 5),
    ("Emitir determinação normativa", 6, 5),
    ("Notificar cartórios", 7, 5),
    ("Regularizar registro", 8, 5),
    ("Arquivamento", 9, 5),
    ("Fim", 10, 5)
]

for name, x, y in nodes:
    fig.add_trace(go.Scatter(x=[x], y=[y], text=[name], mode='text+markers',
                             marker=dict(size=40, color='lightblue'),
                             textposition="top center"))

fig.update_layout(showlegend=False, height=500,
                  margin=dict(l=20, r=20, t=20, b=20),
                  xaxis=dict(visible=False), yaxis=dict(visible=False))

st.plotly_chart(fig, use_container_width=True)

# SIMBOLOGIA E LEGENDA
st.markdown("---")
st.markdown("<div class='bloco-inferior'>"
            "<div><b>Simbologia:</b><br>"
            "- 🟠 Início/Fim<br>"
            "- ▭ Processo<br>"
            "- ◇ Decisão<br>"
            "- 🗎 Documento<br>"
            "- 🔽 Arquivamento</div>"
            "<div><b>Legenda:</b><br>"
            "Fluxograma institucional da retificação administrativa de ofício, "
            "de acordo com o Provimento nº 27/2024, incluindo análise da existência de pacto antenupcial, "
            "aplicação da Súmula 377 e ações formais de regularização cartorial.</div>"
            "</div>", unsafe_allow_html=True)

# RODAPÉ
st.markdown("---")
st.caption("Sistema de Mapeamento Automatizado - COGEX/TJMA")
