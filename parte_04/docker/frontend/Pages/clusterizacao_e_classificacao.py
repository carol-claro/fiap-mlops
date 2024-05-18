import streamlit as st
import requests
import json

def dados_clustering(body):
    with open('/myServer/config/microservices.json') as json_file:
        microservices_config = json.load(json_file)

    url = f'{microservices_config["model_manager"]["endpoint"]}/predict?model=customer_clustering'
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, data=json.dumps(body), headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro na requisição: {e}, {json.dumps(body)}")
        return None

def mostrar_emoji(emoji: str):
    """Mostra um emoji como um ícone de página no estilo Notion."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

def avaliacao_credito():
    mostrar_emoji("📊")  # Alterando o emoji para um gráfico
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Avaliação de Crédito')
    with st.form("detalhes_emprestimo"):
        loan_purpose = st.selectbox('Finalidade do Empréstimo', options=['p1', 'p4', 'p3', 'p2'])
        security_type = st.selectbox('Tipo de Segurança', options=['Direto', 'Indireto'])
        age = st.selectbox('Faixa Etária do Solicitante', options=['55-64', '45-54', '35-44', '>74', '25-34', '65-74', '<25'])
        region = st.selectbox('Região', options=['Norte', 'Centro', 'Sul', 'Nordeste'])

        year = st.number_input('Ano', min_value=2010, max_value=2030, value=2024)
        loan_amount = st.number_input('Valor do Empréstimo', min_value=0.0, max_value=3576500.0)
        term = st.number_input('Prazo (em meses)', min_value=1, max_value=360)
        property_value = st.number_input('Valor do Imóvel', min_value=8000.0, max_value=16508000.0)
        income = st.number_input('Renda do Solicitante', min_value=0.0, max_value=578580.0)
        credit_score = st.number_input('Pontuação de Crédito', min_value=0.0, max_value=1000.0)
        ltv = st.number_input('LTV (Taxa de Empréstimo-Valor)', min_value=0, max_value=10000)
        dtir1 = st.number_input('DTIR1 (Razão Dívida-Renda)', min_value=0.0, max_value=100.0)

        submitted = st.form_submit_button("Enviar")
        if submitted:
            body = {
                'loan_purpose': f"{loan_purpose}",
                'Security_Type': f"{security_type}",
                'age': f"{age}",
                'Region': f"{region}",
                'year': int(year),
                'loan_amount': int(loan_amount),
                'term': float(term),
                'property_value': float(property_value),
                'income': float(income),
                'Credit_Score': int(credit_score),
                'LTV': float(ltv),
                'dtir1': float(dtir1)
            }

            retorno = dados_clustering(body)
            if retorno is not None:
                st.write(retorno)
