import streamlit as st
from gerar_pdf import gerar_pdf  # Importando a função de geração de PDF
import streamlit.components.v1 as components

# Funções de cálculo (sem alterações)
def calcular_valor(estimativa_horas, desconto, parametros):
    valor_por_hora = 200
    valor_base = estimativa_horas * valor_por_hora
    ajustes = {
        "escopo": {"Sem escopo definido": 1.2, "Apenas com diretrizes gerais": 1.1,
                   "Informações suficientes para iniciar o trabalho": 1.05,
                   "Escopo detalhado e documentado": 1.0},
        "maturidade_cliente": {"Baixa": 1.2, "Média": 1.1, "Alta": 1.0},
        "tecnologia": {"Low Code": 1.0, "Hard Code": 1.2, "Misto": 1.1},
        "prazo_entrega": {"< 45 dias": 1.3, "45 - 60 dias": 1.1,
                          "61 - 90 dias": 1.0, "> 90 dias": 0.9},
        "complexidade": {"Baixa": 1.0, "Média": 1.2, "Alta": 1.5},
    }
    for chave, ajuste in ajustes.items():
        valor_base *= ajuste[parametros[chave]]
    desconto_valor = valor_base * (desconto / 100)
    valor_final = valor_base - desconto_valor
    return valor_final

# Função principal da aplicação
def main():
    nome_cliente = st.text_input("Nome do Cliente")
    st.title("Precificação de Projetos")

    # Entrada de dados do cliente
    estimativa_horas = st.number_input("Estimativa de Horas", min_value=1, value=300)

    # Parâmetros do projeto com Checkbox ou Radio Button
    parametros = {
        "escopo": st.radio("Escopo do Projeto", 
                           ["Sem escopo definido", "Apenas com diretrizes gerais",
                            "Informações suficientes para iniciar o trabalho",
                            "Escopo detalhado e documentado"]),
        "maturidade_cliente": st.radio("Maturidade do Cliente com Tecnologia e Dados", 
                                       ["Baixa", "Média", "Alta"]),
        "tecnologia": st.radio("Tecnologias para Desenvolvimento", 
                               ["Low Code", "Hard Code", "Misto"]),
        "prazo_entrega": st.radio("Prazo de Entrega (Dias)", 
                                  ["< 45 dias", "45 - 60 dias", "61 - 90 dias", "> 90 dias"]),
        "complexidade": st.radio("Complexidade do Projeto", ["Baixa", "Média", "Alta"]),
    }

    # Descrição e Observações do Serviço
    descricao_servico = st.text_area("Descrição do Serviço", height=150)
    observacoes = st.text_area("Observações e Comentários", height=150)

    # Calcular valor em tempo real
    valor_final = calcular_valor(estimativa_horas, 0, parametros)

    # Barra lateral com ícones e exibição dos parâmetros
    with st.sidebar:
        # Cabeçalho com Nome do Cliente e Valor Final
        st.markdown(f"## :bust_in_silhouette: **{nome_cliente}**")
        st.markdown(f"### :moneybag: **Valor Final:** R$ {valor_final:,.2f}")
        
        st.markdown("---")
        st.markdown("### Parâmetros Selecionados:")

        # Itens em Lista com ícones
        st.markdown(f"**:clipboard: Escopo:** {parametros['escopo']}")
        st.markdown(f"**:chart_with_upwards_trend: Maturidade do Cliente:** {parametros['maturidade_cliente']}")
        st.markdown(f"**:computer: Tecnologia:** {parametros['tecnologia']}")
        st.markdown(f"**:calendar: Prazo de Entrega:** {parametros['prazo_entrega']}")
        st.markdown(f"**:bar_chart: Complexidade:** {parametros['complexidade']}")
        
        st.markdown("---")
        st.markdown(f"### :memo: Descrição do Serviço\n{descricao_servico}")
        st.markdown(f"### :speech_balloon: Observações\n{observacoes}")

        # Slider para Aplicar Desconto no final
        desconto = st.slider("Aplicar Desconto (%)", min_value=0, max_value=15, value=0)

        # Recalcular valor com desconto
        valor_com_desconto = calcular_valor(estimativa_horas, desconto, parametros)

        st.markdown(f"### :money_with_wings: Desconto: {desconto}%")
        st.markdown(f"**Valor Final com Desconto: R$ {valor_com_desconto:,.2f}**")

        # Gerar PDF
        pdf_path = gerar_pdf(nome_cliente, valor_com_desconto, parametros, descricao_servico, observacoes, desconto)
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="Baixar Nota Fiscal em PDF",
                data=pdf_file,
                file_name="nota_fiscal_servico.pdf",
                mime="application/pdf",
            )

if __name__ == "__main__":
    main()
