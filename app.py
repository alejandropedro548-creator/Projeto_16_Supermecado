# ============================================================
# FUTDADOS
# Sistema Inteligente de Análise e Desempenho no Futebol
# Dados totalmente fictícios
# ============================================================


# ============================================================
# IMPORTAÇÕES
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import random

import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(

    page_title="FutDados",

    page_icon="⚽",

    layout="wide",

    initial_sidebar_state="expanded"

)



# ============================================================
# CSS PERSONALIZADO
# ============================================================


st.markdown(

"""

<style>


@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap'
);



*{

    font-family:'Poppins', sans-serif;

}



.stApp{

    background:

    linear-gradient(

        135deg,

        #06121f,

        #0c2840,

        #073b27

    );

}



section[data-testid="stSidebar"]{

    background:#07131f;

    border-right:

    1px solid rgba(255,255,255,0.12);

}



h1,h2,h3,h4{

    color:white;

}



p,span,label{

    color:#d9d9d9;

}



.card{


    background:

    rgba(255,255,255,0.06);


    border:

    1px solid rgba(255,255,255,0.12);


    border-radius:22px;


    padding:25px;


    backdrop-filter:blur(15px);


    margin-bottom:20px;


}



.banner{


    background:

    linear-gradient(

        120deg,

        #0d6efd,

        #198754

    );


    padding:35px;


    border-radius:25px;


}



.metric-card{


    background:

    rgba(255,255,255,0.07);


    border-radius:18px;


    padding:20px;


    text-align:center;


    border:

    1px solid rgba(255,255,255,0.1);


}



.metric-card h1{


    color:#38ef7d;


}



.footer{


    text-align:center;


    color:#888;


    padding:30px;


}


</style>


""",

unsafe_allow_html=True

)



# ============================================================
# DADOS FICTÍCIOS
# ============================================================


random.seed(42)

np.random.seed(42)



nomes = [

"Lucas",
"Pedro",
"Gabriel",
"João",
"Matheus",
"Arthur",
"Rafael",
"Bruno",
"Leonardo",
"Victor",
"Caio",
"Henrique",
"Felipe",
"Gustavo",
"Samuel",
"Thiago",
"Eduardo",
"Vinicius",
"Diego",
"Rodrigo",
"Igor",
"Murilo",
"Yuri",
"Nathan",
"Davi",
"Alan",
"Jean",
"André"

]



sobrenomes = [

"Silva",
"Santos",
"Oliveira",
"Lima",
"Souza",
"Costa",
"Ferreira",
"Alves",
"Pereira",
"Rocha",
"Barbosa",
"Moura",
"Ribeiro",
"Teixeira"

]



clubes = [

"Atlético Paulista",

"União FC",

"Real Brasil",

"Estrela Futebol Clube",

"Nova Geração",

"Central Esportivo",

"Academia FC",

"Vila Futebol"

]



posicoes = [

"Goleiro",

"Zagueiro",

"Lateral",

"Volante",

"Meia",

"Ponta",

"Centroavante"

]



pes = [

"Direito",

"Esquerdo"

]



def gerar_nome():

    return (

        random.choice(nomes)

        +

        " "

        +

        random.choice(sobrenomes)

    )



jogadores=[]



for i in range(100):


    posicao=random.choice(posicoes)


    gols=random.randint(0,30)

    assistencias=random.randint(0,18)



    if posicao=="Goleiro":

        gols=random.randint(0,1)

        assistencias=random.randint(0,3)



    total_passes=random.randint(

        300,

        2000

    )


    passes_certos=int(

        total_passes *

        random.uniform(

            0.70,

            0.97

        )

    )



    nota=round(

        random.uniform(

            6.0,

            9.8

        ),

        1

    )


    fadiga=random.randint(

        10,

        95

    )



    if fadiga < 35:

        risco="Baixo"


    elif fadiga < 70:

        risco="Médio"


    else:

        risco="Alto"



    jogadores.append({


        "Jogador":

        gerar_nome(),


        "Idade":

        random.randint(

            17,

            36

        ),


        "Clube":

        random.choice(

            clubes

        ),


        "Posição":

        posicao,


        "Pé":

        random.choice(

            pes

        ),


        "Altura":

        random.randint(

            168,

            198

        ),


        "Peso":

        random.randint(

            65,

            95

        ),


        "Jogos":

        random.randint(

            5,

            40

        ),


        "Minutos":

        random.randint(

            300,

            3500

        ),


        "Gols":

        gols,


        "Assistências":

        assistencias,


        "Passes Certos":

        passes_certos,


        "Passes Errados":

        total_passes - passes_certos,


        "Precisão de Passe":

        round(

            passes_certos /

            total_passes *

            100,

            1

        ),


        "Desarmes":

        random.randint(

            5,

            120

        ),


        "Km Percorridos":

        round(

            random.uniform(

                7.5,

                13

            ),

            1

        ),


        "Sprints":

        random.randint(

            20,

            250

        ),


        "Velocidade Máxima":

        round(

            random.uniform(

                28,

                37

            ),

            1

        ),


        "Nota":

        nota,


        "Fadiga":

        fadiga,


        "Risco de Lesão":

        risco,


        "Valor de Mercado":

        round(

            random.uniform(

                1,

                100

            ),

            1

        ),


        "Potencial":

        random.randint(

            65,

            99

        )

    })



