from fpdf import FPDF

path_file = 'C:/Users/joreu.konrad/Documents/VS Code Workplaces/Starting My Journey/Starting_my_Journey/Youtube_Channels/Chart Explorers/'

class PDF(FPDF):
   def header(self):
      # logo
      self.image('C:/Users/joreu.konrad/Documents/VS Code Workplaces/Starting My Journey/Starting_my_Journey/Youtube_Channels/Chart Explorers/logotest.png',10,8,25)
      self.set_font('helvetica','B',20)
      self.cell(0,10,'Title',border=0,ln=1,align='C')
      self.ln(20)
   
   def footer(self):
      self.set_y(-15)
      self.set_font('helvetica','I',10)
      self.cell(0,10,f'Page{self.page_no()}/{{nb}}',align='C')

def trunca_texto(texto, largura_max):
    # Se o texto for mais longo que a largura máxima, trunca e adiciona "..."
    if pdf.get_string_width(texto) > largura_max:
        while pdf.get_string_width(texto + '...') > largura_max:
            texto = texto[:-1]
        return texto + '...'
    else:
        return texto


pdf = PDF('P','mm','Letter')

pdf.alias_nb_pages()

pdf.set_auto_page_break(auto=1,margin=12)

pdf.add_page()

pdf.set_font('helvetica','',12)


for i in range(1,400):
   if i % 2 == 0:
      pdf.cell(20,15,f'Estoque: {i-1} 5000',ln=1)
   else:
      pdf.cell(10,10,f'Produto: {i} Bagulho',ln=1)

'''
texto = "Este é um exemplo de texto longo que precisa ser ajustado para caber na célula."
texto_truncado = trunca_texto(texto, 50)

for i in range(1,400):
   pdf.cell(10,10,texto_truncado,ln=1)
'''

pdf.output(path_file+'pdfTeste3.pdf')




