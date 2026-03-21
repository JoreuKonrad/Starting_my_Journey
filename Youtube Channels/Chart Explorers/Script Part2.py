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

pdf = PDF('P','mm','Letter')

pdf.alias_nb_pages()

pdf.set_auto_page_break(auto=1,margin=12)

pdf.add_page()

pdf.set_font('helvetica','',16)


for i in range(2,400):
   pdf.cell(0,10,f'Line: {i} yeee',ln=1)



pdf.output(path_file+'pdfTeste2.pdf')