df=pd.DataFrame(jogadores)



# ============================================================
# ÍNDICE DE DESEMPENHO
# ============================================================


df["Índice de Desempenho"]=(


    df["Nota"]*10

    +

    df["Gols"]*2

    +

    df["Assistências"]*2

    +

    df["Precisão de Passe"]*0.4

    +

    df["Km Percorridos"]*2


)



df["Índice de Desempenho"]=round(

    df["Índice de Desempenho"],

    1

)



# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================


def criar_card(titulo,valor):

    st.markdown(

    f"""

    <div class="metric-card">

    <h3>{titulo}</h3>

    <h1>{valor}</h1>

    </div>

    """,

    unsafe_allow_html=True

    )



# ============================================================
# FIM DA PARTE 1
# ============================================================
# ============================================================
# SIDEBAR
# ============================================================


st.sidebar.markdown(

"""

<h1 style="color:#38ef7d">

⚽ FutDados

</h1>


<p>

Sistema Inteligente de Análise
e Desempenho no Futebol

</p>


""",

unsafe_allow_html=True

)



pagina = st.sidebar.radio(

    "Navegação",

    [

        "🏠 Início",

        "📊 Dashboard",

        "👀 Olheiro",

        "🧠 Analista de Dados",

        "👨‍🏫 Técnico",

        "🏃 Preparador Físico",

        "⚽ Jogador",

        "🔥 Mapa de Calor",

        "👥 Integrantes"

    ]

)



st.sidebar.divider()



st.sidebar.markdown(

"""

<div class="card">

<h4>📌 Informações</h4>


<b>Projeto:</b> FutDados


<br><br>


<b>Base:</b>

100 jogadores fictícios


<br><br>


<b>Objetivo:</b>

Demonstrar o uso de análise de dados
no futebol profissional.


</div>

""",

unsafe_allow_html=True

)



# ============================================================
# PÁGINA INICIAL
# ============================================================


if pagina == "🏠 Início":



    st.markdown(

    """

    <div class="banner">


    <h1>

    ⚽ FutDados

    </h1>



    <h2>

    Sistema Inteligente de Análise e Desempenho no Futebol

    </h2>



    <p style="font-size:18px">


    Transformando dados esportivos em decisões inteligentes.


    </p>



    </div>


    """,

    unsafe_allow_html=True

    )



    st.write("")



    # ========================================================
    # INDICADORES PRINCIPAIS
    # ========================================================


    c1,c2,c3,c4 = st.columns(4)



    with c1:

        criar_card(

            "👥 Jogadores",

            len(df)

        )



    with c2:

        criar_card(

            "⚽ Gols",

            int(

                df["Gols"]

                .sum()

            )

        )



    with c3:

        criar_card(

            "🎯 Assistências",

            int(

                df["Assistências"]

                .sum()

            )

        )



    with c4:

        criar_card(

            "⭐ Nota Média",

            round(

                df["Nota"]

                .mean(),

                2

            )

        )



    st.write("")



    esquerda,direita = st.columns(

        [2,1]

    )



    # ========================================================
    # EXPLICAÇÃO
    # ========================================================


    with esquerda:



        st.markdown(

        """

        <div class="card">


        <h2>

        📊 Sobre o FutDados

        </h2>



        <p>


        O FutDados simula um departamento
        de análise de desempenho de um clube
        de futebol.


        <br><br>


        O Analista de Dados recebe informações
        dos jogadores, identifica padrões,
        cria relatórios e entrega informações
        para auxiliar decisões.


        <br><br>


        Os dados podem ajudar:


        <br><br>


        👀 Olheiro:
        encontrar novos talentos.


        <br><br>


        👨‍🏫 Técnico:
        montar estratégias.


        <br><br>


        🏃 Preparador:
        controlar desempenho físico.


        <br><br>


        ⚽ Jogador:
        melhorar sua performance.


        </p>


        </div>


        """,

        unsafe_allow_html=True

        )



    # ========================================================
    # INTEGRANTES
    # ========================================================


    with direita:



        st.markdown(

        """

        <div class="card">


        <h2>

        👥 Equipe

        </h2>



        <p>


        📊 Pedro Alejandro

        <br>

        Analista de Dados


        <br><br>


        👀 Bruno

        <br>

        Olheiro


        <br><br>


        ⚽ Leonardo

        <br>

        Jogador


        <br><br>


        👨‍🏫 Luis Fernando

        <br>

        Técnico


        <br><br>


        🏃 Nicolas

        <br>

        Preparador Físico


        </p>


        </div>


        """,

        unsafe_allow_html=True

        )



    st.write("")



    # ========================================================
    # FLUXO PROFISSIONAL
    # ========================================================


    st.subheader(

        "🔄 Como os dados circulam no clube"

    )



    fluxo = st.columns(5)



    profissionais = [

        (

            "👀",

            "Olheiro",

            "Coleta informações"

        ),


        (

            "📊",

            "Analista",

            "Analisa dados"

        ),


        (

            "👨‍🏫",

            "Técnico",

            "Toma decisões"

        ),


        (

            "🏃",

            "Preparador",

            "Controla carga"

        ),


        (

            "⚽",

            "Jogador",

            "Evolui"

        )

    ]



    for coluna, item in zip(

        fluxo,

        profissionais

    ):


        with coluna:



            st.markdown(

            f"""

            <div class="card"

            style="text-align:center">


            <h1>

            {item[0]}

            </h1>


            <h4>

            {item[1]}

            </h4>


            <p>

            {item[2]}

            </p>


            </div>


            """,

            unsafe_allow_html=True

            )



    st.write("")



    # ========================================================
    # PRÉVIA DOS DADOS
    # ========================================================


    st.subheader(

        "📋 Base de jogadores"

    )



    st.dataframe(

        df.head(15),

        use_container_width=True,

        hide_index=True

    )



