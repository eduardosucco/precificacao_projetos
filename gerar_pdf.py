from weasyprint import HTML
from datetime import datetime

def gerar_pdf(nome_cliente, valor_final, parametros, descricao, observacoes, desconto):
    # Data Atual
    data_atual = datetime.now().strftime("%d/%m/%Y")

    # Gerar conteúdo HTML para o PDF
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                color: #333;
                margin: 20px;
            }}
            h1 {{
                text-align: center;
                color: #4CAF50;
            }}
            h2 {{
                color: #333;
            }}
            .section-title {{
                font-weight: bold;
                margin-top: 20px;
                margin-bottom: 10px;
            }}
            .content {{
                margin-left: 20px;
            }}
            .footer {{
                text-align: center;
                font-size: 10px;
                margin-top: 30px;
                color: #888;
            }}
            .highlight {{
                font-weight: bold;
                color: #4CAF50;
            }}
            .table {{
                width: 100%;
                border-collapse: collapse;
            }}
            .table td, .table th {{
                padding: 8px;
                border: 1px solid #ddd;
            }}
            .table th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>NOTA FISCAL DE SERVIÇO</h1>
        <p><strong>Cliente:</strong> {nome_cliente}</p>
        <p><strong>Data:</strong> {data_atual}</p>

        <div class="section-title">Detalhes do Projeto:</div>
        <table class="table">
            <tr><th>Parâmetro</th><th>Valor</th></tr>
    """

    # Adicionar os parâmetros na tabela
    for chave, valor in parametros.items():
        html_content += f"<tr><td>{chave.capitalize()}</td><td>{valor}</td></tr>"

    html_content += f"""
        </table>

        <div class="section-title">Descrição do Serviço:</div>
        <p class="content">{descricao}</p>

        <div class="section-title">Observações:</div>
        <p class="content">{observacoes}</p>

        <div class="section-title">Cálculos:</div>
        <p><strong>Subtotal:</strong> R$ {valor_final:,.2f}</p>
        <p><strong>Impostos (10%):</strong> R$ {valor_final * 0.10:,.2f}</p>
        <p><strong>Total com Impostos:</strong> R$ {valor_final * 1.10:,.2f}</p>

        <p><strong>Desconto Aplicado:</strong> {desconto}%</p>
        <p class="highlight"><strong>Valor Final com Desconto:</strong> R$ {valor_final - (valor_final * desconto / 100):,.2f}</p>

        <div class="footer">
            <p>Serviço prestado conforme contrato. Todos os impostos são de responsabilidade do prestador.</p>
        </div>
    </body>
    </html>
    """

    # Gerar o PDF a partir do HTML
    pdf_filename = "nota_fiscal_servico.pdf"
    HTML(string=html_content).write_pdf(pdf_filename)
    return pdf_filename
