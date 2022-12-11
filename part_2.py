from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        #logo
        self.image('github_test.png', 10, 8, 25)
        #font
        self.set_font('helvetica', 'B', 20)
        #padding
        self.cell(80)
        #title
        self.cell(30, 10, 'My_pdf', border=True, ln=1, align='C')
        #line break
        self.ln(20)

    def footer(self):
        #set position of the footer
        self.set_y(-15)
        #set font
        self.set_font('helvetica', 'I', 10)
        #page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

pdf = PDF('P', 'mm', 'Letter')

#get total page numbers
pdf.alias_nb_pages()

#set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

pdf.add_page()

pdf.set_font('helvetica', '', 16)

pdf.set_font('times', '', 12)

for i in range(1, 41):
    pdf.cell(0, 10, f'This is line {i} :D', ln=True)

pdf.output('pdf_2.pdf')