# ============================================================
# FIM DA PARTE 2
# ============================================================
# ============================================================
# DASHBOARD
# ============================================================


elif pagina == "📊 Dashboard":


    st.markdown(

    """

    <div class="banner">


    <h1>

    📊 Dashboard de Desempenho

    </h1>


    <p>

    Área responsável por transformar
    dados esportivos em informações
    para tomada de decisão.

    </p>


    </div>


    """,

    unsafe_allow_html=True

    )



    st.write("")



    # ========================================================
    # FILTROS
    # ========================================================


    filtro1,filtro2,filtro3 = st.columns(3)



    with filtro1:


        clube = st.selectbox(

            "🏟️ Clube",

            [

                "Todos"

            ]

            +

            sorted(

                df["Clube"]

                .unique()

                .tolist()

            )

        )



    with filtro2:


        posicao = st.selectbox(

            "⚽ Posição",

            [

                "Todas"

            ]

            +

            sorted(

                df["Posição"]

                .unique()

                .tolist()

            )

        )



    with filtro3:


        risco = st.selectbox(

            "🩺 Risco de lesão",

            [

                "Todos"

            ]

            +

            sorted(

                df["Risco de Lesão"]

                .unique()

                .tolist()

            )

        )



    dados = df.copy()



    if clube != "Todos":

        dados = dados[

            dados["Clube"]

            ==

            clube

        ]



    if posicao != "Todas":

        dados = dados[

            dados["Posição"]

            ==

            posicao

        ]



    if risco != "Todos":

        dados = dados[

            dados["Risco de Lesão"]

            ==

            risco

        ]



    st.divider()



    # ========================================================
    # INDICADORES
    # ========================================================


    a,b,c,d,e = st.columns(5)



    with a:

        criar_card(

            "👥 Atletas",

            len(dados)

        )


    with b:

        criar_card(

            "⚽ Gols",

            int(

                dados["Gols"]

                .sum()

            )

        )


    with c:

        criar_card(

            "🎯 Assistências",

            int(

                dados["Assistências"]

                .sum()

            )

        )


    with d:

        criar_card(

            "⭐ Nota média",

            round(

                dados["Nota"]

                .mean(),

                2

            )

        )


    with e:

        criar_card(

            "🔥 Índice médio",

            round(

                dados["Índice de Desempenho"]

                .mean(),

                1

            )

        )



    st.write("")



    # ========================================================
    # GRÁFICO 1
    # ========================================================


    col1,col2 = st.columns(2)



    with col1:



        gols = (

            dados

            .groupby(

                "Posição"

            )

            ["Gols"]

            .sum()

            .reset_index()

        )



        fig = px.bar(

            gols,

            x="Posição",

            y="Gols",

            color="Posição",

            title="⚽ Total de gols por posição"

        )



        fig.update_layout(

            template="plotly_dark",

            height=420

        )



        st.plotly_chart(

            fig,

            use_container_width=True

        )



    with col2:



        media = (

            dados

            .groupby(

                "Posição"

            )

            ["Nota"]

            .mean()

            .reset_index()

        )



        fig2 = px.line(

            media,

            x="Posição",

            y="Nota",

            markers=True,

            title="⭐ Nota média por posição"

        )



        fig2.update_layout(

            template="plotly_dark",

            height=420

        )



        st.plotly_chart(

            fig2,

            use_container_width=True

        )



    # ========================================================
    # GRÁFICO 2
    # ========================================================


    col3,col4 = st.columns(2)



    with col3:



        fig3 = px.scatter(

            dados,

            x="Km Percorridos",

            y="Nota",

            size="Índice de Desempenho",

            color="Posição",

            hover_name="Jogador",

            title="🏃 Desempenho físico x técnico"

        )



        fig3.update_layout(

            template="plotly_dark",

            height=450

        )



        st.plotly_chart(

            fig3,

            use_container_width=True

        )



    with col4:



        risco_df=(

            dados

            [

                "Risco de Lesão"

            ]

            .value_counts()

            .reset_index()

        )



        risco_df.columns=[

            "Risco",

            "Quantidade"

        ]



        fig4 = px.pie(

            risco_df,

            names="Risco",

            values="Quantidade",

            hole=.5,

            title="🩺 Controle de risco físico"

        )



        fig4.update_layout(

            template="plotly_dark",

            height=450

        )



        st.plotly_chart(

            fig4,

            use_container_width=True

        )



    st.divider()



    # ========================================================
    # RANKING
    # ========================================================


    st.subheader(

        "🏆 Ranking de desempenho"

    )



    ranking = (

        dados

        .sort_values(

            "Índice de Desempenho",

            ascending=False

        )

        .head(15)

    )



    fig5 = px.bar(

        ranking,

        x="Índice de Desempenho",

        y="Jogador",

        orientation="h",

        color="Índice de Desempenho",

        title="Top 15 jogadores"

    )



    fig5.update_layout(

        template="plotly_dark",

        height=600,

        yaxis=dict(

            autorange="reversed"

        )

    )



    st.plotly_chart(

        fig5,

        use_container_width=True

    )



    st.subheader(

        "📋 Dados completos"

    )


    st.dataframe(

        ranking,

        use_container_width=True,

        hide_index=True

    )



