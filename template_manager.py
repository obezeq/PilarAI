"""
Template Management Module

Handles loading and validation of:
- Document templates
- User configuration files
"""

import json
from datetime import datetime

def load_template(path: str) -> dict:
    """Loads and validates PDF template configuration.
    
    Args:
        path: Path to template.json file
        
    Returns:
        dict: Validated template configuration
        
    Raises:
        FileNotFoundError: If template file is missing
        ValueError: For invalid template structure
    """
    with open(path, 'r') as f:
        template = json.load(f)
    validate_template(template)
    return template

def load_user_data(path: str) -> dict:
    """Loads user configuration data.
    
    Args:
        path: Path to user.json file
        
    Returns:
        dict: User configuration data
    """
    with open(path, 'r') as f:
        user_data = json.load(f)
    return user_data

def validate_template(template: dict):
    """Validates template structure and required fields.
    
    Args:
        template: Template configuration to validate
        
    Raises:
        ValueError: For missing required fields
    """
    required_fields = ['styles', 'header', 'footer']
    for field in required_fields:
        if field not in template:
            raise ValueError(f"Invalid template: Missing required field '{field}'")