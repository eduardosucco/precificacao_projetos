import streamlit as st
from fpdf import FPDF

# Funções de cálculo
def calcular_valor(estimativa_horas, desconto, parametros):
    # Base inicial: valor por hora (ajustável)
    valor_por_hora = 200  
    valor_base = estimativa_horas * valor_por_hora

    # Ajustes no valor base de acordo com os parâmetros
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

    # Aplicar desconto
    desconto_valor = valor_base * (desconto / 100)
    valor_final = valor_base - desconto_valor

    return valor_final

# Função para gerar o PDF
def gerar_pdf(nome_cliente, valor_final, parametros):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Cabeçalho
    pdf.cell(200, 10, txt="Proposta de Projeto", ln=True, align='C')
    pdf.ln(10)

    # Informações do cliente e valor
    pdf.cell(200, 10, txt=f"Cliente: {nome_cliente}", ln=True)
    pdf.cell(200, 10, txt=f"Valor Final: R$ {valor_final:.2f}", ln=True)
    pdf.ln(10)

    # Detalhes do projeto
    pdf.cell(200, 10, txt="Detalhes do Projeto:", ln=True)
    for chave, valor in parametros.items():
        pdf.cell(200, 10, txt=f"{chave.capitalize()}: {valor}", ln=True)

    # Salvar o PDF
    pdf_filename = "proposta_projeto.pdf"
    pdf.output(pdf_filename)
    return pdf_filename

# Função principal da aplicação
def main():
    st.title("Precificação de Projetos - WGG Digital Solutions")

    # Entrada de dados do cliente
    nome_cliente = st.text_input("Nome do Cliente")
    estimativa_horas = st.number_input("Estimativa de Horas", min_value=1, value=300)
    desconto = st.slider("Aplicar Desconto (%)", min_value=0, max_value=15, value=0)

    # Parâmetros do projeto
    parametros = {
        "escopo": st.selectbox("Escopo do Projeto", 
                               ["Sem escopo definido", "Apenas com diretrizes gerais",
                                "Informações suficientes para iniciar o trabalho",
                                "Escopo detalhado e documentado"]),
        "maturidade_cliente": st.selectbox("Maturidade do Cliente com Tecnologia e Dados", 
                                           ["Baixa", "Média", "Alta"]),
        "tecnologia": st.selectbox("Tecnologias para Desenvolvimento", 
                                   ["Low Code", "Hard Code", "Misto"]),
        "prazo_entrega": st.selectbox("Prazo de Entrega (Dias)", 
                                      ["< 45 dias", "45 - 60 dias", "61 - 90 dias", "> 90 dias"]),
        "complexidade": st.selectbox("Complexidade do Projeto", ["Baixa", "Média", "Alta"]),
    }

    # Calcular valor final
    if st.button("Calcular Valor"):
        valor_final = calcular_valor(estimativa_horas, desconto, parametros)
        st.write(f"**Valor Final do Projeto: R$ {valor_final:.2f}**")

        # Gerar PDF
        pdf_path = gerar_pdf(nome_cliente, valor_final, parametros)
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="Baixar Proposta em PDF",
                data=pdf_file,
                file_name="proposta_projeto.pdf",
                mime="application/pdf",
            )

if __name__ == "__main__":
    main()
