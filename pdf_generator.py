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
        self.add_font("Arial", style="", fname="fonts/arial.ttf", uni=True)
        self.add_font("Arial", style="B", fname="fonts/arialbd.ttf", uni=True)
        self.set_font("Arial", "", 12)
    
    def setup_styles(self):
        self.styles = {
            'h1': {'size': 24, 'color': '#2c3e50'},
            'h2': {'size': 20, 'color': '#34495e'},
            'h3': {'size': 16, 'color': '#4a6572'},
            'body': {'size': 12, 'color': '#333333'}
        }
        
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