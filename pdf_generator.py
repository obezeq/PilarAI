#!/usr/bin/python3

"""
PDF Generation Module

Creates styled PDF documents from Markdown content using:
- FPDF2 for PDF creation
- BeautifulSoup for HTML/Markdown parsing
"""

from fpdf import FPDF
from markdown import markdown
from bs4 import BeautifulSoup
from datetime import datetime

class PDF(FPDF):
    """Custom PDF generator with academic styling and user data integration.
    
    Attributes:
        template: Document styling configuration
        user_data: User information for header/footer
        current_indent: Current list indentation level
        styles: Predefined text styling configurations
    """
    
    def __init__(self, template: dict, user_data: dict):
        """Initializes PDF document with template and user data.
        
        Args:
            template: Style configuration dictionary
            user_data: User information dictionary
        """
        super().__init__()
        self.template = template
        self.user_data = user_data
        self.current_indent = 0
        self.setup_fonts()
        self.setup_styles()
        
    def setup_fonts(self):
        """Configures document fonts with fallback to Arial."""
        main_font = self.template['styles']['main_font']
        try:
            self.add_font(main_font, style="", fname=f"fonts/{main_font.lower()}.ttf", uni=True)
            self.add_font(main_font, style="B", fname=f"fonts/{main_font.lower()}bd.ttf", uni=True)
        except:
            self.add_font("Arial", style="", fname="fonts/arial.ttf", uni=True)
            self.add_font("Arial", style="B", fname="fonts/arialbd.ttf", uni=True)
        self.set_font(self.template['styles']['main_font'], "", 12)
    
    def setup_styles(self):
        """Initializes document styles from template configuration."""
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
        """Generates document header with user information."""
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
        """Generates document footer with page numbers."""
        self.set_y(-15)
        self.set_font(self.template['styles']['main_font'], 'I', 8)
        self.set_text_color(*self.hex_to_rgb(self.template['footer']['style']['color']))
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')
        
    def add_markdown_content(self, md_content: str):
        """Converts Markdown content to PDF elements.
        
        Args:
            md_content: Markdown-formatted text content
        """
        html = markdown(md_content)
        self.process_html(html)

    def process_html(self, html: str):
        """Parses HTML content and converts to PDF elements.
        
        Args:
            html: HTML content to process
        """
        soup = BeautifulSoup(html, 'html.parser')
        self.parse_element(soup)

    def parse_element(self, element):
        """Recursively processes HTML elements for PDF conversion.
        
        Args:
            element: BeautifulSoup element to process
        """
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

    def add_heading(self, text: str, level: int = 1):
        """Adds styled heading to PDF document.
        
        Args:
            text: Heading text content
            level: Heading level (1-3)
        """
        self.ln(10)
        style = self.styles[f'h{level}']
        self.set_font("Arial", 'B', style['size'])
        self.set_text_color(*self.hex_to_rgb(style['color']))
        self.multi_cell(0, 10, text)
        self.reset_styles()
        self.ln(5)

    def add_paragraph(self, text: str):
        """Adds standard paragraph text to PDF document.
        
        Args:
            text: Paragraph content
        """
        self.set_font("Arial", '', self.styles['body']['size'])
        self.set_text_color(*self.hex_to_rgb(self.styles['body']['color']))
        self.multi_cell(0, 5, text)
        self.ln(3)

    def process_list(self, element):
        """Processes HTML list elements with proper indentation.
        
        Args:
            element: BeautifulSoup list element
        """
        self.current_indent += 15
        for item in element.find_all('li'):
            self.ln(3)
            self.cell(self.current_indent)
            self.add_text('• ' + item.text)
        self.current_indent -= 15

    def add_text(self, text: str, style: str = ''):
        """Adds formatted text to PDF document.
        
        Args:
            text: Text content to add
            style: Font style (B/I/U)
        """
        self.set_font("Arial", style, self.styles['body']['size'])
        self.multi_cell(0, 5, text)
        self.ln(2)

    def reset_styles(self):
        """Resets text styling to default body style."""
        self.set_font("Arial", '', self.styles['body']['size'])
        self.set_text_color(*self.hex_to_rgb(self.styles['body']['color']))

    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple:
        """Converts hexadecimal color code to RGB tuple.
        
        Args:
            hex_color: Color code in #RRGGBB format
            
        Returns:
            tuple: (R, G, B) values (0-255)
        """
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_pdf(md_content: str, template: dict, user_data: dict, output_path: str):
    """Generates PDF document from Markdown content.
    
    Args:
        md_content: Markdown-formatted text
        template: Style configuration dictionary
        user_data: User information dictionary
        output_path: Destination path for PDF file
    """
    pdf = PDF(template, user_data)
    pdf.add_page()
    pdf.add_markdown_content(md_content)
    pdf.output(output_path)