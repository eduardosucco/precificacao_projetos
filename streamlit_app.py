import streamlit as st
from gerar_pdf import gerar_pdf  # Importando a função de geração de PDF

def calcular_valor(estimativa_horas, desconto, parametros):
    # Defina aqui a lógica de cálculo do valor final do projeto
    # Este é um exemplo simples onde se assume que o valor por hora é R$ 100
    valor_por_hora = 100
    valor_base = estimativa_horas * valor_por_hora
    
    # Aplicando o desconto
    valor_com_desconto = valor_base * (1 - desconto / 100)
    
    # Aqui você pode adicionar mais lógica com base nos parâmetros do projeto
    # Por exemplo, se a complexidade for alta, pode aumentar o valor em 20%
    if parametros["complexidade"] == "Alta":
        valor_com_desconto *= 1.2
    elif parametros["complexidade"] == "Média":
        valor_com_desconto *= 1.1
    
    return valor_com_desconto

def main():
    st.title("Precificação de Projetos")

    # Entrada de dados do cliente
    nome_cliente = st.text_input("Nome do Cliente")
    estimativa_horas = st.number_input("Estimativa de Horas", min_value=1, value=300)
    desconto = st.slider("Aplicar Desconto (%)", min_value=0, max_value=15, value=0)

    # Parâmetros do projeto
    parametros = {
        "escopo": st.selectbox("Escopo do Projeto", ["Sem escopo definido", "Apenas com diretrizes gerais", "Informações suficientes para iniciar o trabalho", "Escopo detalhado e documentado"]),
        "maturidade_cliente": st.selectbox("Maturidade do Cliente", ["Baixa", "Média", "Alta"]),
        "tecnologia": st.selectbox("Tecnologias para Desenvolvimento", ["Low Code", "Hard Code", "Misto"]),
        "prazo_entrega": st.selectbox("Prazo de Entrega (Dias)", ["< 45 dias", "45 - 60 dias", "61 - 90 dias", "> 90 dias"]),
        "complexidade": st.selectbox("Complexidade do Projeto", ["Baixa", "Média", "Alta"]),
    }

    # Calcular valor final
    if st.button("Calcular Valor"):
        valor_final = calcular_valor(estimativa_horas, desconto, parametros)
        st.write(f"**Valor Final do Projeto: R$ {valor_final:.2f}**")

        # Gerar PDF
        pdf_path = gerar_pdf(nome_cliente, valor_final, parametros, "Descrição do serviço", "Observações", desconto)
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(label="Baixar Proposta em PDF", data=pdf_file, file_name=pdf_path)

if __name__ == "__main__":
    main()
