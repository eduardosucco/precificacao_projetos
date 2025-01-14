from weasyprint import HTML
from jinja2 import Template
import os

# Função para gerar o PDF a partir do template HTML
def gerar_pdf(nome_cliente, valor_final, parametros, descricao_servico, observacoes, desconto):
    # Carregar o template HTML
    with open("invoice_template.html", "r") as file:
        html_template = file.read()

    # Dados para preenchimento no template
    data = {
        "from_address": "WeasyPrint\n26 rue Emile Decorps\n69100 Villeurbanne\nFrance",
        "to_address": f"{nome_cliente}\nEndereço do cliente\nCidade, País",
        "invoice_number": "12345",  # Aqui pode ser um número gerado ou sequencial
        "date": "2025-01-14",  # Data atual ou especificada
        "due_date": "2025-02-14",  # Prazo de pagamento
        "account_number": "132 456 789 012",
        "total_due": f"R$ {valor_final:.2f}",
        "items": [
            {"description": "Descrição do serviço", "price": "R$ 200,00", "quantity": 1, "subtotal": f"R$ {valor_final:.2f}"}
        ]
    }

    # Preencher o template HTML com os dados
    template = Template(html_template)
    html_output = template.render(data)

    # Gerar o PDF a partir do HTML
    pdf = HTML(string=html_output).write_pdf()

    # Salvar o PDF gerado
    pdf_filename = f"proposta_projeto_{nome_cliente}.pdf"
    with open(pdf_filename, "wb") as f:
        f.write(pdf)

    return pdf_filename
