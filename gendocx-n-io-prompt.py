import os
from docxtpl import DocxTemplate

def main():
    template_path = "template.docx"
    output_path = "generated_document.docx"
    
    if not os.path.exists(template_path):
        print(f"Error: Could not find '{template_path}' in the current directory.")
        return

    print("--- Word Document Automation Tool ---")
    
    # 1. Collect inputs dynamically from the prompt
    context = {
        "client_name": input("Enter Client Name: "),
        "project_name": input("Enter Project Name: "),
        "amount": input("Enter Invoice Amount ($): "),
        "due_date": input("Enter Due Date (YYYY-MM-DD): ")
    }
    
    # 2. Load the template and inject data
    try:
        doc = DocxTemplate(template_path)
        doc.render(context)
        doc.save(output_path)
        print(f"\nSuccess! Document saved as '{output_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
