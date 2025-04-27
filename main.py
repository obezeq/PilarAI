"""
PilarAI - Smart Academic Assistant Main Module

This module serves as the entry point for the PilarAI application. It coordinates:
- Template loading
- User input handling
- AI solution generation
- PDF document creation
"""

import openai_handler
import template_manager
import pdf_generator
import json
import os

def main():
    """Main execution flow for PilarAI academic assistant application.
    
    Handles:
    1. Template configuration loading
    2. User task input collection
    3. AI-powered solution generation
    4. PDF document creation
    5. Error handling and user feedback
    
    Raises:
        FileNotFoundError: If template configuration files are missing
        Exception: General errors during solution generation or PDF creation
    """
    # Initial configuration
    print("🚀 Welcome to PilarAI - Your smart academic assistant\n")
    
    # Load template
    try:
        template = template_manager.load_template("config/template.json")
    except FileNotFoundError:
        print("Error: Template file not found in config/template.json")
        return
    
    # Get user task
    task = input("📝 Enter the task you need to solve:\n> ")
    
    # Generate solution with OpenAI
    print("\n⚡ Generating solution...")
    try:
        markdown_content = openai_handler.generate_solution(task)
        os.makedirs("results", exist_ok=True)
        with open("results/solution.txt", "w", encoding="utf-8") as f:
            f.write(markdown_content)
    except Exception as e:
        print(f"Error generating solution: {str(e)}")
        return
    
    # Generate PDF
    print("🎨 Creating PDF document...")
    try:
        user_data = template_manager.load_user_data("config/user.json")
        pdf_generator.create_pdf(markdown_content, template, user_data, "results/solution.pdf")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return
    
    print("\n✅ Task completed! Check the files in the 'results' folder")

if __name__ == "__main__":
    main()