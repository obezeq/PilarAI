from fpdf import FPDF
from markdown import markdown
from bs4 import BeautifulSoup
from datetime import datetime

class PDF(FPDF):
    def __init__(self, template, user_data):
        super().__init__()
        self.template = template
        self.user_data = user_data
        self.current_indent = 0
        self.setup_fonts()
        self.setup_styles()
        
    def setup_fonts(self):
        main_font = self.template['styles']['main_font']
        try:
            self.add_font(main_font, style="", fname=f"fonts/{main_font.lower()}.ttf", uni=True)
            self.add_font(main_font, style="B", fname=f"fonts/{main_font.lower()}bd.ttf", uni=True)
        except:
            self.add_font("Arial", style="", fname="fonts/arial.ttf", uni=True)
            self.add_font("Arial", style="B", fname="fonts/arialbd.ttf", uni=True)
        self.set_font(self.template['styles']['main_font'], "", 12)
    
    def setup_styles(self):
        self.styles = {
            'h1': {
                'size': self.template['styles']['sizes']['h1'],
                'color': self.template['styles']['header_colors']['primary']
            },
            'h2': {
                'size': self.template['styles']['sizes']['h2'],
                'color': self.template['styles']['header_colors']['secondary']
            },
            'h3': {
                'size': self.template['styles']['sizes']['h3'],
                'color': self.template['styles']['header_colors']['tertiary']
            },
            'body': {
                'size': 12,
                'color': self.template['styles']['text_color']
            }
        }
        
    def header(self):
        # Add user information header
        header_text = (
            f"{self.user_data['firstName']} {self.user_data['lastName']} | "
            f"{self.user_data['course']} | "
            f"{datetime.now().strftime('%Y-%m-%d')}"
        )
        self.set_font(self.template['styles']['main_font'], 'B', 14)
        self.set_text_color(*self.hex_to_rgb(self.template['styles']['header_colors']['primary']))
        self.cell(0, 10, header_text, border=0, ln=1, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font(self.template['styles']['main_font'], 'I', 8)
        self.set_text_color(*self.hex_to_rgb(self.template['footer']['style']['color']))
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')
        
    def add_markdown_content(self, md_content):
        html = markdown(md_content)
        self.process_html(html)

    def process_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        self.parse_element(soup)

    def parse_element(self, element):
        for child in element.children:
            if child.name in ['h1', 'h2', 'h3']:
                self.add_heading(child.text, level=int(child.name[1]))
            elif child.name == 'p':
                self.add_paragraph(child.text)
            elif child.name == 'ul':
                self.process_list(child)
            elif child.name == 'strong':
                self.add_text(child.text, style='B')
            else:
                if hasattr(child, 'text'):
                    self.add_text(child.text)

    def add_heading(self, text, level=1):
        self.ln(10)
        style = self.styles[f'h{level}']
        self.set_font("Arial", 'B', style['size'])
        self.set_text_color(*self.hex_to_rgb(style['color']))
        self.multi_cell(0, 10, text)
        self.reset_styles()
        self.ln(5)

    def add_paragraph(self, text):
        self.set_font("Arial", '', self.styles['body']['size'])
        self.set_text_color(*self.hex_to_rgb(self.styles['body']['color']))
        self.multi_cell(0, 5, text)
        self.ln(3)

    def process_list(self, element):
        self.current_indent += 15
        for item in element.find_all('li'):
            self.ln(3)
            self.cell(self.current_indent)
            self.add_text('• ' + item.text)
        self.current_indent -= 15

    def add_text(self, text, style=''):
        self.set_font("Arial", style, self.styles['body']['size'])
        self.multi_cell(0, 5, text)
        self.ln(2)

    def reset_styles(self):
        self.set_font("Arial", '', self.styles['body']['size'])
        self.set_text_color(*self.hex_to_rgb(self.styles['body']['color']))

    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_pdf(md_content, template, user_data, output_path):
    pdf = PDF(template, user_data)
    pdf.add_page()
    pdf.add_markdown_content(md_content)
    pdf.output(output_path)