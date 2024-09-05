import pandas as pd
from fpdf import FPDF
import os

dados = pd.read_csv("dados.csv")
dados.head()

# Dados do certificado
titulo = "CERTIFICADO DE PARTICIPAÇÃO"
subtitulo = "Este certificado comprova que"
texto2 = "Concluiu com êxito o curso GRATUITO DE PYTHON ministrado por"
texto3 = "PROF. HENRY TELES ARUCHE entre 15/06/2023 e 21/06/2023,"
texto4 = "com carga horária de aproximadamente 15 horas."

margem_cabecalho = 1.27  # em cm
margem_rodape = 1.27  # em cm
largura_pagina = 29.7  # cm
altura_pagina = 21  # cm

# Convertendo para mm
margem_cabecalho_mm = margem_cabecalho * 10
margem_rodape_mm = margem_rodape * 10
largura_pagina_mm = largura_pagina * 10
altura_pagina_mm = altura_pagina * 10

pasta_destino = 'Certificados'


# Função para centralizar o texto
def centralizar_texto(pdf, texto, y_mm, font_size=15):
    pdf.set_font("Arial", 'B', size=font_size)
    largura_texto = pdf.get_string_width(texto)
    x_mm = (largura_pagina_mm - largura_texto) / 2
    pdf.text(x_mm, y_mm, texto)

for nome in dados['nomecompleto']:

    pdf = FPDF(orientation='L', unit='mm', format='A4') 
    pdf.add_page()

    pdf.image("template.png", x=0, y=0, w=largura_pagina_mm)

    pdf.set_left_margin(margem_cabecalho_mm)
    pdf.set_right_margin(margem_rodape_mm)

    pdf.set_text_color(33, 24, 136)
    
    # Ajustar posições para o formato horizontal
    centralizar_texto(pdf, titulo, 50, 20)
    centralizar_texto(pdf, subtitulo, 70, 12)
    centralizar_texto(pdf, nome, 90, 15)
    centralizar_texto(pdf, texto2, 110, 12)
    centralizar_texto(pdf, texto3, 130, 12)
    centralizar_texto(pdf, texto4, 150, 12)

    # Salvando o PDF
    caminho_arquivo = os.path.join(pasta_destino, f"Certificado_{nome}.pdf")
    pdf.output(caminho_arquivo)
    
    print("Certificados gerados e salvos com sucesso na pasta:", pasta_destino)
