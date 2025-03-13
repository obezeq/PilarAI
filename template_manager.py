import json
from datetime import datetime

def load_template(path):
    with open(path, 'r') as f:
        template = json.load(f)
    validate_template(template)
    return template

def load_user_data(path):
    with open(path, 'r') as f:
        user_data = json.load(f)
    return user_data

def validate_template(template):
    required_fields = ['estilos', 'encabezado', 'pie_pagina']
    for field in required_fields:
        if field not in template:
            raise ValueError(f"Plantilla inválida: Falta el campo '{field}'")