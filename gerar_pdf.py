import pdfkit

def gerar_pdf(nome_cliente, valor_com_desconto, parametros, descricao_servico, observacoes, desconto):
    # Defina seu caminho para o HTML gerado aqui
    caminho_html = "caminho/para/seu/arquivo.html"
    
    # Gerar PDF a partir do HTML
    pdf_path = f"{nome_cliente}_proposta.pdf"
    pdfkit.from_file(caminho_html, pdf_path)
    return pdf_path
