import streamlit as st
import requests
import json

def dados_inadimplencia(body):
    with open('/myServer/config/microservices.json') as json_file:
        microservices_config = json.load(json_file)

    url = f'{microservices_config["model_manager"]["endpoint"]}/predict?model=default_propensity'
    headers = {'Content-Type': 'application/json'}
    try:
        resposta = requests.post(url, data=json.dumps(body), headers=headers)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro na requisição: {e}, {json.dumps(body)}")
        return None

def mostrar_emoji(emoji: str):
    """Mostra um emoji como um ícone de página no estilo Notion."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

def propensao_de_inadimplencia():
    mostrar_emoji("💳")  # Alteração do emoji aqui
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Propensão de Inadimplência')
    with st.form("formulario_aplicacao_emprestimo"):
        tipo_ocupacao = st.selectbox('Tipo de Ocupação', options=['pr', 'ir', 'sr'])
        tipo_credito_co_aplicante = st.selectbox('Tipo de Crédito do Co-Requerente', options=['EXP', 'CIB'])
        pontuacao_credito = st.number_input('Pontuação de Crédito', min_value=0.0, max_value=1000.0)
        ltv = st.number_input('LTV', min_value=0, max_value=10000)
        finalidade_emprestimo = st.selectbox('Finalidade do Empréstimo', options=['p1', 'p4', 'p3', 'p2'])
        dtir1 = st.number_input('DTIR1', min_value=0.0, max_value=100.0)
        valor_imovel = st.number_input('Valor do Imóvel', min_value=8000.0, max_value=16508000.0)
        envio_aplicacao = st.selectbox('Envio da Aplicação', options=['to_inst', 'not_inst'])
        aprovacao_antecipada = st.selectbox('Aprovação Antecipada', options=['nopre', 'pre'])
        renda = st.number_input('Renda', min_value=0.0, max_value=578580.0)
        
        enviado = st.form_submit_button("Executar")
        if enviado:
            body = {
                'occupancy_type': f"{tipo_ocupacao}",
                'co_applicant_credit_type': f"{tipo_credito_co_aplicante}",
                'Credit_Score': float(pontuacao_credito),
                'LTV': float(ltv),
                'loan_purpose': f"{finalidade_emprestimo}",
                'dtir1': float(dtir1),
                'property_value': float(valor_imovel),
                'submission_of_application': f"{envio_aplicacao}",
                'approv_in_adv': f"{aprovacao_antecipada}",
                'income': float(renda)
            }

            retorno = dados_inadimplencia(body)
            if retorno is not None:
                if retorno['prediction'] == 0:
                    st.write('Sem propensão a inadimplência')
                else:
                    st.write('Com propensão a inadimplência')
                
