import streamlit as st

def mostrar_emoji(emoji: str):
    """Mostra um emoji como um ícone de página no estilo Notion."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

def inicio():

    mostrar_emoji("🏦")
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Bem-vindo à QuantumFinance - Transformando Seu Futuro Financeiro!')

    st.markdown('Na **QuantumFinance**, estamos redefinindo o cenário financeiro com **inovação**, **transparência** e **compromisso**. Somos uma **Fintech emergente**, determinada a oferecer **soluções financeiras inteligentes e acessíveis para todos**. Ao entrarmos no mercado, estamos prontos para **desafiar as normas, impulsionar a mudança e inspirar confiança**.\n\n')
    st.title('Por que escolher a QuantumFinance?\n')
    st.markdown('- **Inovação Pioneira**: Utilizamos tecnologia de ponta para desenvolver **soluções financeiras inovadoras** que se adaptam às suas necessidades em constante evolução.')
    st.markdown('- **Transparência Total**: Acreditamos na **transparência total em todas as interações**. Sem letras miúdas, sem surpresas desagradáveis - apenas uma **abordagem clara e honesta para o seu sucesso financeiro**.')
    st.markdown('- **Acessibilidade Universal**: Queremos **democratizar o acesso a serviços financeiros de qualidade**. Nossas soluções são projetadas para serem acessíveis a todos, independentemente de seu histórico financeiro.')
    st.markdown('- **Compromisso com o Cliente**: Você não é apenas um número para nós. Estamos comprometidos em **construir relacionamentos sólidos com nossos clientes**, oferecendo **suporte personalizado em cada passo do caminho**.\n\n')
    st.title('Nossos Serviços:\n')
    st.markdown('- **Previsão de Inadimplência**: Utilizando **algoritmos avançados**, oferecemos **previsões precisas para ajudá-lo a gerenciar riscos e tomar decisões informadas**.')
    st.markdown('- **Avaliação de Crédito Simplificada**: **Simplificamos o processo de avaliação de crédito**, tornando-o mais rápido e eficiente, permitindo que você **alcance seus objetivos financeiros**.')

    # Botão personalizado
    st.markdown(
        """
        <style>
        .myButton {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 10px;
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    if st.button('Clique aqui para começar'):
        # Ação ao clicar no botão
        st.write("Você clicou no botão!")
