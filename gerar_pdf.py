from fpdf import FPDF

def gerar_pdf(nome_cliente, valor_final, parametros, descricao, observacoes, desconto):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Cabeçalho
    pdf.cell(200, 10, txt="NOTA FISCAL DE SERVIÇO", ln=True, align='C')
    pdf.ln(10)

    # Dados do Cliente
    pdf.cell(200, 10, txt=f"Cliente: {nome_cliente}", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Data: {pdf.get_date()}", ln=True)
    pdf.ln(10)

    # Tabela de Itens (Parâmetros do Projeto)
    pdf.cell(200, 10, txt="Detalhes do Projeto:", ln=True)
    for chave, valor in parametros.items():
        pdf.cell(200, 10, txt=f"{chave.capitalize()}: {valor}", ln=True)

    # Descrição do Serviço
    pdf.ln(10)
    pdf.cell(200, 10, txt="Descrição do Serviço:", ln=True)
    pdf.multi_cell(200, 10, txt=descricao)

    # Observações
    pdf.ln(10)
    pdf.cell(200, 10, txt="Observações:", ln=True)
    pdf.multi_cell(200, 10, txt=observacoes)

    # Calcular os impostos e mostrar total
    impostos = valor_final * 0.10  # Exemplo: 10% de imposto
    total_com_impostos = valor_final + impostos

    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Subtotal: R$ {valor_final:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Impostos (10%): R$ {impostos:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"**Total com Impostos: R$ {total_com_impostos:,.2f}**", ln=True)

    # Desconto aplicado
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Desconto Aplicado: {desconto}%", ln=True)
    desconto_valor = valor_final * (desconto / 100)
    valor_com_desconto = valor_final - desconto_valor
    pdf.cell(200, 10, txt=f"**Valor Final com Desconto: R$ {valor_com_desconto:,.2f}**", ln=True)

    # Rodapé com Informações Fiscais (exemplo)
    pdf.ln(20)
    pdf.set_font("Arial", "I", size=10)
    pdf.cell(200, 10, txt="Serviço prestado conforme contrato. Todos os impostos são de responsabilidade do prestador.", ln=True, align='C')

    # Salvar o PDF
    pdf_filename = "nota_fiscal_servico.pdf"
    pdf.output(pdf_filename)
    return pdf_filename