# ============================================================
# FIM DA PARTE 3
# ============================================================
# ============================================================
# OLHEIRO
# ============================================================


elif pagina == "👀 Olheiro":


    st.markdown(

    """

    <div class="banner">


    <h1>

    👀 Central do Olheiro

    </h1>


    <p>

    Identificação de talentos,
    análise de potencial e indicação
    de jogadores para observação.

    </p>


    </div>


    """,

    unsafe_allow_html=True

    )


    st.write("")



    # ========================================================
    # FILTROS DE OBSERVAÇÃO
    # ========================================================


    filtro1,filtro2,filtro3 = st.columns(3)



    with filtro1:


        idade_max = st.slider(

            "🎂 Idade máxima",

            17,

            36,

            23

        )



    with filtro2:


        potencial_min = st.slider(

            "⭐ Potencial mínimo",

            65,

            99,

            80

        )



    with filtro3:


        valor_max = st.slider(

            "💰 Valor máximo (milhões R$)",

            1.0,

            100.0,

            50.0

        )



    jogadores_observados = df[

        (df["Idade"] <= idade_max)

        &

        (df["Potencial"] >= potencial_min)

        &

        (df["Valor de Mercado"] <= valor_max)

    ]



    st.divider()



    # ========================================================
    # INDICADORES DO OLHEIRO
    # ========================================================


    a,b,c,d = st.columns(4)



    with a:

        criar_card(

            "🔎 Encontrados",

            len(jogadores_observados)

        )


    with b:

        criar_card(

            "⭐ Potencial médio",

            round(

                jogadores_observados["Potencial"]

                .mean(),

                1

            )

            if len(jogadores_observados)>0

            else 0

        )


    with c:

        criar_card(

            "⚽ Gols",

            int(

                jogadores_observados["Gols"]

                .sum()

            )

            if len(jogadores_observados)>0

            else 0

        )


    with d:

        criar_card(

            "💰 Valor médio",

            round(

                jogadores_observados["Valor de Mercado"]

                .mean(),

                1

            )

            if len(jogadores_observados)>0

            else 0

        )



    st.write("")



    # ========================================================
    # RECOMENDAÇÃO AUTOMÁTICA
    # ========================================================


    st.subheader(

        "🎯 Recomendações de contratação"

    )



    if len(jogadores_observados) > 0:



        recomendados = (

            jogadores_observados

            .sort_values(

                [

                "Potencial",

                "Índice de Desempenho"

                ],

                ascending=False

            )

            .head(10)

        )



        st.success(

            f"{len(recomendados)} jogadores recomendados para análise."

        )



        st.dataframe(

            recomendados[

            [

            "Jogador",

            "Idade",

            "Posição",

            "Clube",

            "Potencial",

            "Nota",

            "Índice de Desempenho",

            "Valor de Mercado"

            ]

            ],

            use_container_width=True,

            hide_index=True

        )



    else:


        st.warning(

            "Nenhum jogador encontrado com esses critérios."

        )



    st.write("")



    # ========================================================
    # ANÁLISE POR POSIÇÃO
    # ========================================================


    st.subheader(

        "📊 Distribuição dos talentos encontrados"

    )



    if len(jogadores_observados)>0:



        posicao_talentos=(

            jogadores_observados

            .groupby(

                "Posição"

            )

            .size()

            .reset_index(

                name="Quantidade"

            )

        )



        fig = px.bar(

            posicao_talentos,

            x="Posição",

            y="Quantidade",

            color="Posição",

            title="Talentos por posição"

        )



        fig.update_layout(

            template="plotly_dark",

            height=400

        )



        st.plotly_chart(

            fig,

            use_container_width=True

        )



    st.divider()



    # ========================================================
    # RELATÓRIO DO OLHEIRO
    # ========================================================


    st.subheader(

        "📝 Relatório de observação"

    )



    if len(jogadores_observados)>0:


        escolhido = st.selectbox(

            "Selecione um atleta",

            jogadores_observados["Jogador"]

        )



        atleta = jogadores_observados[

            jogadores_observados["Jogador"]

            ==

            escolhido

        ].iloc[0]



        st.markdown(

        f"""

        <div class="card">


        <h2>

        Relatório: {atleta['Jogador']}

        </h2>


        <p>


        🏟️ Clube:
        {atleta['Clube']}


        <br><br>


        ⚽ Posição:
        {atleta['Posição']}


        <br><br>


        🎂 Idade:
        {atleta['Idade']} anos


        <br><br>


        ⭐ Potencial:
        {atleta['Potencial']}/99


        <br><br>


        📈 Índice:
        {atleta['Índice de Desempenho']}


        <br><br>


        💰 Valor estimado:
        R$ {atleta['Valor de Mercado']} milhões


        </p>


        <hr>


        <b>Recomendação:</b>


        Atleta apresenta características
        compatíveis para acompanhamento
        da comissão técnica.


        </div>


        """,

        unsafe_allow_html=True

        )



