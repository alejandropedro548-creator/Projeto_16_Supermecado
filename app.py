### Importando as blibiotecas
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
###Criando uma sessão para salvar os produtos
if "produtos" not in st.session_state:
   st.session_state.produtos = []
### Criando as TABS ou Abas
st.title("Atacadão Do Lima")
Cadastro, Compras, Sobre =st.tabs(["Cadastro","Compras","Sobre Nós"])

### Usando a TAG Cadastro
with Cadastro:
    ### Solicitando informações do produto
    nome_produto = st.text_input("Digite o Nome do Produto")
    preco_produto = st.text_input("Digite o Preço do Produto")
    quantidade_produto = st.text_input("Digite a Quantidade do Produto")
    data_cadastro = st.date_input("Escolha a Data de Cadastro do Produto",format="DD/MM/YYYY")
    data_vencimento = st.date_input("Escolha a Data de Vencimento do Produto",format="DD/MM/YYYY")

    ###Criando uma lsta de dicionários
   
    produtos = []
    produto = {
        "Nome_Produto":nome_produto,
        "Preco":preco_produto,
        "Quantidade":quantidade_produto,
        "Data_Cadastro":data_cadastro,
        "Data_Vencimento":data_vencimento
    }
    ### Criando um botão
    if st.button("Cadastrar"):
        st.session_state.produtos.append(produto)
        st.success(f"O Produto {produto["Nome_Produto"]}, Foi cadastrado com sucesso!!!")



with Compras:
    df = pd.DataFrame(st.session_state.produtos)
    #st.dataframe(df)
    produtos_cadastrados = df['Nome_Produto'].unique().tolist()
    st.selectbox('Escolha o produto:',produtos_cadastrados)


#st.write(st.session_state.produtos)

with Sobre:
    st.title("🏪 Sobre o Atacadão do Ale")

    st.markdown("""
    Nosso compromisso é oferecer produtos de qualidade, economia e um atendimento que faça nossos clientes voltarem sempre.
    """)

    st.divider()

    col1, col2 = st.columns([2,1])

    with col1:
        st.subheader("Quem Somos")

        st.write("""
Somos um mercado focado em qualidade, variedade e atendimento.

Trabalhamos diariamente para oferecer produtos frescos, preços competitivos e um ambiente organizado para toda a família.
""")

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1542838132-92c53300491e",
            use_container_width=True
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1604719312566-8912e9c8a213",
            use_container_width=True
        )

    with col2:
        st.subheader("Nossa Missão")

        st.write("""
Oferecer produtos de qualidade com preços acessíveis, garantindo uma experiência de compra rápida, segura e agradável.
""")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Hortifruti")

        st.write("""
Frutas, legumes e verduras selecionados diariamente para garantir frescor e qualidade.
""")

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1542838138-8c7aa8026d6c",
            use_container_width=True
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1607623814075-e51df1bdc82f",
            use_container_width=True
        )

    with col2:
        st.subheader("Açougue")

        st.write("""
Carnes selecionadas, cortes especiais e rigoroso controle de qualidade.
""")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Padaria")

        st.write("""
Pães fresquinhos, bolos, doces e salgados preparados diariamente.
""")

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1509440159596-0249088772ff",
            use_container_width=True
        )

    st.divider()

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1521791136064-7986c2920216",
            use_container_width=True
        )

    with col2:
        st.subheader("Nossa Equipe")

        st.write("""
Nossa equipe é formada por profissionais capacitados e comprometidos em oferecer um atendimento cordial, rápido e eficiente.
""")

        st.dataframe(
            {
                "Nome": [
                    "João Silva",
                    "Maria Souza",
                    "Carlos Lima",
                    "Ana Oliveira"
                ],
                "Cargo": [
                    "Gerente",
                    "Operadora de Caixa",
                    "Repositor",
                    "Atendimento"
                ]
            },
            use_container_width=True
        )

    st.divider()

    st.subheader("Nosso Compromisso")

    st.success("""
✔ Produtos de qualidade

✔ Atendimento de excelência

✔ Economia para sua família

✔ Ambiente limpo e organizado

✔ Satisfação do cliente em primeiro lugar
""")

    st.info("""
📍 Rua Exemplo, 123

📞 (11) 99999-9999

✉ contato@atacadaodoale.com.br
""")