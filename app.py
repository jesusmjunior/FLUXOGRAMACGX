import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

# Título geral
titulo = "Fluxogramas – Provimentos COGEX/TJMA"
st.set_page_config(page_title=titulo, layout="wide")
st.title(titulo)

# Seletor de provimento
opcao = st.selectbox("Selecione o Provimento:", ["Provimento nº 31/2024", "Provimento nº 33/2024"])

# Definições de grafos
if opcao == "Provimento nº 33/2024":
    nodes = [
        Node(id="INÍCIO", label="INÍCIO"),
        Node(id="estudo", label="Estudo Interno da Corregedoria"),
        Node(id="fiscalizacao", label="Necessidade em Fiscalização"),
        Node(id="solicitacao", label="Solicitação de Atualização"),
        Node(id="minuta", label="Redação da Minuta Normativa"),
        Node(id="analise", label="Análise Jurídica (Código de Normas)"),
        Node(id="precedentes", label="Consulta CNJ / Prov. 16/2022"),
        Node(id="aprovacao", label="Aprovação Final pela COGEX"),
        Node(id="publicacao", label="Publicação do Provimento nº 33/2024"),
        Node(id="vinculacao", label="Vinculação às Serventias Extrajudiciais"),
        Node(id="obrigatoriedade", label="Cumprimento Imediato Obrigatório"),
        Node(id="FIM", label="FIM")
    ]
    edges = [
        Edge(source="INÍCIO", target="estudo"),
        Edge(source="estudo", target="fiscalizacao"),
        Edge(source="fiscalizacao", target="solicitacao"),
        Edge(source="solicitacao", target="minuta"),
        Edge(source="minuta", target="analise"),
        Edge(source="analise", target="precedentes"),
        Edge(source="precedentes", target="aprovacao"),
        Edge(source="aprovacao", target="publicacao"),
        Edge(source="publicacao", target="vinculacao"),
        Edge(source="vinculacao", target="obrigatoriedade"),
        Edge(source="obrigatoriedade", target="FIM")
    ]

elif opcao == "Provimento nº 31/2024":
    nodes = [
        Node(id="INÍCIO", label="INÍCIO"),
        Node(id="avaliar", label="Avaliar Aplicabilidade Normativa"),
        Node(id="minuta", label="Formular Minuta de Revogação"),
        Node(id="juridico", label="Consultar Setor Jurídico"),
        Node(id="publicar", label="Publicar Provimento nº 31/2024"),
        Node(id="notificar", label="Notificar Serventias"),
        Node(id="FIM", label="FIM")
    ]
    edges = [
        Edge(source="INÍCIO", target="avaliar"),
        Edge(source="avaliar", target="minuta"),
        Edge(source="minuta", target="juridico"),
        Edge(source="juridico", target="publicar"),
        Edge(source="publicar", target="notificar"),
        Edge(source="notificar", target="FIM")
    ]

# Configuração comum do grafo
config = Config(
    width=1000,
    height=600,
    directed=True,
    physics=False,
    hierarchical=True,
    nodeHighlightBehavior=True,
    highlightColor="#F7A7A6",
    collapsible=True
)

st.markdown(f"### Visualização do Fluxograma – {opcao}")
agraph(nodes=nodes, edges=edges, config=config)