# ============================================================
# FIM DA PARTE 4
# ============================================================
# ============================================================
# ANALISTA DE DADOS
# ============================================================


elif pagina == "🧠 Analista de Dados":


    st.markdown(

    """

    <div class="banner">


    <h1>

    🧠 Central do Analista de Dados

    </h1>


    <p>

    Transformando números em decisões
    estratégicas para o clube.

    </p>


    </div>


    """,

    unsafe_allow_html=True

    )



    st.write("")



    # ========================================================
    # SELEÇÃO DE JOGADORES
    # ========================================================


    st.subheader(

        "🔍 Comparação entre atletas"

    )



    jogadores_lista = sorted(

        df["Jogador"]

        .unique()

        .tolist()

    )



    jogador1,jogador2 = st.columns(2)



    with jogador1:


        atleta1 = st.selectbox(

            "Primeiro jogador",

            jogadores_lista,

            key="jogador_1"

        )



    with jogador2:


        atleta2 = st.selectbox(

            "Segundo jogador",

            jogadores_lista,

            index=1,

            key="jogador_2"

        )



    dados1 = df[

        df["Jogador"]

        ==

        atleta1

    ].iloc[0]



    dados2 = df[

        df["Jogador"]

        ==

        atleta2

    ].iloc[0]



    st.divider()



    # ========================================================
    # COMPARAÇÃO
    # ========================================================


    comparacao = pd.DataFrame(

    {

        "Indicador":

        [

        "Nota",

        "Gols",

        "Assistências",

        "Precisão de Passe",

        "Desarmes",

        "Km Percorridos",

        "Velocidade",

        "Índice"

        ],


        atleta1:

        [

        dados1["Nota"],

        dados1["Gols"],

        dados1["Assistências"],

        dados1["Precisão de Passe"],

        dados1["Desarmes"],

        dados1["Km Percorridos"],

        dados1["Velocidade Máxima"],

        dados1["Índice de Desempenho"]

        ],


        atleta2:

        [

        dados2["Nota"],

        dados2["Gols"],

        dados2["Assistências"],

        dados2["Precisão de Passe"],

        dados2["Desarmes"],

        dados2["Km Percorridos"],

        dados2["Velocidade Máxima"],

        dados2["Índice de Desempenho"]

        ]

    }

    )



    st.dataframe(

        comparacao,

        use_container_width=True,

        hide_index=True

    )



    # ========================================================
    # GRÁFICO RADAR
    # ========================================================


    st.subheader(

        "📈 Perfil dos jogadores"

    )



    categorias=[

        "Nota",

        "Gols",

        "Assistências",

        "Precisão de Passe",

        "Desarmes",

        "Velocidade Máxima"

    ]



    fig = go.Figure()



    fig.add_trace(

        go.Scatterpolar(

            r=[

            dados1[c]

            for c in categorias

            ],

            theta=categorias,

            fill="toself",

            name=atleta1

        )

    )



    fig.add_trace(

        go.Scatterpolar(

            r=[

            dados2[c]

            for c in categorias

            ],

            theta=categorias,

            fill="toself",

            name=atleta2

        )

    )



    fig.update_layout(

        template="plotly_dark",

        polar=dict(

            bgcolor="rgba(0,0,0,0)"

        ),

        height=500

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    # ========================================================
    # ANÁLISE AUTOMÁTICA
    # ========================================================


    st.subheader(

        "🤖 Análise automática"

    )



    melhor = None



    if dados1["Índice de Desempenho"] > dados2["Índice de Desempenho"]:

        melhor = atleta1

        diferenca = (

            dados1["Índice de Desempenho"]

            -

            dados2["Índice de Desempenho"]

        )


    else:

        melhor = atleta2

        diferenca = (

            dados2["Índice de Desempenho"]

            -

            dados1["Índice de Desempenho"]

        )



    st.success(

        f"""

        O jogador com maior índice de desempenho
        atualmente é {melhor}.


        Diferença estimada:

        {round(diferenca,1)} pontos.

        """

    )



    # ========================================================
    # PONTOS FORTES E FRACOS
    # ========================================================


    st.subheader(

        "📋 Relatório técnico"

    )



    escolhido_nome = st.selectbox(

        "Escolha um jogador para relatório",

        jogadores_lista,

        key="relatorio"

    )



    jogador = df[

        df["Jogador"]

        ==

        escolhido_nome

    ].iloc[0]



    pontos=[]

    melhorias=[]



    if jogador["Nota"] >= 8:

        pontos.append(

            "Excelente avaliação média"

        )

    else:

        melhorias.append(

            "Melhorar consistência técnica"

        )



    if jogador["Precisão de Passe"] >= 85:

        pontos.append(

            "Boa qualidade de passe"

        )

    else:

        melhorias.append(

            "Aumentar precisão dos passes"

        )



    if jogador["Velocidade Máxima"] >= 34:

        pontos.append(

            "Boa capacidade física"

        )

    else:

        melhorias.append(

            "Evoluir velocidade e explosão"

        )



    if jogador["Risco de Lesão"]=="Alto":

        melhorias.append(

            "Necessita controle de carga física"

        )



    st.markdown(

    f"""

    <div class="card">


    <h2>

    Relatório: {jogador['Jogador']}

    </h2>


    <b>Pontos fortes:</b>


    <ul>

    {"".join(

    f"<li>{p}</li>"

    for p in pontos

    )}

    </ul>



    <b>Pontos para evolução:</b>


    <ul>

    {"".join(

    f"<li>{m}</li>"

    for m in melhorias

    )}

    </ul>



    </div>


    """,

    unsafe_allow_html=True

    )



# ============================================================
# FIM DA PARTE 5
# ============================================================
# ============================================================
# MAPA DE CALOR
# ============================================================


elif pagina == "🔥 Mapa de Calor":


    st.markdown(

    """

    <div class="banner">


    <h1>

    🔥 Mapa de Calor

    </h1>


    <p>

    Visualização da movimentação do atleta
    durante uma partida.

    </p>


    </div>


    """,

    unsafe_allow_html=True

    )



    st.write("")



    # ========================================================
    # GERADOR DE POSIÇÕES FICTÍCIAS
    # ========================================================


    def gerar_movimentacao(posicao):


        quantidade = 250



        if posicao == "Goleiro":

            x = np.random.normal(

                10,

                8,

                quantidade

            )

            y = np.random.normal(

                34,

                12,

                quantidade

            )


        elif posicao in [

            "Zagueiro",

            "Lateral"

        ]:


            x = np.random.normal(

                35,

                18,

                quantidade

            )

            y = np.random.normal(

                34,

                20,

                quantidade

            )


        elif posicao in [

            "Volante",

            "Meia"

        ]:


            x = np.random.normal(

                55,

                20,

                quantidade

            )

            y = np.random.normal(

                34,

                22,

                quantidade

            )


        else:


            x = np.random.normal(

                75,

                18,

                quantidade

            )

            y = np.random.normal(

                34,

                22,

                quantidade

            )



        x=np.clip(

            x,

            0,

            100

        )


        y=np.clip(

            y,

            0,

            68

        )



        return x,y



    # ========================================================
    # SELEÇÃO DO ATLETA
    # ========================================================



    jogador_nome = st.selectbox(

        "⚽ Escolha o jogador",

        sorted(

            df["Jogador"]

            .tolist()

        )

    )



    jogador = df[

        df["Jogador"]

        ==

        jogador_nome

    ].iloc[0]



    x,y = gerar_movimentacao(

        jogador["Posição"]

    )



    # ========================================================
    # CAMPO DE FUTEBOL
    # ========================================================



    fig = go.Figure()



    # linhas do campo


    linhas = [

        ([0,100],[0,0]),

        ([0,100],[68,68]),

        ([0,0],[0,68]),

        ([100,100],[0,68]),

        ([50,50],[0,68])

    ]



    for linha in linhas:


        fig.add_trace(

            go.Scatter(

                x=linha[0],

                y=linha[1],

                mode="lines",

                line=dict(

                    width=3,

                    color="white"

                ),

                showlegend=False

            )

        )



    # mapa de calor


    fig.add_trace(

        go.Histogram2dContour(

            x=x,

            y=y,

            colorscale="Hot",

            showscale=False,

            contours=dict(

                coloring="heatmap"

            )

        )

    )



    # posição média


    fig.add_trace(

        go.Scatter(

            x=[

            np.mean(x)

            ],

            y=[

            np.mean(y)

            ],

            mode="markers",

            marker=dict(

                size=18,

                color="white"

            ),

            name="Posição média"

        )

    )



    fig.update_layout(

        title=

        f"🔥 Movimentação: {jogador_nome}",


        template="plotly_dark",


        height=600,


        xaxis=dict(

            range=[0,100],

            showgrid=False

        ),


        yaxis=dict(

            range=[0,68],

            showgrid=False

        )

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    # ========================================================
    # ANÁLISE DA MOVIMENTAÇÃO
    # ========================================================


    st.subheader(

        "📊 Análise da movimentação"

    )



    c1,c2,c3,c4 = st.columns(4)



    with c1:

        criar_card(

            "Posição",

            jogador["Posição"]

        )


    with c2:

        criar_card(

            "Distância",

            f"{jogador['Km Percorridos']} km"

        )


    with c3:

        criar_card(

            "Sprints",

            jogador["Sprints"]

        )


    with c4:

        criar_card(

            "Velocidade",

            f"{jogador['Velocidade Máxima']} km/h"

        )



    st.markdown(

    f"""

    <div class="card">


    <h3>

    📝 Interpretação do Analista

    </h3>


    O jogador <b>{jogador['Jogador']}</b>
    atua como <b>{jogador['Posição']}</b>.


    <br><br>


    A análise demonstra sua ocupação de espaço
    durante a partida, permitindo ao técnico
    avaliar posicionamento e comportamento tático.


    <br><br>


    O preparador físico pode utilizar esses dados
    para controlar intensidade de treino,
    distância percorrida e carga física.


    </div>


    """,

    unsafe_allow_html=True

    )



# ============================================================
# FIM DA PARTE 6
# ============================================================
# ============================================================
# TÉCNICO
# ============================================================


elif pagina == "👨‍🏫 Técnico":


    st.markdown(

    """

    <div class="banner">


    <h1>

    👨‍🏫 Central do Técnico

    </h1>


    <p>

    Auxílio na tomada de decisões,
    escalação e análise de desempenho coletivo.

    </p>


    </div>


    """,

    unsafe_allow_html=True

    )



    st.write("")



    # ========================================================
    # ESCOLHA DO ESQUEMA
    # ========================================================


    esquema = st.selectbox(

        "📋 Escolha a estratégia",

        [

            "4-3-3 Ofensivo",

            "4-4-2 Equilibrado",

            "3-5-2 Posse de bola",

            "4-2-3-1 Controle"

        ]

    )



    st.success(

        f"Estratégia selecionada: {esquema}"

    )



    st.divider()



    # ========================================================
    # MELHORES JOGADORES POR POSIÇÃO
    # ========================================================


    st.subheader(

        "⭐ Sugestão de escalação baseada em dados"

    )



    escalação=[]



    for pos in posicoes:


        jogador_pos = df[

            df["Posição"]

            ==

            pos

        ]



        if len(jogador_pos)>0:


            melhor = jogador_pos.sort_values(

                "Índice de Desempenho",

                ascending=False

            ).iloc[0]



            escalação.append(

                {

                "Posição":pos,

                "Jogador":melhor["Jogador"],

                "Nota":melhor["Nota"],

                "Índice":melhor["Índice de Desempenho"]

                }

            )



    escala_df=pd.DataFrame(

        escalação

    )



    st.dataframe(

        escala_df,

        use_container_width=True,

        hide_index=True

    )



    st.divider()



    # ========================================================
    # ANÁLISE COLETIVA
    # ========================================================


    st.subheader(

        "📈 Visão coletiva do elenco"

    )



    c1,c2,c3 = st.columns(3)



    with c1:


        criar_card(

            "⭐ Média técnica",

            round(

                df["Nota"].mean(),

                2

            )

        )



    with c2:


        criar_card(

            "⚽ Média gols/jogo",

            round(

                df["Gols"].mean(),

                2

            )

        )



    with c3:


        criar_card(

            "🏃 Intensidade média",

            round(

                df["Km Percorridos"]

                .mean(),

                1

            )

        )



    st.markdown(

    """

    <div class="card">


    <h3>

    💡 Decisão do Técnico

    </h3>


    Os dados auxiliam o treinador a escolher
    atletas com melhor desempenho,
    identificar necessidades da equipe
    e ajustar estratégias.


    </div>


    """,

    unsafe_allow_html=True

    )




# ============================================================
# PREPARADOR FÍSICO
# ============================================================


elif pagina == "🏃 Preparador Físico":



    st.markdown(

    """

    <div class="banner">


    <h1>

    🏃 Central do Preparador Físico

    </h1>


    <p>

    Controle de carga,
    fadiga e prevenção de lesões.

    </p>


    </div>


    """,

    unsafe_allow_html=True

    )



    st.write("")



    # ========================================================
    # INDICADORES FÍSICOS
    # ========================================================


    a,b,c,d = st.columns(4)



    with a:

        criar_card(

            "🏃 Km médio",

            round(

                df["Km Percorridos"]

                .mean(),

                1

            )

        )



    with b:

        criar_card(

            "🔥 Sprints médios",

            round(

                df["Sprints"]

                .mean(),

                1

            )

        )



    with c:

        criar_card(

            "⚡ Velocidade",

            round(

                df["Velocidade Máxima"]

                .mean(),

                1

            )

        )



    with d:

        criar_card(

            "🩺 Alto risco",

            len(

                df[

                df["Risco de Lesão"]

                =="Alto"

                ]

            )

        )



    st.divider()



    # ========================================================
    # MONITORAMENTO DE ATLETAS
    # ========================================================


    st.subheader(

        "🚨 Atletas que precisam de atenção"

    )



    risco_alto = df[

        df["Risco de Lesão"]

        ==

        "Alto"

    ].sort_values(

        "Fadiga",

        ascending=False

    )



    st.dataframe(

        risco_alto[

        [

        "Jogador",

        "Posição",

        "Fadiga",

        "Risco de Lesão",

        "Km Percorridos",

        "Sprints"

        ]

        ],

        use_container_width=True,

        hide_index=True

    )



    # ========================================================
    # GRÁFICO DE CARGA
    # ========================================================


    carga = df.sort_values(

        "Fadiga",

        ascending=False

    ).head(15)



    fig = px.bar(

        carga,

        x="Jogador",

        y="Fadiga",

        color="Risco de Lesão",

        title="🔥 Índice de fadiga dos atletas"

    )



    fig.update_layout(

        template="plotly_dark",

        height=450

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.markdown(

    """

    <div class="card">


    <h3>

    📝 Recomendação física

    </h3>


    Jogadores com alta fadiga devem
    receber controle de carga,
    recuperação adequada e acompanhamento
    da comissão técnica.


    </div>


    """,

    unsafe_allow_html=True

    )



# ============================================================
# FIM DA PARTE 7
# ============================================================
# ============================================================
# JOGADOR
# ============================================================


elif pagina == "⚽ Jogador":


    st.markdown(

    """

    <div class="banner">


    <h1>

    ⚽ Área do Jogador

    </h1>


    <p>

    O atleta acompanha seus próprios
    indicadores e identifica pontos
    para evolução.

    </p>


    </div>


    """,

    unsafe_allow_html=True

    )



    st.write("")



    jogador_escolhido = st.selectbox(

        "Selecione o atleta",

        sorted(

            df["Jogador"]

            .tolist()

        )

    )



    atleta = df[

        df["Jogador"]

        ==

        jogador_escolhido

    ].iloc[0]



    st.divider()



    c1,c2,c3,c4 = st.columns(4)



    with c1:

        criar_card(

            "⭐ Nota",

            atleta["Nota"]

        )



    with c2:

        criar_card(

            "⚽ Gols",

            atleta["Gols"]

        )



    with c3:

        criar_card(

            "🎯 Assistências",

            atleta["Assistências"]

        )



    with c4:

        criar_card(

            "📈 Índice",

            atleta["Índice de Desempenho"]

        )



    st.write("")



    col1,col2 = st.columns(2)



    with col1:



        desempenho = pd.DataFrame(

        {

            "Métrica":

            [

            "Nota",

            "Precisão Passe",

            "Velocidade",

            "Potencial",

            "Desarmes"

            ],


            "Valor":

            [

            atleta["Nota"]*10,

            atleta["Precisão de Passe"],

            atleta["Velocidade Máxima"]*3,

            atleta["Potencial"],

            atleta["Desarmes"]

            ]

        }

        )



        fig = px.bar(

            desempenho,

            x="Métrica",

            y="Valor",

            color="Métrica",

            title="📊 Perfil técnico"

        )



        fig.update_layout(

            template="plotly_dark",

            height=400

        )



        st.plotly_chart(

            fig,

            use_container_width=True

        )



    with col2:



        st.markdown(

        f"""

        <div class="card">


        <h2>

        Relatório individual

        </h2>


        <p>


        👤 Jogador:

        {atleta['Jogador']}


        <br><br>


        🏟️ Clube:

        {atleta['Clube']}


        <br><br>


        ⚽ Posição:

        {atleta['Posição']}


        <br><br>


        🎂 Idade:

        {atleta['Idade']} anos


        <br><br>


        📏 Altura:

        {atleta['Altura']} cm


        <br><br>


        🏃 Distância:

        {atleta['Km Percorridos']} km


        <br><br>


        🩺 Risco:

        {atleta['Risco de Lesão']}


        </p>


        </div>


        """,

        unsafe_allow_html=True

        )



    st.divider()



    st.subheader(

        "💡 Sugestão de evolução"

    )



    if atleta["Nota"] >= 8:


        st.success(

            "Atleta apresenta ótimo desempenho técnico."

        )


    else:


        st.warning(

            "Atleta deve buscar evolução técnica."

        )



    if atleta["Risco de Lesão"]=="Alto":


        st.error(

            "Necessário controle de carga física."

        )



# ============================================================
# INTEGRANTES
# ============================================================


elif pagina == "👥 Integrantes":



    st.markdown(

    """

    <div class="banner">


    <h1>

    👥 Equipe FutDados

    </h1>


    <p>

    Profissões envolvidas no projeto.

    </p>


    </div>


    """,

    unsafe_allow_html=True

    )



    st.write("")



    integrantes = [

        (

        "📊",

        "Pedro Alejandro",

        "Analista de Dados",

        "Recebe dados, cria análises e transforma informações em decisões."

        ),


        (

        "👀",

        "Bruno",

        "Olheiro",

        "Busca talentos e identifica jogadores com potencial."

        ),


        (

        "⚽",

        "Leonardo",

        "Jogador",

        "Executa o desempenho dentro de campo."

        ),


        (

        "👨‍🏫",

        "Luis Fernando",

        "Técnico",

        "Utiliza dados para montar estratégias."

        ),


        (

        "🏃",

        "Nicolas",

        "Preparador Físico",

        "Controla carga, desempenho e prevenção de lesões."

        )

    ]



    colunas = st.columns(5)



    for coluna,item in zip(

        colunas,

        integrantes

    ):



        with coluna:



            st.markdown(

            f"""

            <div class="card"

            style="text-align:center">


            <h1>

            {item[0]}

            </h1>


            <h3>

            {item[1]}

            </h3>


            <b>

            {item[2]}

            </b>


            <p>

            {item[3]}

            </p>


            </div>


            """,

            unsafe_allow_html=True

            )



# ============================================================
# RODAPÉ
# ============================================================


st.markdown(

"""

<div class="footer">


⚽ FutDados © 2026

<br>

Projeto acadêmico utilizando
análise de dados aplicada ao futebol.


<br><br>

Todos os dados utilizados são fictícios.


</div>


""",

unsafe_allow_html=True

)



