from fpdf import FPDF

caminho_pdf = 'C:/Users/joreu.konrad/Documents/VS Code Workplaces/Starting My Journey/Starting_my_Journey/Youtube_Channels/Chart Explorers/'

pdf = FPDF('P','mm','Letter')

pdf.add_page()


pdf.set_font('helvetica','',16)

pdf.cell(40,10,'Hello World',ln=True,border=True)
pdf.cell(80,10,'Bye World')

pdf.output(caminho_pdf+'pdfTeste.pdf')
