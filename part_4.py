from fpdf import FPDF

title = "Lorem Ipsum"

class PDF(FPDF):
    def header(self):
        #font
        self.set_font('helvetica', 'B', 15)
        #calculate width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        #colors of frame, background, and text
        self.set_draw_color(0, 80, 180) #border = blue
        self.set_fill_color(230, 230, 0) #background - yellow
        self.set_text_color(220, 50, 50) #text = red
        #thickness of frame (border)
        self.set_line_width(1)
        #title
        self.cell(title_w, 10, title, border=1, ln=1, align='C', fill=1)
        #line break
        self.ln(20)

    def footer(self):
        #set position of the footer
        self.set_y(-15)
        #set font
        self.set_font('helvetica', 'I', 10)
        #set font color grey
        self.set_text_color(169, 169, 169)
        #page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    # Adding chapter title to start of each chapter
    def chapter_title(self, ch_num, ch_title, link):
        #set link location
        self.set_link(link)
        #set font
        self.set_font('helvetica', '', 12)
        #background color
        self.set_fill_color(200, 220, 255)
        #chapter title
        chapter_title = f'Chapter {ch_num} : {ch_title}'
        self.cell(0, 5, chapter_title, ln=1, fill=1)
        #line break
        self.ln()

    def chapter_body(self, name):
        #read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        #set font
        self.set_font('times', '', 12)
        #insert text
        self.multi_cell(0, 5, txt)
        #line break
        self.ln()
        # end each chapter
        self.set_font('times', 'I', 12)
        self.cell(0, 5, 'END OF CHAPTER')

    def print_chapter(self, ch_num, ch_title, name, link):
        self.add_page()
        self.chapter_title(ch_num, ch_title, link)
        self.chapter_body(name)

#create a PDF object
pdf = PDF('P', 'mm', 'Letter')

#metadata
pdf.set_title(title)
pdf.set_author('Mr Lopuz')

#links
website = "http://www.google.com"
ch1_link = pdf.add_link()
ch2_link = pdf.add_link()

#set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

#add page
pdf.add_page()
pdf.image('background_image.jpg', x = -0.5, w = pdf.w + 1)

#attach links
pdf.cell(0, 10, 'Text source', ln=1, link = website)
pdf.cell(0, 10, 'Chapter 1', ln=1, link = ch1_link)
pdf.cell(0, 10, 'Chapter 2', ln=1, link = ch2_link)

pdf.print_chapter(1, 'Definition and origin', 'chp1.txt', ch1_link)
pdf.print_chapter(2, 'Reason and place', 'chp2.txt', ch2_link)

pdf.output('pdf_4.pdf')
