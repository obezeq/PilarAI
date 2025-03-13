import openai_handler
import template_manager
import pdf_generator
import json

def main():
    # Configuración inicial
    print("🚀 Bienvenido a PilarAI - Tu asistente académico inteligente\n")
    
    # Cargar plantilla
    try:
        template = template_manager.load_template("config/template.json")
    except FileNotFoundError:
        print("Error: No se encontró el archivo de plantilla en config/template.json")
        return
    
    # Obtener tarea del usuario
    task = input("📝 Ingresa la tarea que necesitas resolver:\n> ")
    
    # Generar solución con OpenAI
    print("\n⚡ Generando solución...")
    try:
        markdown_content = openai_handler.generate_solution(task)
        with open("resultados/solucion.txt", "w", encoding="utf-8") as f:
            f.write(markdown_content)
    except Exception as e:
        print(f"Error al generar la solución: {str(e)}")
        return
    
    # Generar PDF
    print("🎨 Creando documento PDF...")
    try:
        user_data = template_manager.load_user_data("config/usuario.json")
        pdf_generator.create_pdf(markdown_content, template, user_data, "resultados/solucion.pdf")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return
    
    print("\n✅ ¡Tarea completada! Revisa los archivos en la carpeta 'resultados'")

if __name__ == "__main__":
    main()